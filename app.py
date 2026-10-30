import os
import json
import re
import random
import difflib
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, send_file, Response

app = Flask(__name__, static_folder="static", template_folder="templates")
app.secret_key = os.environ.get("SECRET_KEY", "guess-the-thing-ultra-secret-key-2026")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_FILE = os.path.join(BASE_DIR, "data", "questions.json")
EXTRA_CATALOGS_FILE = os.path.join(BASE_DIR, "data", "extra_catalogs.json")
LEADERBOARD_FILE = os.path.join(BASE_DIR, "data", "leaderboard.json")
USERS_FILE = os.path.join(BASE_DIR, "data", "users.json")

ALL_VISUAL_CATEGORIES = ("movies", "anime", "common_objects", "superheroes", "games", "characters")

CATEGORY_DISPLAY_NAMES = {
    "movies": "Movies",
    "anime": "Anime",
    "common_objects": "Common Object",
    "superheroes": "Superheroes",
    "games": "Games",
    "characters": "Characters"
}

# -------------------------------------------------------------
# DATA & USER HELPERS
# -------------------------------------------------------------

def load_questions():
    """Load question repository from JSON file."""
    if os.path.exists(QUESTIONS_FILE):
        try:
            with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print("Error loading questions:", e)
    return []

def load_extra_catalogs():
    """Load extended autocomplete catalogs across all categories."""
    if os.path.exists(EXTRA_CATALOGS_FILE):
        try:
            with open(EXTRA_CATALOGS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print("Error loading extra catalogs:", e)
    return {}

def load_users():
    """Load registered user accounts and score histories."""
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print("Error loading users:", e)
    return {}

def save_users(users):
    """Persist user accounts and score histories to JSON."""
    try:
        os.makedirs(os.path.dirname(USERS_FILE), exist_ok=True)
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump(users, f, indent=2)
    except Exception as e:
        print("Error saving users:", e)

def get_current_user():
    """Return the currently logged-in user's dictionary or None."""
    username = session.get("username")
    if not username:
        return None
    users = load_users()
    user = users.get(username.lower())
    if not user:
        return None
    history = user.get("history", [])
    total_games = len(history)
    best_score = max((h.get("score", 0) for h in history), default=0)
    best_streak = max((h.get("streak", 0) for h in history), default=0)
    avg_accuracy = round(sum(h.get("accuracy", 0) for h in history) / total_games, 1) if total_games > 0 else 0
    return {
        "username": user.get("username", username),
        "joined": user.get("joined", "2026"),
        "history": history,
        "total_games": total_games,
        "best_score": best_score,
        "best_streak": best_streak,
        "avg_accuracy": avg_accuracy
    }

@app.context_processor
def inject_user():
    """Make current_user available across all Jinja templates."""
    return {"current_user": get_current_user()}

def normalize_text(text):
    """Normalize user input and target answers for forgiving matching."""
    if not text:
        return ""
    text = text.lower().strip()
    return re.sub(r"[^a-z0-9]", "", text)

def get_category_catalog(category="movies"):
    """Return deduplicated catalog for autocomplete & 6-attribute comparison."""
    questions = load_questions()
    items = [q for q in questions if q.get("category") == category]
    seen = {normalize_text(m.get("name", "")) for m in items}

    extra_catalogs = load_extra_catalogs()
    extra_pool = extra_catalogs.get(category, [])

    for extra in extra_pool:
        norm = normalize_text(extra.get("name", ""))
        if norm and norm not in seen:
            items.append(extra)
            seen.add(norm)
    return sorted(items, key=lambda m: m.get("name", ""))

def find_item_by_guess(guess, category="movies"):
    """Find an item object in the category catalog matching the user's guess."""
    norm_guess = normalize_text(guess)
    if not norm_guess:
        return None

    catalog = get_category_catalog(category)
    for item in catalog:
        if norm_guess == normalize_text(item.get("name", "")):
            return item
        for alias in item.get("aliases", []):
            if norm_guess == normalize_text(alias):
                return item

    norm_map = {normalize_text(m.get("name", "")): m for m in catalog}
    close = difflib.get_close_matches(norm_guess, list(norm_map.keys()), n=1, cutoff=0.65)
    if close:
        return norm_map[close[0]]

    for norm_name, item in norm_map.items():
        if norm_guess in norm_name or norm_name in norm_guess:
            return item

    return None

def check_answer(guess, question):
    """Verify if user guess matches target name or any recognized alias."""
    norm_guess = normalize_text(guess)
    if not norm_guess:
        return False

    if norm_guess == normalize_text(question.get("name", "")):
        return True

    for alias in question.get("aliases", []):
        if norm_guess == normalize_text(alias):
            return True

    return False

def build_guess_comparison(guess_text, target_question):
    """Compare a guessed item against the target across all 6 attributes."""
    cat = target_question.get("category", "movies")
    guessed_item = find_item_by_guess(guess_text, category=cat)
    is_correct = check_answer(guess_text, target_question)
    if is_correct:
        guessed_item = target_question

    target_year = int(target_question.get("year", 2000))
    target_director = target_question.get("director", "Unknown")
    target_actor = target_question.get("actor", "Unknown")
    target_rated = target_question.get("rated", "PG-13")
    target_genres = target_question.get("genres", [])
    target_studio = target_question.get("studio", "Unknown")

    if guessed_item:
        guess_name = guessed_item.get("name", guess_text)
        guess_year = int(guessed_item.get("year", 0))
        guess_director = guessed_item.get("director", "Unknown")
        guess_actor = guessed_item.get("actor", "Unknown")
        guess_rated = guessed_item.get("rated", "N/A")
        guess_genres = guessed_item.get("genres", [])
        guess_studio = guessed_item.get("studio", "Unknown")

        year_close_threshold = 50 if cat == "common_objects" else (10 if cat in ("superheroes", "characters") else 5)
        if guess_year == target_year:
            year_status = "green"
            year_hint = "✓ Exact"
            year_arrow = "✓"
        else:
            year_diff = abs(guess_year - target_year)
            year_status = "yellow" if year_diff <= year_close_threshold else "wrong"
            if target_year > guess_year:
                year_hint = "↑ Higher"
                year_arrow = "↑"
            else:
                year_hint = "↓ Lower"
                year_arrow = "↓"

        director_status = "green" if normalize_text(guess_director) == normalize_text(target_director) else "wrong"
        actor_status = "green" if normalize_text(guess_actor) == normalize_text(target_actor) else "wrong"
        rated_status = "green" if normalize_text(guess_rated) == normalize_text(target_rated) else "wrong"

        g_set = {g.lower().strip() for g in guess_genres}
        t_set = {g.lower().strip() for g in target_genres}
        if g_set and g_set == t_set:
            genres_status = "green"
        elif g_set and (g_set & t_set):
            genres_status = "green" if list(guess_genres)[0].lower() == list(target_genres)[0].lower() else "yellow"
        else:
            genres_status = "wrong"

        studio_status = "green" if normalize_text(guess_studio) == normalize_text(target_studio) else "wrong"

        return {
            "guess_name": guess_name,
            "is_correct": is_correct,
            "recognized": True,
            "year": guess_year,
            "year_status": year_status,
            "year_hint": year_hint,
            "year_arrow": year_arrow,
            "director": guess_director,
            "director_status": director_status,
            "actor": guess_actor,
            "actor_status": actor_status,
            "rated": guess_rated,
            "rated_status": rated_status,
            "genres": ", ".join(guess_genres) if isinstance(guess_genres, list) else str(guess_genres),
            "genres_status": genres_status,
            "studio": guess_studio,
            "studio_status": studio_status
        }
    else:
        return {
            "guess_name": guess_text,
            "is_correct": False,
            "recognized": False,
            "year": "?",
            "year_status": "wrong",
            "year_hint": "Use dropdown",
            "year_arrow": "?",
            "director": "Not in list",
            "director_status": "wrong",
            "actor": "Not in list",
            "actor_status": "wrong",
            "rated": "?",
            "rated_status": "wrong",
            "genres": "Pick from dropdown",
            "genres_status": "wrong",
            "studio": "Not in list",
            "studio_status": "wrong"
        }

def render_common_object_svg(question):
    """Generates a detailed, unmistakable vector object illustration designed for Black Silhouette & Color Reveal."""
    stype = question.get("silhouette_type", "umbrella")
    shapes = {
        "umbrella": """
            <path d="M300 65 C195 65, 130 140, 125 190 C155 175, 190 175, 215 190 C240 175, 275 175, 300 190 C325 175, 360 175, 385 190 C410 175, 445 175, 475 190 C470 140, 405 65, 300 65 Z" fill="#ef4444" stroke="#b91c1c" stroke-width="6"/>
            <rect x="295" y="48" width="10" height="230" rx="5" fill="#94a3b8"/>
            <path d="M300 272 L300 295 C300 318, 265 318, 265 295" fill="none" stroke="#eab308" stroke-width="14" stroke-linecap="round"/>
        """,
        "scissors": """
            <g transform="translate(300,180) rotate(-25) translate(-300,-180)">
                <polygon points="285,175 305,175 365,55 340,45" fill="#cbd5e1" stroke="#64748b" stroke-width="4"/>
                <polygon points="315,175 295,175 235,55 260,45" fill="#e2e8f0" stroke="#64748b" stroke-width="4"/>
                <circle cx="300" cy="175" r="9" fill="#475569"/>
                <circle cx="255" cy="255" r="42" fill="none" stroke="#ef4444" stroke-width="18"/>
                <circle cx="345" cy="255" r="42" fill="none" stroke="#ef4444" stroke-width="18"/>
                <line x1="278" y1="220" x2="296" y2="180" stroke="#ef4444" stroke-width="16" stroke-linecap="round"/>
                <line x1="322" y1="220" x2="304" y2="180" stroke="#ef4444" stroke-width="16" stroke-linecap="round"/>
            </g>
        """,
        "lightbulb": """
            <path d="M300 50 C235 50, 195 95, 195 150 C195 190, 225 215, 245 245 L355 245 C375 215, 405 190, 405 150 C405 95, 365 50, 300 50 Z" fill="#fde047" stroke="#eab308" stroke-width="6"/>
            <path d="M275 245 L275 160 L290 140 L300 160 L310 140 L325 160 L325 245" fill="none" stroke="#f97316" stroke-width="5"/>
            <rect x="250" y="245" width="100" height="48" rx="10" fill="#94a3b8" stroke="#475569" stroke-width="5"/>
            <line x1="250" y1="262" x2="350" y2="262" stroke="#475569" stroke-width="5"/>
            <line x1="250" y1="278" x2="350" y2="278" stroke="#475569" stroke-width="5"/>
            <path d="M270 293 C275 315, 325 315, 330 293 Z" fill="#1e293b"/>
        """,
        "headphones": """
            <path d="M180 210 L180 165 C180 90, 230 55, 300 55 C370 55, 420 90, 420 165 L420 210" fill="none" stroke="#3b82f6" stroke-width="22" stroke-linecap="round"/>
            <rect x="148" y="185" width="48" height="95" rx="22" fill="#1e293b" stroke="#60a5fa" stroke-width="6"/>
            <rect x="404" y="185" width="48" height="95" rx="22" fill="#1e293b" stroke="#60a5fa" stroke-width="6"/>
            <rect x="186" y="198" width="16" height="70" rx="8" fill="#64748b"/>
            <rect x="398" y="198" width="16" height="70" rx="8" fill="#64748b"/>
        """,
        "key": """
            <g transform="translate(300,180) rotate(-15) translate(-300,-180)">
                <circle cx="195" cy="180" r="62" fill="#facc15" stroke="#ca8a04" stroke-width="8"/>
                <circle cx="195" cy="180" r="24" fill="#e2e8f0"/>
                <path d="M255 164 L455 164 L470 180 L455 196 L430 196 L430 226 L405 226 L405 196 L380 196 L380 218 L355 218 L355 196 L255 196 Z" fill="#facc15" stroke="#ca8a04" stroke-width="6"/>
            </g>
        """,
        "mug": """
            <path d="M350 135 L405 135 C440 135, 440 245, 405 245 L350 245" fill="none" stroke="#f97316" stroke-width="22" stroke-linecap="round"/>
            <rect x="180" y="105" width="180" height="185" rx="22" fill="#f97316" stroke="#c2410c" stroke-width="6"/>
            <path d="M235 85 C225 65, 245 55, 235 35" fill="none" stroke="#94a3b8" stroke-width="6" stroke-linecap="round"/>
            <path d="M275 85 C265 65, 285 55, 275 35" fill="none" stroke="#94a3b8" stroke-width="6" stroke-linecap="round"/>
            <path d="M315 85 C305 65, 325 55, 315 35" fill="none" stroke="#94a3b8" stroke-width="6" stroke-linecap="round"/>
        """,
        "bicycle": """
            <circle cx="185" cy="230" r="62" fill="none" stroke="#1e293b" stroke-width="16"/>
            <circle cx="415" cy="230" r="62" fill="none" stroke="#1e293b" stroke-width="16"/>
            <polygon points="185,230 265,140 375,140 285,230" fill="none" stroke="#ef4444" stroke-width="12" stroke-linejoin="round"/>
            <line x1="265" y1="140" x2="285" y2="230" stroke="#ef4444" stroke-width="12"/>
            <line x1="375" y1="140" x2="415" y2="230" stroke="#ef4444" stroke-width="12"/>
            <line x1="375" y1="140" x2="360" y2="100" stroke="#334155" stroke-width="10" stroke-linecap="round"/>
            <line x1="340" y1="100" x2="388" y2="100" stroke="#1e293b" stroke-width="12" stroke-linecap="round"/>
            <line x1="265" y1="140" x2="255" y2="112" stroke="#334155" stroke-width="10"/>
            <rect x="232" y="102" width="48" height="14" rx="7" fill="#1e293b"/>
        """,
        "glasses": """
            <rect x="130" y="135" width="140" height="95" rx="26" fill="#bae6fd" stroke="#1e293b" stroke-width="16"/>
            <rect x="330" y="135" width="140" height="95" rx="26" fill="#bae6fd" stroke="#1e293b" stroke-width="16"/>
            <path d="M270 165 C285 148, 315 148, 330 165" fill="none" stroke="#1e293b" stroke-width="14"/>
            <line x1="100" y1="155" x2="130" y2="155" stroke="#1e293b" stroke-width="14" stroke-linecap="round"/>
            <line x1="470" y1="155" x2="500" y2="155" stroke="#1e293b" stroke-width="14" stroke-linecap="round"/>
        """,
        "guitar": """
            <g transform="translate(300,180) rotate(-35) translate(-300,-180)">
                <path d="M260 190 C220 190, 215 240, 245 255 C210 275, 215 335, 300 335 C385 335, 390 275, 355 255 C385 240, 380 190, 340 190 Z" fill="#d97706" stroke="#78350f" stroke-width="6"/>
                <circle cx="300" cy="248" r="24" fill="#292524"/>
                <rect x="286" y="42" width="28" height="160" fill="#78350f"/>
                <rect x="280" y="18" width="40" height="32" rx="6" fill="#451a03"/>
                <rect x="275" y="292" width="50" height="12" rx="3" fill="#292524"/>
            </g>
        """,
        "hammer": """
            <g transform="translate(300,180) rotate(-25) translate(-300,-180)">
                <rect x="284" y="110" width="32" height="210" rx="10" fill="#d97706" stroke="#78350f" stroke-width="5"/>
                <path d="M210 75 L340 75 L340 120 L255 120 C235 120, 215 135, 200 155 C205 120, 210 95, 210 75 Z" fill="#64748b" stroke="#334155" stroke-width="5"/>
                <rect x="335" y="68" width="38" height="60" rx="6" fill="#475569" stroke="#1e293b" stroke-width="5"/>
            </g>
        """,
        "watch": """
            <rect x="262" y="32" width="76" height="296" rx="14" fill="#92400e" stroke="#451a03" stroke-width="5"/>
            <circle cx="300" cy="180" r="78" fill="#f8fafc" stroke="#eab308" stroke-width="14"/>
            <rect x="382" y="168" width="14" height="24" rx="4" fill="#eab308"/>
            <line x1="300" y1="180" x2="300" y2="128" stroke="#1e293b" stroke-width="8" stroke-linecap="round"/>
            <line x1="300" y1="180" x2="342" y2="180" stroke="#ef4444" stroke-width="6" stroke-linecap="round"/>
            <circle cx="300" cy="180" r="7" fill="#1e293b"/>
        """,
        "camera": """
            <rect x="210" y="82" width="90" height="32" rx="8" fill="#334155"/>
            <rect x="370" y="90" width="36" height="20" rx="5" fill="#ef4444"/>
            <rect x="145" y="105" width="310" height="190" rx="26" fill="#1e293b" stroke="#475569" stroke-width="6"/>
            <circle cx="300" cy="200" r="68" fill="#64748b" stroke="#cbd5e1" stroke-width="8"/>
            <circle cx="300" cy="200" r="44" fill="#0ea5e9"/>
            <circle cx="385" cy="142" r="14" fill="#fde047"/>
        """,
        "toothbrush": """
            <g transform="translate(300,180) rotate(-20) translate(-300,-180)">
                <rect x="120" y="175" width="360" height="26" rx="13" fill="#06b6d4" stroke="#0e7490" stroke-width="5"/>
                <rect x="135" y="132" width="95" height="44" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="4"/>
                <line x1="155" y1="132" x2="155" y2="175" stroke="#cbd5e1" stroke-width="4"/>
                <line x1="175" y1="132" x2="175" y2="175" stroke="#cbd5e1" stroke-width="4"/>
                <line x1="195" y1="132" x2="195" y2="175" stroke="#cbd5e1" stroke-width="4"/>
                <line x1="215" y1="132" x2="215" y2="175" stroke="#cbd5e1" stroke-width="4"/>
            </g>
        """,
        "backpack": """
            <path d="M265 65 C265 38, 335 38, 335 65" fill="none" stroke="#1e293b" stroke-width="14" stroke-linecap="round"/>
            <path d="M185 110 C150 130, 150 250, 185 270" fill="none" stroke="#334155" stroke-width="18" stroke-linecap="round"/>
            <path d="M415 110 C450 130, 450 250, 415 270" fill="none" stroke="#334155" stroke-width="18" stroke-linecap="round"/>
            <rect x="185" y="65" width="230" height="245" rx="48" fill="#ef4444" stroke="#991b1b" stroke-width="6"/>
            <rect x="215" y="180" width="170" height="105" rx="22" fill="#f87171" stroke="#991b1b" stroke-width="5"/>
            <line x1="215" y1="210" x2="385" y2="210" stroke="#fde047" stroke-width="6"/>
        """,
        "hourglass": """
            <rect x="195" y="45" width="210" height="22" rx="8" fill="#92400e"/>
            <rect x="195" y="293" width="210" height="22" rx="8" fill="#92400e"/>
            <line x1="215" y1="67" x2="215" y2="293" stroke="#92400e" stroke-width="10"/>
            <line x1="385" y1="67" x2="385" y2="293" stroke="#92400e" stroke-width="10"/>
            <path d="M235 67 L365 67 L312 180 L365 293 L235 293 L288 180 Z" fill="#e0f2fe" stroke="#0284c7" stroke-width="6"/>
            <polygon points="250,290 350,290 300,225" fill="#facc15"/>
            <polygon points="265,125 335,125 300,175" fill="#facc15"/>
        """,
        "flashlight": """
            <g transform="translate(300,180) rotate(-18) translate(-300,-180)">
                <rect x="120" y="150" width="210" height="60" rx="12" fill="#334155" stroke="#0f172a" stroke-width="6"/>
                <polygon points="330,150 395,118 395,242 330,210" fill="#ef4444" stroke="#991b1b" stroke-width="6"/>
                <rect x="395" y="114" width="18" height="132" rx="6" fill="#fde047"/>
                <rect x="210" y="136" width="38" height="14" rx="5" fill="#ef4444"/>
                <polygon points="413,120 530,75 530,285 413,240" fill="rgba(253,224,71,0.45)"/>
            </g>
        """,
        "magnifying_glass": """
            <line x1="340" y1="215" x2="455" y2="315" stroke="#78350f" stroke-width="28" stroke-linecap="round"/>
            <circle cx="265" cy="145" r="88" fill="#bae6fd" stroke="#eab308" stroke-width="18"/>
            <path d="M220 105 A55 55 0 0 1 295 95" fill="none" stroke="#ffffff" stroke-width="8" stroke-linecap="round"/>
        """,
        "padlock": """
            <path d="M235 160 L235 105 C235 55, 365 55, 365 105 L365 160" fill="none" stroke="#94a3b8" stroke-width="26" stroke-linecap="round"/>
            <rect x="195" y="150" width="210" height="165" rx="26" fill="#eab308" stroke="#ca8a04" stroke-width="8"/>
            <circle cx="300" cy="218" r="18" fill="#1e293b"/>
            <polygon points="292,225 308,225 314,268 286,268" fill="#1e293b"/>
        """,
        "teapot": """
            <path d="M195 155 C140 155, 140 255, 195 255" fill="none" stroke="#0284c7" stroke-width="22" stroke-linecap="round"/>
            <path d="M395 225 C435 215, 450 150, 480 140" fill="none" stroke="#0284c7" stroke-width="24" stroke-linecap="round"/>
            <ellipse cx="295" cy="210" rx="115" ry="85" fill="#38bdf8" stroke="#0284c7" stroke-width="8"/>
            <path d="M230 132 C255 105, 335 105, 360 132 Z" fill="#0284c7"/>
            <circle cx="295" cy="100" r="16" fill="#eab308"/>
        """,
        "microphone": """
            <g transform="translate(300,180) rotate(30) translate(-300,-180)">
                <polygon points="274,155 326,155 314,305 286,305" fill="#1e293b" stroke="#475569" stroke-width="5"/>
                <circle cx="300" cy="105" r="56" fill="#94a3b8" stroke="#475569" stroke-width="7"/>
                <line x1="246" y1="105" x2="354" y2="105" stroke="#334155" stroke-width="7"/>
            </g>
        """,
        "trophy": """
            <path d="M210 95 C145 95, 150 185, 225 185" fill="none" stroke="#eab308" stroke-width="18" stroke-linecap="round"/>
            <path d="M390 95 C455 95, 450 185, 375 185" fill="none" stroke="#eab308" stroke-width="18" stroke-linecap="round"/>
            <path d="M205 70 L395 70 L375 190 C365 235, 235 235, 225 190 Z" fill="#facc15" stroke="#ca8a04" stroke-width="7"/>
            <rect x="282" y="220" width="36" height="55" fill="#eab308"/>
            <rect x="220" y="275" width="160" height="42" rx="8" fill="#451a03" stroke="#78350f" stroke-width="5"/>
        """,
        "anchor": """
            <circle cx="300" cy="65" r="22" fill="none" stroke="#475569" stroke-width="14"/>
            <line x1="300" y1="87" x2="300" y2="295" stroke="#475569" stroke-width="20" stroke-linecap="round"/>
            <line x1="225" y1="135" x2="375" y2="135" stroke="#475569" stroke-width="18" stroke-linecap="round"/>
            <path d="M175 215 C195 315, 405 315, 425 215" fill="none" stroke="#475569" stroke-width="20" stroke-linecap="round"/>
            <polygon points="155,230 175,185 205,225" fill="#475569"/>
            <polygon points="445,230 425,185 395,225" fill="#475569"/>
        """,
        "crown": """
            <polygon points="145,265 125,120 215,190 300,90 385,190 475,120 455,265" fill="#facc15" stroke="#ca8a04" stroke-width="8" stroke-linejoin="round"/>
            <rect x="145" y="265" width="310" height="32" rx="8" fill="#eab308" stroke="#ca8a04" stroke-width="6"/>
            <circle cx="125" cy="112" r="14" fill="#ef4444"/>
            <circle cx="300" cy="82" r="16" fill="#3b82f6"/>
            <circle cx="475" cy="112" r="14" fill="#ef4444"/>
        """,
        "frying_pan": """
            <g transform="translate(300,180) rotate(-18) translate(-300,-180)">
                <line x1="340" y1="180" x2="505" y2="180" stroke="#334155" stroke-width="26" stroke-linecap="round"/>
                <circle cx="235" cy="180" r="105" fill="#1e293b" stroke="#475569" stroke-width="12"/>
                <circle cx="225" cy="175" r="46" fill="#f8fafc"/>
                <circle cx="230" cy="172" r="20" fill="#facc15"/>
            </g>
        """
    }
    shape_markup = shapes.get(stype, shapes["umbrella"])
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 360" width="100%" height="100%">
        <g id="objectShape">
            {shape_markup}
        </g>
    </svg>"""
    return Response(svg, mimetype="image/svg+xml")

def load_leaderboard():
    """Load leaderboard records."""
    if os.path.exists(LEADERBOARD_FILE):
        try:
            with open(LEADERBOARD_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print("Error loading leaderboard:", e)
    return []

def save_leaderboard(entries):
    """Persist leaderboard records to JSON file."""
    try:
        with open(LEADERBOARD_FILE, "w", encoding="utf-8") as f:
            json.dump(entries, f, indent=2)
    except Exception as e:
        print("Error saving leaderboard:", e)

def calculate_rank_title(accuracy, score):
    """Assign an honorary gaming title based on final match performance."""
    if accuracy >= 100:
        return "🌟 Omniscient Sage"
    elif accuracy >= 80 and score >= 1000:
        return "👑 Grandmaster of Trivia"
    elif accuracy >= 70:
        return "⚔️ Master Sleuth"
    elif accuracy >= 50:
        return "🧩 Skilled Deductive"
    elif accuracy >= 25:
        return "🌱 Trivia Apprentice"
    else:
        return "🔍 Rookie Seeker"

def record_match_for_user(game):
    """Automatically save completed game into the logged-in user's personal history and global leaderboard."""
    if not game or game.get("user_history_recorded"):
        return
    username = session.get("username")
    if not username:
        return

    users = load_users()
    user_key = username.lower()
    if user_key not in users:
        return

    history = game.get("history", [])
    total_q = len(get_game_questions(game))
    correct_count = sum(1 for h in history if h.get("correct"))
    accuracy = round((correct_count / total_q * 100), 1) if total_q > 0 else 0
    score = game.get("score", 0)
    streak = game.get("max_streak", 0)
    raw_cat = game.get("category", "movies")
    cat_label = CATEGORY_DISPLAY_NAMES.get(raw_cat, raw_cat.replace("_", " ").title())
    mode_label = "Random" if game.get("is_random_mode") else game.get("game_mode", "classic").capitalize()
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M")

    match_entry = {
        "date": date_str,
        "category": cat_label,
        "game_mode": mode_label,
        "score": score,
        "accuracy": accuracy,
        "correct_count": correct_count,
        "total_questions": total_q,
        "streak": streak,
        "rank_title": calculate_rank_title(accuracy, score)
    }

    users[user_key].setdefault("history", []).insert(0, match_entry)
    save_users(users)

    # Also auto-record to the global leaderboard for logged-in user
    if score > 0 and not game.get("score_saved"):
        entries = load_leaderboard()
        entries.append({
            "id": len(entries) + 1,
            "player_name": users[user_key].get("username", username),
            "score": score,
            "category": cat_label,
            "game_mode": mode_label,
            "difficulty": game.get("difficulty", "medium").capitalize(),
            "date": datetime.now().strftime("%Y-%m-%d"),
            "streak": streak
        })
        entries = sorted(entries, key=lambda x: x.get("score", 0), reverse=True)
        save_leaderboard(entries)
        game["score_saved"] = True

    game["user_history_recorded"] = True
    session.modified = True

# -------------------------------------------------------------
# AUTHENTICATION & USER PROFILE ROUTES
# -------------------------------------------------------------

@app.route("/signup", methods=["POST"])
def signup():
    """Register a new user account and log them in."""
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "").strip()

    if not username or len(username) < 2:
        flash("Please choose a username with at least 2 characters.", "warning")
        return redirect(request.referrer or url_for("home"))
    if not password or len(password) < 4:
        flash("Password must be at least 4 characters long.", "warning")
        return redirect(request.referrer or url_for("home"))

    users = load_users()
    user_key = username.lower()
    if user_key in users:
        flash(f"Username '{username}' is already taken. Try logging in!", "warning")
        return redirect(request.referrer or url_for("home"))

    users[user_key] = {
        "username": username,
        "password_hash": generate_password_hash(password),
        "joined": datetime.now().strftime("%Y-%m-%d"),
        "history": []
    }
    save_users(users)

    session["username"] = username
    session["player_name"] = username
    flash(f"✨ Welcome to Guess the Thing, {username}! Your account is ready and all your scores will now be saved to your history.", "success")
    return redirect(request.referrer or url_for("home"))

@app.route("/login", methods=["POST"])
def login():
    """Authenticate an existing user."""
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "").strip()

    users = load_users()
    user = users.get(username.lower())

    if not user or not check_password_hash(user.get("password_hash", ""), password):
        flash("Invalid username or password. Please try again.", "error")
        return redirect(request.referrer or url_for("home"))

    session["username"] = user.get("username", username)
    session["player_name"] = user.get("username", username)
    flash(f"👋 Welcome back, {user.get('username')}!", "success")
    return redirect(request.referrer or url_for("home"))

@app.route("/logout")
def logout():
    """Log out the current user."""
    username = session.pop("username", None)
    if username:
        flash(f"Logged out from {username}. See you next time!", "info")
    return redirect(url_for("home"))

@app.route("/profile")
def profile():
    """Display the logged-in user's score history and statistics."""
    user = get_current_user()
    if not user:
        flash("Please log in or sign up to view your personal Score History.", "warning")
        return redirect(url_for("home"))
    return render_template("profile.html", active_page="profile", user=user)

# -------------------------------------------------------------
# CORE GAME ROUTES
# -------------------------------------------------------------

@app.route("/")
def home():
    """Home setup page with live Leaderboard and User Account History."""
    entries = sorted(load_leaderboard(), key=lambda x: x.get("score", 0), reverse=True)
    return render_template(
        "index.html",
        active_page="home",
        leaderboard_entries=entries[:10]
    )

@app.route("/style.css")
def stylesheet():
    """Backwards compatibility for direct /style.css requests."""
    return send_file(os.path.join(BASE_DIR, "static", "style.css"), mimetype="text/css")

@app.route("/movie-poster/<question_id>")
def movie_poster(question_id):
    """
    Serves the visual image clue for Movies, Anime, Common Objects, and other categories.
    """
    questions = load_questions()
    question = next((q for q in questions if q.get("id") == question_id), None)
    cat = (question or {}).get("category", "movies")

    if cat == "common_objects" and question:
        return render_common_object_svg(question)

    folder_map = {
        "movies": "movies",
        "anime": "anime",
        "common_objects": "objects",
        "superheroes": "superheroes",
        "games": "games",
        "characters": "characters"
    }
    sub_dir = folder_map.get(cat, "movies")
    img_dir = os.path.join(BASE_DIR, "static", "images", sub_dir)
    for ext in ("jpg", "jpeg", "png", "webp"):
        candidate = os.path.join(img_dir, f"{question_id}.{ext}")
        if os.path.exists(candidate):
            return send_file(candidate)

    theme = (question or {}).get("poster_theme", {})
    bg1 = theme.get("bg1", "#0f172a")
    bg2 = theme.get("bg2", "#1e3a5f")
    accent = theme.get("accent", "#f59e0b")
    icon = theme.get("icon", "🎬")
    subtitle = theme.get("subtitle", "Mystery Clue")
    year = (question or {}).get("year", "")
    genres = ", ".join((question or {}).get("genres", ["Trivia"]))

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 360" width="100%" height="100%">
        <defs>
            <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="{bg1}"/>
                <stop offset="100%" stop-color="{bg2}"/>
            </linearGradient>
            <radialGradient id="glowGrad" cx="50%" cy="45%" r="50%">
                <stop offset="0%" stop-color="{accent}" stop-opacity="0.45"/>
                <stop offset="100%" stop-color="{accent}" stop-opacity="0"/>
            </radialGradient>
        </defs>
        <rect width="600" height="360" fill="url(#bgGrad)"/>
        <circle cx="300" cy="160" r="170" fill="url(#glowGrad)"/>
        <circle cx="300" cy="145" r="74" fill="rgba(0,0,0,0.35)" stroke="{accent}" stroke-width="3" stroke-dasharray="8 4"/>
        <text x="300" y="172" font-size="78" text-anchor="middle" dominant-baseline="middle">{icon}</text>
        <text x="300" y="262" font-family="Plus Jakarta Sans, sans-serif" font-size="24" font-weight="800" fill="#ffffff" text-anchor="middle" letter-spacing="1.5">{subtitle.upper()}</text>
        <text x="300" y="295" font-family="Plus Jakarta Sans, sans-serif" font-size="15" font-weight="600" fill="{accent}" text-anchor="middle" letter-spacing="2">{genres.upper()} • {year}</text>
    </svg>"""
    return Response(svg, mimetype="image/svg+xml")

def get_game_questions(game):
    """Resolve question objects from session question_ids."""
    if not game:
        return []
    if "question_ids" in game:
        all_q = {q.get("id"): q for q in load_questions()}
        return [all_q[qid] for qid in game["question_ids"] if qid in all_q]
    return game.get("questions", [])

def init_game_session(category="movies", difficulty="medium", clue_style="normal", game_mode="classic", player_name=None, rounds_count=5):
    """Helper to initialize a new game session."""
    all_questions = load_questions()
    if not player_name:
        player_name = session.get("username") or session.get("player_name") or "Player 1"

    is_random_mode = (game_mode == "random")
    if is_random_mode:
        category = random.choice(list(ALL_VISUAL_CATEGORIES))
        active_mode = random.choice(["classic", "timer"])
    else:
        active_mode = game_mode if game_mode in ("classic", "timer") else "classic"

    filtered = [q for q in all_questions if q.get("category") == category]
    if not filtered:
        filtered = all_questions

    selected_pool = list(filtered)
    random.shuffle(selected_pool)
    chosen_questions = selected_pool[:rounds_count]
    question_ids = [q.get("id") for q in chosen_questions if q.get("id")]

    max_attempts = 5

    session["player_name"] = player_name
    session["game"] = {
        "player_name": player_name,
        "category": category,
        "difficulty": difficulty,
        "clue_style": "normal",
        "game_mode": active_mode,
        "is_random_mode": is_random_mode,
        "rounds_count": len(question_ids),
        "question_ids": question_ids,
        "current_index": 0,
        "score": 0,
        "streak": 0,
        "max_streak": 0,
        "attempts_left": max_attempts,
        "max_attempts": max_attempts,
        "round_guesses": [],
        "hint_used": False,
        "history": [],
        "round_result": None,
        "score_saved": False,
        "user_history_recorded": False,
        "show_instructions": True
    }

@app.route("/start-game", methods=["POST"])
def start_game():
    """Initializes a new game session with chosen options."""
    all_questions = load_questions()
    if not all_questions:
        flash("Question vault is currently unavailable. Please try again.", "error")
        return redirect(url_for("home"))

    default_name = session.get("username") or "Player 1"
    player_name = request.form.get("player_name", default_name).strip() or default_name
    category = request.form.get("category", "movies").lower()
    difficulty = request.form.get("difficulty", "medium").lower()
    game_mode = request.form.get("gameMode", "classic").lower()

    try:
        rounds_count = int(request.form.get("rounds", 5))
    except ValueError:
        rounds_count = 5

    init_game_session(
        category=category,
        difficulty=difficulty,
        clue_style="normal",
        game_mode=game_mode,
        player_name=player_name,
        rounds_count=rounds_count
    )

    return redirect(url_for("play"))

@app.route("/play")
def play():
    """Interactive game arena."""
    game = session.get("game")
    questions = get_game_questions(game)
    if not game or not questions:
        init_game_session(category="movies", difficulty="medium", clue_style="normal", game_mode="classic")
        game = session.get("game")
        questions = get_game_questions(game)

    current_idx = game.get("current_index", 0)

    if current_idx >= len(questions):
        return redirect(url_for("results"))

    current_question = questions[current_idx]
    max_attempts = game.get("max_attempts", 5)
    attempts_left = game.get("attempts_left", 5)
    round_guesses = game.get("round_guesses", [])
    tries_used = len(round_guesses)

    show_instructions = game.get("show_instructions", False)
    if show_instructions:
        game["show_instructions"] = False
        session.modified = True

    q_cat = current_question.get("category", "movies")
    movie_catalog = get_category_catalog(q_cat)

    return render_template(
        "play.html",
        active_page="play",
        question=current_question,
        current_round=current_idx + 1,
        total_rounds=len(questions),
        score=game.get("score", 0),
        streak=game.get("streak", 0),
        game_mode=game.get("game_mode", "classic"),
        is_random_mode=game.get("is_random_mode", False),
        attempts_left=attempts_left,
        max_attempts=max_attempts,
        tries_used=tries_used,
        round_guesses=round_guesses,
        round_result=game.get("round_result"),
        show_instructions=show_instructions,
        movie_catalog=movie_catalog
    )

@app.route("/submit-guess", methods=["POST"])
def submit_guess():
    """Evaluates the player's guess for the active question."""
    game = session.get("game")
    if not game:
        return redirect(url_for("home"))

    current_idx = game.get("current_index", 0)
    questions = get_game_questions(game)
    if current_idx >= len(questions):
        return redirect(url_for("results"))

    question = questions[current_idx]
    guess = request.form.get("guess", "").strip()

    if not guess:
        flash("Please type or select an answer before submitting.", "warning")
        return redirect(url_for("play"))

    q_cat = question.get("category", "movies")
    is_correct = check_answer(guess, question)

    comparison = build_guess_comparison(guess, question)
    round_guesses = game.get("round_guesses", [])
    round_guesses.append(comparison)
    game["round_guesses"] = round_guesses
    if comparison.get("is_correct"):
        is_correct = True

    if is_correct:
        diff_points = {
            "easy": 100,
            "medium": 200,
            "hard": 350,
            "insane": 500
        }
        base_points = diff_points.get(question.get("difficulty", "easy"), 100)

        current_streak = game.get("streak", 0)
        multiplier = 1.0 + (current_streak * 0.2)
        points_earned = int(base_points * multiplier)

        if game.get("hint_used", False):
            points_earned = max(20, points_earned - 20)

        new_streak = current_streak + 1
        new_max_streak = max(game.get("max_streak", 0), new_streak)
        game["score"] = game.get("score", 0) + points_earned
        game["streak"] = new_streak
        game["max_streak"] = new_max_streak

        game["history"].append({
            "name": question.get("name"),
            "category": question.get("category"),
            "correct": True,
            "points": points_earned,
            "user_guess": guess
        })

        game["round_result"] = {
            "is_correct": True,
            "points_earned": points_earned
        }
    else:
        attempts = game.get("attempts_left", 5) - 1
        game["attempts_left"] = attempts

        if attempts > 0:
            if attempts == 1:
                if q_cat == "common_objects":
                    flash("🔓 4 tries used! The Black Silhouette has now REVEALED the full-color object for your final 5th try!", "info")
                else:
                    flash("🔓 4 tries used! The full blurred image has now REVEALED for your final 5th try!", "info")
            else:
                flash(f"Not quite! Check the unlocked clues & green/yellow tiles below — {attempts} {'try' if attempts == 1 else 'tries'} remaining.", "error")
            session.modified = True
            return redirect(url_for("play"))
        else:
            game["streak"] = 0
            game["history"].append({
                "name": question.get("name"),
                "category": question.get("category"),
                "correct": False,
                "points": 0,
                "user_guess": guess
            })
            game["round_result"] = {
                "is_correct": False,
                "points_earned": 0
            }

    session.modified = True
    return redirect(url_for("play"))

@app.route("/next-question")
def next_question():
    """Proceeds to next question after result display."""
    game = session.get("game")
    if not game:
        return redirect(url_for("home"))

    game["current_index"] = game.get("current_index", 0) + 1
    game["attempts_left"] = game.get("max_attempts", 5)
    game["round_guesses"] = []
    game["hint_used"] = False
    game["round_result"] = None
    session.modified = True

    questions = get_game_questions(game)
    if game["current_index"] >= len(questions):
        return redirect(url_for("results"))
    return redirect(url_for("play"))

@app.route("/skip-question", methods=["POST"])
def skip_question():
    """Skip the current question without points."""
    game = session.get("game")
    if not game:
        return redirect(url_for("home"))

    current_idx = game.get("current_index", 0)
    questions = get_game_questions(game)
    if current_idx < len(questions):
        question = questions[current_idx]
        game["streak"] = 0
        game["history"].append({
            "name": question.get("name"),
            "category": question.get("category"),
            "correct": False,
            "points": 0,
            "user_guess": "Skipped"
        })
        game["current_index"] = current_idx + 1
        game["attempts_left"] = game.get("max_attempts", 5)
        game["round_guesses"] = []
        game["hint_used"] = False
        game["round_result"] = None
        session.modified = True
        flash(f"Skipped round. The answer was '{question.get('name')}'.", "info")

    if game.get("current_index", 0) >= len(questions):
        return redirect(url_for("results"))
    return redirect(url_for("play"))

@app.route("/reveal-question", methods=["POST"])
def reveal_question():
    """Give up on the current question and show the answer."""
    game = session.get("game")
    if not game:
        return redirect(url_for("home"))

    current_idx = game.get("current_index", 0)
    questions = get_game_questions(game)
    if current_idx < len(questions):
        question = questions[current_idx]
        game["streak"] = 0
        game["history"].append({
            "name": question.get("name"),
            "category": question.get("category"),
            "correct": False,
            "points": 0,
            "user_guess": "Given Up"
        })
        game["round_result"] = {
            "is_correct": False,
            "points_earned": 0
        }
        session.modified = True

    return redirect(url_for("play"))

@app.route("/results")
def results():
    """Final game statistics and summary."""
    game = session.get("game")
    if not game:
        return redirect(url_for("home"))

    # Automatically record match in logged-in user's personal score history
    record_match_for_user(game)

    history = game.get("history", [])
    total_q = len(get_game_questions(game))
    correct_count = sum(1 for h in history if h.get("correct"))
    accuracy = round((correct_count / total_q * 100), 1) if total_q > 0 else 0
    score = game.get("score", 0)
    rank_title = calculate_rank_title(accuracy, score)

    return render_template(
        "results.html",
        active_page="play",
        score=score,
        accuracy=accuracy,
        correct_count=correct_count,
        total_questions=total_q,
        max_streak=game.get("max_streak", 0),
        rank_title=rank_title,
        history=history,
        player_name=session.get("username") or game.get("player_name", "Player 1"),
        score_saved=game.get("score_saved", False)
    )

@app.route("/save-score", methods=["POST"])
def save_score():
    """Saves the player's score to the global leaderboard."""
    game = session.get("game")
    if not game:
        return redirect(url_for("home"))

    player_name = request.form.get("player_name", "").strip() or session.get("username") or game.get("player_name", "Player 1")
    score = game.get("score", 0)
    raw_cat = game.get("category", "movies")
    category = CATEGORY_DISPLAY_NAMES.get(raw_cat, raw_cat.replace("_", " ").title())
    game_mode = "Random" if game.get("is_random_mode") else game.get("game_mode", "classic").capitalize()
    difficulty = game.get("difficulty", "medium").capitalize()
    streak = game.get("max_streak", 0)

    entries = load_leaderboard()
    new_entry = {
        "id": len(entries) + 1,
        "player_name": player_name,
        "score": score,
        "category": category,
        "game_mode": game_mode,
        "difficulty": difficulty,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "streak": streak
    }
    entries.append(new_entry)
    entries = sorted(entries, key=lambda x: x.get("score", 0), reverse=True)
    save_leaderboard(entries)

    game["score_saved"] = True
    session.modified = True
    flash(f"🎉 Congratulations {player_name}! Your score of {score} pts is now on the Leaderboard.", "success")
    return redirect(url_for("leaderboard"))

@app.route("/leaderboard")
def leaderboard():
    """Hall of Fame page displaying top scorers."""
    entries = load_leaderboard()
    cat_filter = request.args.get("cat", "").strip()

    if cat_filter:
        filtered_entries = [e for e in entries if e.get("category", "").lower() == cat_filter.lower()]
    else:
        filtered_entries = entries

    sorted_entries = sorted(filtered_entries, key=lambda x: x.get("score", 0), reverse=True)

    return render_template(
        "leaderboard.html",
        active_page="leaderboard",
        entries=sorted_entries,
        current_cat=cat_filter
    )

@app.route("/categories")
def categories():
    """Showcase of all trivia universes."""
    return render_template("categories.html", active_page="categories")

@app.route("/rules")
def rules():
    """How to play guidelines and mechanics."""
    return render_template("rules.html", active_page="rules")

# -------------------------------------------------------------
# CLIENT API HOOKS
# -------------------------------------------------------------

@app.route("/api/movies")
def api_movies():
    """Returns catalog list for autocomplete dropdown."""
    cat = request.args.get("category", "movies")
    catalog = get_category_catalog(cat)
    return jsonify([
        {
            "name": m.get("name"),
            "year": m.get("year"),
            "director": m.get("director"),
            "actor": m.get("actor"),
            "rated": m.get("rated"),
            "genres": ", ".join(m.get("genres", [])) if isinstance(m.get("genres"), list) else str(m.get("genres", "")),
            "studio": m.get("studio")
        }
        for m in catalog
    ])

@app.route("/api/use-hint", methods=["POST"])
def api_use_hint():
    """Record that letter hint was requested."""
    game = session.get("game")
    if game:
        game["hint_used"] = True
        session.modified = True
    return jsonify({"status": "hint_enabled"})

@app.route("/api/reveal-clue", methods=["POST"])
def api_reveal_clue():
    """Record progressive clue revelation."""
    return jsonify({"status": "clue_revealed"})

# -------------------------------------------------------------
# SERVER ENTRY POINT
# -------------------------------------------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)