import json
import os

with open("data/questions.json", "r", encoding="utf-8") as f:
    existing_questions = json.load(f)

existing_ids = {q["id"] for q in existing_questions}
existing_names = {(q["category"], q["name"].lower()) for q in existing_questions}

# Enhance existing superheroes, games, and characters with 6-attribute metadata & tips
superhero_meta = {
    "Spider-Man": {"year": 1962, "director": "Marvel Comics", "actor": "Peter Parker", "rated": "Street-Level", "genres": ["Agility", "Web-Slinger"], "studio": "New York City", "icon": "🕷️"},
    "Batman": {"year": 1939, "director": "DC Comics", "actor": "Bruce Wayne", "rated": "Tech & Martial Arts", "genres": ["Detective", "Vigilante"], "studio": "Gotham City", "icon": "🦇"},
    "Iron Man": {"year": 1963, "director": "Marvel Comics", "actor": "Tony Stark", "rated": "Tech & Armor", "genres": ["Genius", "Avenger"], "studio": "Malibu / NYC", "icon": "🦾"},
    "Wonder Woman": {"year": 1941, "director": "DC Comics", "actor": "Diana Prince", "rated": "Divine Power", "genres": ["Warrior", "Justice League"], "studio": "Themyscira", "icon": "🛡️"},
    "Wolverine": {"year": 1974, "director": "Marvel Comics", "actor": "Logan", "rated": "Mutant", "genres": ["Regeneration", "X-Men"], "studio": "Canada", "icon": "爪"},
    "Captain America": {"year": 1941, "director": "Marvel Comics", "actor": "Steve Rogers", "rated": "Super-Soldier", "genres": ["Tactician", "Avenger"], "studio": "Brooklyn", "icon": "🛡️"},
    "Deadpool": {"year": 1991, "director": "Marvel Comics", "actor": "Wade Wilson", "rated": "Mutant", "genres": ["Mercenary", "Anti-Hero"], "studio": "Canada", "icon": "⚔️"},
    "Doctor Strange": {"year": 1963, "director": "Marvel Comics", "actor": "Stephen Strange", "rated": "Magic", "genres": ["Sorcerer", "Defender"], "studio": "New York City", "icon": "🔮"},
}

game_meta = {
    "Minecraft": {"year": 2011, "director": "Mojang Studios", "actor": "Steve & Alex", "rated": "Multi-Platform", "genres": ["Sandbox", "Survival"], "studio": "E10+", "icon": "⛏️"},
    "Super Mario Bros.": {"year": 1985, "director": "Nintendo", "actor": "Mario", "rated": "Nintendo", "genres": ["Platformer", "Adventure"], "studio": "E", "icon": "🍄"},
    "The Legend of Zelda": {"year": 1986, "director": "Nintendo", "actor": "Link", "rated": "Nintendo", "genres": ["Action-Adventure", "RPG"], "studio": "E10+", "icon": "🗡️"},
    "Grand Theft Auto V": {"year": 2013, "director": "Rockstar North", "actor": "Michael, Franklin & Trevor", "rated": "Multi-Platform", "genres": ["Open-World", "Action"], "studio": "M", "icon": "🚗"},
    "Pac-Man": {"year": 1980, "director": "Namco", "actor": "Pac-Man", "rated": "Arcade", "genres": ["Arcade", "Maze"], "studio": "E", "icon": "🍒"},
    "Elden Ring": {"year": 2022, "director": "FromSoftware", "actor": "The Tarnished", "rated": "Multi-Platform", "genres": ["Action RPG", "Soulslike"], "studio": "M", "icon": "💍"},
    "God of War": {"year": 2005, "director": "Santa Monica Studio", "actor": "Kratos", "rated": "PlayStation", "genres": ["Action-Adventure", "Hack & Slash"], "studio": "M", "icon": "🪓"},
    "Among Us": {"year": 2018, "director": "Innersloth", "actor": "Crewmate & Impostor", "rated": "Multi-Platform", "genres": ["Social Deduction", "Party"], "studio": "E10+", "icon": "🚀"},
}

character_meta = {
    "Sherlock Holmes": {"year": 1887, "director": "Literature", "actor": "Sherlock Universe", "rated": "Human Genius", "genres": ["Detective", "Hero"], "studio": "Arthur Conan Doyle", "icon": "🔍"},
    "Harry Potter": {"year": 1997, "director": "Literature & Film", "actor": "Wizarding World", "rated": "Wizard", "genres": ["Fantasy", "Hero"], "studio": "J.K. Rowling", "icon": "⚡"},
    "Darth Vader": {"year": 1977, "director": "Film", "actor": "Star Wars", "rated": "Cyborg Sith", "genres": ["Sci-Fi", "Villain"], "studio": "George Lucas", "icon": " 호흡"},
    "Gandalf": {"year": 1937, "director": "Literature & Film", "actor": "Middle-earth", "rated": "Maiar Wizard", "genres": ["Fantasy", "Mentor"], "studio": "J.R.R. Tolkien", "icon": "🧙"},
    "James Bond": {"year": 1953, "director": "Literature & Film", "actor": "007 Franchise", "rated": "Human Spy", "genres": ["Espionage", "Hero"], "studio": "Ian Fleming", "icon": "🍸"},
    "Katniss Everdeen": {"year": 2008, "director": "Literature & Film", "actor": "The Hunger Games", "rated": "Human Archer", "genres": ["Dystopian", "Hero"], "studio": "Suzanne Collins", "icon": "🏹"},
    "Pikachu": {"year": 1996, "director": "Games & Anime", "actor": "Pokémon", "rated": "Electric Pokémon", "genres": ["Mascot", "Companion"], "studio": "Satoshi Tajiri", "icon": "⚡"},
    "Jack Sparrow": {"year": 2003, "director": "Film", "actor": "Pirates of the Caribbean", "rated": "Human Pirate", "genres": ["Adventure", "Anti-Hero"], "studio": "Gore Verbinski", "icon": "🏴‍☠️"},
}

for q in existing_questions:
    name = q["name"]
    if q["category"] == "superheroes" and name in superhero_meta:
        m = superhero_meta[name]
        q.update({k: v for k, v in m.items() if k != "icon"})
        q["tips"] = q.get("progressive_clues", [q["normal_clue"]])
        q["poster_theme"] = {"bg1": "#0f172a", "bg2": "#1e3a8a", "accent": "#38bdf8", "icon": m["icon"], "subtitle": "Secret Identity"}
    elif q["category"] == "games" and name in game_meta:
        m = game_meta[name]
        q.update({k: v for k, v in m.items() if k != "icon"})
        q["tips"] = q.get("progressive_clues", [q["normal_clue"]])
        q["poster_theme"] = {"bg1": "#090d16", "bg2": "#14532d", "accent": "#4ade80", "icon": m["icon"], "subtitle": "Press Start"}
    elif q["category"] == "characters" and name in character_meta:
        m = character_meta[name]
        q.update({k: v for k, v in m.items() if k != "icon"})
        q["tips"] = q.get("progressive_clues", [q["normal_clue"]])
        q["poster_theme"] = {"bg1": "#1e1b4b", "bg2": "#4c1d95", "accent": "#c084fc", "icon": m["icon"], "subtitle": "Iconic Legend"}

new_questions = [
    # --- MORE MOVIES (Indie, International, Sci-Fi, Thriller, Comedy, Cult Classics) ---
    {
        "id": "movies_25", "category": "movies", "name": "Parasite",
        "aliases": ["gisaengchung", "parasite 2019"], "difficulty": "medium",
        "year": 2019, "director": "Bong Joon-ho", "actor": "Song Kang-ho", "rated": "R",
        "genres": ["Thriller", "Drama"], "studio": "CJ Entertainment",
        "poster_theme": {"bg1": "#0f172a", "bg2": "#14532d", "accent": "#4ade80", "icon": "🪨", "subtitle": "Act Like You Own The Place"},
        "tips": [
            "A struggling family living in a semi-basement apartment infiltrates a wealthy household by posing as unrelated tutors and staff.",
            "Features a scholar's rock, ram-don (Jjapaguri) noodles with steak, and a hidden subterranean bunker.",
            "First non-English language film in history to win the Academy Award for Best Picture."
        ],
        "normal_clue": "Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.",
        "progressive_clues": [
            "The Kim family folds pizza boxes in a cramped semi-basement before conning their way into the modernist Park mansion.",
            "A rainstorm floods their neighborhood while they camp out in the rich family's living room.",
            "Directed by Bong Joon-ho, winning four Oscars including Best Picture."
        ],
        "cryptic_clue": "Morse code blinks from basement stairs as counterfeit tutors feast on steak noodles above a secret bunker.",
        "letter_hint": "P _ _ _ _ _ _ _",
        "fun_fact": "The gorgeous modernist house of the wealthy Park family was not a real building—it was constructed from scratch specifically for the film!"
    },
    {
        "id": "movies_26", "category": "movies", "name": "Whiplash",
        "aliases": ["whiplash 2014"], "difficulty": "medium",
        "year": 2014, "director": "Damien Chazelle", "actor": "Miles Teller", "rated": "R",
        "genres": ["Drama", "Music"], "studio": "Sony Pictures Classics",
        "poster_theme": {"bg1": "#1c1917", "bg2": "#78350f", "accent": "#facc15", "icon": "🥁", "subtitle": "Not Quite My Tempo"},
        "tips": [
            "A first-year jazz drummer at the prestigious Shaffer Conservatory is pushed to the brink by a ruthless conductor.",
            "Famous terrifying line: 'Were you rushing or were you dragging?'",
            "J.K. Simmons won the Academy Award for Best Supporting Actor as Terence Fletcher."
        ],
        "normal_clue": "A promising young jazz drummer enrolls at a cut-throat music conservatory where his abusive instructor pushes him to madness.",
        "progressive_clues": [
            "Andrew Neiman practices until his hands bleed through band-aids into a bucket of ice water.",
            "Conductor Terence Fletcher hurls a chair and demands: 'Not quite my tempo.'",
            "Climaxes with an electrifying 9-minute drum solo to 'Caravan' at Carnegie Hall."
        ],
        "cryptic_clue": "Blood-splattered cymbals and a hurled chair measure whether a conservatory perfectionist is rushing or dragging.",
        "letter_hint": "W _ _ _ _ _ _ _",
        "fun_fact": "Damien Chazelle wrote the script based on his own anxiety-ridden experiences as a high school jazz band drummer!"
    },
    {
        "id": "movies_27", "category": "movies", "name": "Everything Everywhere All at Once",
        "aliases": ["eeaao", "everything everywhere"], "difficulty": "hard",
        "year": 2022, "director": "Daniels", "actor": "Michelle Yeoh", "rated": "R",
        "genres": ["Sci-Fi", "Comedy"], "studio": "A24",
        "poster_theme": {"bg1": "#1e1b4b", "bg2": "#be123c", "accent": "#fde047", "icon": "🥯", "subtitle": "Googly Eyes & Everything Bagel"},
        "tips": [
            "An exhausted Chinese-American laundromat owner is audited by the IRS when her husband verse-jumps from another reality.",
            "Features a nihilistic black hole made of an 'Everything Bagel', hot-dog fingers, and googly eyes.",
            "Swept the 95th Academy Awards with 7 wins including Best Picture and Best Actress for Michelle Yeoh."
        ],
        "normal_clue": "A middle-aged Chinese immigrant is swept up into an insane adventure in which she alone can save existence by exploring other universes.",
        "progressive_clues": [
            "Evelyn Wang accesses skills from alternate lifetimes during an IRS audit with Deirdre Beaubeirdre.",
            "Battles Jobu Tupaki, who has placed every hope and dream onto a spinning black Everything Bagel.",
            "Produced by A24 and starring Michelle Yeoh, Ke Huy Quan, and Stephanie Hsu."
        ],
        "cryptic_clue": "Plastic googly eyes counter a nihilistic pastry vortex while two rocks share silent captions in a canyon.",
        "letter_hint": "E _ _ _ _ _ _ _ _ _   E _ _ _ _ _ _ _ _ _   A _ _   a _   O _ _ _",
        "fun_fact": "The visual effects team consisted of just five self-taught artists working from their bedrooms using regular off-the-shelf software!"
    },
    {
        "id": "movies_28", "category": "movies", "name": "The Truman Show",
        "aliases": ["truman show", "the truman show 1998"], "difficulty": "medium",
        "year": 1998, "director": "Peter Weir", "actor": "Jim Carrey", "rated": "PG",
        "genres": ["Drama", "Sci-Fi"], "studio": "Paramount Pictures",
        "poster_theme": {"bg1": "#0c4a6e", "bg2": "#0284c7", "accent": "#fde047", "icon": "📺", "subtitle": "On The Air Since Birth"},
        "tips": [
            "An insurance salesman lives in the picturesque island town of Seahaven, unaware it is a giant television studio dome.",
            "Every neighbor, coworker, and even his wife is a paid actor broadcasting 24/7 to the world.",
            "Famous catchphrase: 'In case I don't see ya, good afternoon, good evening, and good night!'"
        ],
        "normal_clue": "An insurance salesman discovers his entire life is actually a 24/7 reality TV show broadcast to billions of viewers worldwide.",
        "progressive_clues": [
            "A studio stage light labeled 'Sirius (9 Canis Major)' suddenly falls from the blue sky onto his street.",
            "Creator Christof directs the weather and sun from a control room hidden inside the artificial moon.",
            "Jim Carrey sails a boat until its bow punctures the painted sky wall at the edge of the dome."
        ],
        "cryptic_clue": "Five thousand hidden cameras watch a caged sailor touch the painted horizon before taking a final bow at the exit door.",
        "letter_hint": "T _ _   T _ _ _ _ _   S _ _ _",
        "fun_fact": "The idyllic town of Seahaven was filmed in the real-life planned community of Seaside, Florida!"
    },
    {
        "id": "movies_29", "category": "movies", "name": "Get Out",
        "aliases": ["get out 2017"], "difficulty": "medium",
        "year": 2017, "director": "Jordan Peele", "actor": "Daniel Kaluuya", "rated": "R",
        "genres": ["Horror", "Thriller"], "studio": "Universal Pictures",
        "poster_theme": {"bg1": "#09090b", "bg2": "#1e293b", "accent": "#ef4444", "icon": "☕", "subtitle": "The Sunken Place"},
        "tips": [
            "A young Black photographer visits his white girlfriend's family estate for a weekend full of eerie microaggressions.",
            "Stirring a silver spoon inside a porcelain teacup triggers hypnosis into 'The Sunken Place'.",
            "Jordan Peele won the Oscar for Best Original Screenplay for his directorial debut."
        ],
        "normal_clue": "A young African-American visits his white girlfriend's parents for the weekend, where his simmering uneasiness about their reception reaches a boiling point.",
        "progressive_clues": [
            "Missy Armitage taps a silver spoon against a teacup, sending Chris falling into the Sunken Place.",
            "A silent bingo game at a garden party is actually an auction for the Coagula brain-transplant procedure.",
            "Chris plugs his ears with cotton stuffing torn from the armrests of a leather chair to escape hypnosis."
        ],
        "cryptic_clue": "Clinking porcelain spoons drop a photographer into a dark abyss while bingo cards auction vessels on a manicured lawn.",
        "letter_hint": "G _ _   O _ _",
        "fun_fact": "Daniel Kaluuya landed the lead role on the spot after crying a single tear at the exact beat during his first audition scene!"
    },
    {
        "id": "movies_30", "category": "movies", "name": "The Grand Budapest Hotel",
        "aliases": ["grand budapest hotel"], "difficulty": "hard",
        "year": 2014, "director": "Wes Anderson", "actor": "Ralph Fiennes", "rated": "R",
        "genres": ["Comedy", "Adventure"], "studio": "Fox Searchlight",
        "poster_theme": {"bg1": "#4c0519", "bg2": "#be185d", "accent": "#fbcfe8", "icon": "🏨", "subtitle": "Society Of The Crossed Keys"},
        "tips": [
            "Follows legendary concierge Monsieur Gustave H. and his young lobby boy Zero Moustafa.",
            "Revolves around the theft of a priceless Renaissance painting called 'Boy with Apple'.",
            "Famous for pastel pink symmetry, Mendl's pastry boxes, and director Wes Anderson's visual style."
        ],
        "normal_clue": "A writer encounters the owner of an aging high-class alpine hotel, who tells him of his early years serving as a lobby boy under an exceptional concierge.",
        "progressive_clues": [
            "Monsieur Gustave H. is framed for the murder of wealthy dowager Madame D. after inheriting 'Boy with Apple'.",
            "Prison escape tools are smuggled inside pink Mendl's Courtesan au Chocolat pastry boxes.",
            "Directed by Wes Anderson using three different aspect ratios for three historical eras."
        ],
        "cryptic_clue": "L'Air de Panache lingers in a symmetrical pink funicular as a concierge and his lobby boy flee with a stolen Renaissance canvas.",
        "letter_hint": "T _ _   G _ _ _ _   B _ _ _ _ _ _ _   H _ _ _ _",
        "fun_fact": "The hotel interior was filmed inside an abandoned, intact 1912 Art Nouveau department store in Görlitz, Germany!"
    },
    {
        "id": "movies_31", "category": "movies", "name": "No Country for Old Men",
        "aliases": ["no country for old men 2007"], "difficulty": "hard",
        "year": 2007, "director": "Coen Brothers", "actor": "Javier Bardem", "rated": "R",
        "genres": ["Crime", "Thriller"], "studio": "Miramax",
        "poster_theme": {"bg1": "#1c1917", "bg2": "#451a03", "accent": "#f59e0b", "icon": "🪙", "subtitle": "Call It, Friendo"},
        "tips": [
            "A Texas welder stumbles upon a botched desert drug deal and takes a satchel containing $2 million.",
            "Hunted by a relentless hitman with a pageboy haircut who carries a captive-bolt cattle stun gun.",
            "The killer forces a gas station proprietor to bet his life on a coin toss: 'Call it, friendo.'"
        ],
        "normal_clue": "Violence and mayhem ensue after a hunter stumbles upon a drug deal gone wrong and more than two million dollars in cash near the Rio Grande.",
        "progressive_clues": [
            "Anton Chigurh uses a pressurized air tank cattle gun to blow lock cylinders out of motel doors.",
            "Flips a 1958 quarter on a gas station counter and demands: 'What's the most you ever lost on a coin toss?'",
            "Directed by Joel and Ethan Coen, winning four Oscars including Best Picture."
        ],
        "cryptic_clue": "A tracking transponder beeps inside a leather satchel while a pneumatic hose and a lucky quarter decide fates across West Texas.",
        "letter_hint": "N _   C _ _ _ _ _ _   f _ _   O _ _   M _ _",
        "fun_fact": "There is almost no musical score in the entire two-hour film—the Coen Brothers used only ambient desert wind and silence to build tension!"
    },
    {
        "id": "movies_32", "category": "movies", "name": "Knives Out",
        "aliases": ["knives out 2019"], "difficulty": "medium",
        "year": 2019, "director": "Rian Johnson", "actor": "Daniel Craig", "rated": "PG-13",
        "genres": ["Crime", "Comedy"], "studio": "Lionsgate",
        "poster_theme": {"bg1": "#1e1b4b", "bg2": "#78350f", "accent": "#fbbf24", "icon": "🗡️", "subtitle": "A Donut Hole In A Donut's Hole"},
        "tips": [
            "Southern gentleman detective Benoit Blanc investigates the death of wealthy mystery novelist Harlan Thrombey.",
            "The nurse Marta physically cannot tell a lie without immediately vomiting.",
            "Features a massive circular throne surrounded by dozens of ornamental daggers and a 'My House, My Rules' coffee mug."
        ],
        "normal_clue": "A detective investigates the death of the patriarch of an eccentric, combative family after his 85th birthday party.",
        "progressive_clues": [
            "Harlan Thrombey leaves his entire fortune and publishing empire to his kind nurse, Marta Cabrera.",
            "Private detective Benoit Blanc compares the case to 'a donut hole in the center of a donut's hole.'",
            "Starring Daniel Craig, Ana de Armas, and Chris Evans in a cozy cable-knit sweater."
        ],
        "cryptic_clue": "A ring of decorative blades frames a seat where a stage prop blade fails to pierce and a coffee mug declares ownership.",
        "letter_hint": "K _ _ _ _ _   O _ _",
        "fun_fact": "Apple allows villains to use iPhones in movies? No! Rian Johnson revealed that film studios aren't allowed to let bad guys use iPhones on camera, which was a subtle clue!"
    },

    # --- MORE ANIME (Varied Genres: Mecha, Psychological, Fantasy, Comedy, Sports) ---
    {
        "id": "anime_17", "category": "anime", "name": "Neon Genesis Evangelion",
        "aliases": ["evangelion", "nge", "shinji ikari"], "difficulty": "hard",
        "year": 1995, "director": "Hideaki Anno", "actor": "Shinji Ikari", "rated": "TV-14",
        "genres": ["Sci-Fi", "Psychological"], "studio": "Gainax",
        "poster_theme": {"bg1": "#1e1b4b", "bg2": "#4c1d95", "accent": "#4ade80", "icon": "🤖", "subtitle": "Get In The Robot, Shinji"},
        "tips": [
            "Teenagers are recruited by the paramilitary agency NERV to pilot bio-mechanical giants called EVAs against 'Angels'.",
            "Set in the retractable fortress city of Tokyo-3 fifteen years after the cataclysmic Second Impact.",
            "Famous opening theme song: 'A Cruel Angel's Thesis'."
        ],
        "normal_clue": "A reluctant 14-year-old boy is summoned by his estranged father to Tokyo-3 to pilot a giant bio-machine against monstrous beings called Angels.",
        "progressive_clues": [
            "Shinji Ikari pilots the purple-and-green Unit-01 alongside Rei Ayanami and Asuka Langley Soryu.",
            "EVAs rely on an umbilical power cable providing only 5 minutes of internal battery backup.",
            "Explores deep psychological trauma and the mysterious Human Instrumentality Project."
        ],
        "cryptic_clue": "Severed umbilical cables leave three hundred seconds for a purple bio-titan to breach an Angel's AT Field.",
        "letter_hint": "N _ _ _   G _ _ _ _ _ _   E _ _ _ _ _ _ _ _ _",
        "fun_fact": "The monstrous Angels and religious symbolism were added primarily because director Hideaki Anno thought they looked cool and mysterious!"
    },
    {
        "id": "anime_18", "category": "anime", "name": "Frieren: Beyond Journey's End",
        "aliases": ["frieren", "sousou no frieren"], "difficulty": "medium",
        "year": 2023, "director": "Kanehito Yamada", "actor": "Frieren", "rated": "TV-14",
        "genres": ["Fantasy", "Adventure"], "studio": "Madhouse",
        "poster_theme": {"bg1": "#0c4a6e", "bg2": "#1e3a8a", "accent": "#f8fafc", "icon": "🪄", "subtitle": "After The Demon King Falls"},
        "tips": [
            "Begins *after* the Hero Party has already defeated the Demon King following a 10-year quest.",
            "An immortal elven mage realizes how brief human lifespans are after Hero Himmel passes away of old age.",
            "She collects silly folk grimoires (like a spell to make sweet grapes sour) and constantly gets stuck inside Mimic chests!"
        ],
        "normal_clue": "An elven mage who helped defeat the Demon King embarks on a new journey decades later to understand humanity and fulfill her late comrades' wishes.",
        "progressive_clues": [
            "Outlives her former party members Himmel the Hero and Heiter the Priest due to her thousand-year elven lifespan.",
            "Mentors young human mage Fern and timid warrior Stark while traveling north toward Aureole.",
            "Known as 'Frieren the Slayer' among demons for concealing her vast mana for over a millennium."
        ],
        "cryptic_clue": "Blue-moon weed blooms beside an aging hero's statue as an immortal twin-tailed elf retraces a ten-year quest.",
        "letter_hint": "F _ _ _ _ _ _ :   B _ _ _ _ _   J _ _ _ _ _ _ ' s   E _ _",
        "fun_fact": "Every character and town name in Frieren is actually a German word describing their personality—'Frieren' means 'to freeze', 'Stark' means 'strong', and 'Himmel' means 'heaven'!"
    },
    {
        "id": "anime_19", "category": "anime", "name": "Spy x Family",
        "aliases": ["spy family", "anya forger", "loid forger"], "difficulty": "easy",
        "year": 2022, "director": "Tatsuya Endo", "actor": "Loid Forger", "rated": "TV-14",
        "genres": ["Action", "Comedy"], "studio": "WIT Studio",
        "poster_theme": {"bg1": "#064e3b", "bg2": "#115e59", "accent": "#f43f5e", "icon": "🥜", "subtitle": "Operation Strix"},
        "tips": [
            "Master spy 'Twilight' builds a fake family to infiltrate an elite school, unaware his wife is an assassin and his daughter is a telepath.",
            "Pink-haired Anya loves peanuts, spy cartoons, and making her iconic smug 'Heh' face.",
            "Even their family dog Bond has the secret power to see into the future!"
        ],
        "normal_clue": "A master spy must build a fake family to execute a peace mission, not realizing the girl he adopts is a telepath and the woman he marries is a lethal assassin.",
        "progressive_clues": [
            "Agent Twilight assumes the identity of psychiatrist Loid Forger for Operation Strix in Ostania.",
            "Young Anya must earn 8 Stella Stars at Eden Academy while avoiding Tonitrus Bolts.",
            "Yor Forger works as a polite city hall clerk by day and the assassin 'Thorn Princess' by night."
        ],
        "cryptic_clue": "A telepathic peanut lover keeps the secrets of a disguised intelligence agent and a stiletto-wielding bride under one roof.",
        "letter_hint": "S _ _   x   F _ _ _ _ _",
        "fun_fact": "The stylish chairs shown on the manga covers are all real-world iconic mid-century designer chairs!"
    },
    {
        "id": "anime_20", "category": "anime", "name": "Mob Psycho 100",
        "aliases": ["mob psycho", "shigeo kageyama", "reigen arataka"], "difficulty": "medium",
        "year": 2016, "director": "ONE", "actor": "Shigeo Kageyama", "rated": "TV-14",
        "genres": ["Action", "Comedy"], "studio": "Bones",
        "poster_theme": {"bg1": "#090d16", "bg2": "#3b0764", "accent": "#ec4899", "icon": "💥", "subtitle": "99% ... 100% Explosion"},
        "tips": [
            "A bowl-cut middle schooler with godlike psychic powers works part-time for a con-artist spirit medium named Reigen.",
            "Whenever his suppressed emotional gauge reaches '100%', his psychic aura explodes.",
            "Instead of using his psychic gifts for popularity, he joins the school's wholesome Body Improvement Club!"
        ],
        "normal_clue": "A psychic middle school boy tries to live a normal life and keep his growing powers under control, even though an on-screen counter tracks his emotional limit toward 100%.",
        "progressive_clues": [
            "Created by ONE (the author of One Punch Man) and animated by Studio Bones.",
            "Works for 300 yen an hour under self-proclaimed 'Greatest Psychic of the 21st Century' Arataka Reigen.",
            "Accompanied by the floating green upper-class evil spirit Dimple."
        ],
        "cryptic_clue": "A bowl-cut esper lifts dumbbells with muscular wholesome upperclassmen while a percentage ticker climbs toward telekinetic eruption.",
        "letter_hint": "M _ _   P _ _ _ _ _   1 0 0",
        "fun_fact": "All the anime opening sequences incorporate hundreds of frames of hand-painted oil-on-glass animation!"
    },
    {
        "id": "anime_21", "category": "anime", "name": "Monster",
        "aliases": ["naoki urasawa monster", "dr tenma", "johan liebert"], "difficulty": "insane",
        "year": 2004, "director": "Naoki Urasawa", "actor": "Kenzo Tenma", "rated": "TV-MA",
        "genres": ["Thriller", "Drama"], "studio": "Madhouse",
        "poster_theme": {"bg1": "#09090b", "bg2": "#1e293b", "accent": "#dc2626", "icon": "🩺", "subtitle": "The Nameless Monster"},
        "tips": [
            "A brilliant Japanese neurosurgeon in Germany defies hospital politics to save a young boy shot in the head instead of the town mayor.",
            "Nine years later, he learns the boy he saved—Johan Liebert—has grown into a charismatic, nihilistic serial killer.",
            "Set across post-Cold War Germany and Czechia following the fall of the Berlin Wall."
        ],
        "normal_clue": "A brilliant neurosurgeon in Germany sacrifices his career to save a young boy's life, only to discover years later that the child grew into a sociopathic mastermind.",
        "progressive_clues": [
            "Dr. Kenzo Tenma is hunted by obsessive BKA Inspector Lunge across Düsseldorf, Munich, and Prague.",
            "Revolves around the mysterious Kinderheim 511 orphanage and a Czech picture book about 'The Nameless Monster'.",
            "Written by master mangaka Naoki Urasawa and adapted across 74 episodes by Madhouse."
        ],
        "cryptic_clue": "A scalpel spares a twin boy's bullet-pierced skull in Düsseldorf, unleashing a soft-spoken blond nihilist who leaves no trace.",
        "letter_hint": "M _ _ _ _ _ _",
        "fun_fact": "Every single European street, bridge, and hospital in Monster was meticulously drawn from real-world architectural photographs of Germany and Prague!"
    },
    {
        "id": "anime_22", "category": "anime", "name": "Haikyu!!",
        "aliases": ["haikyuu", "shoyo hinata", "kageyama"], "difficulty": "medium",
        "year": 2014, "director": "Haruichi Furudate", "actor": "Shoyo Hinata", "rated": "TV-14",
        "genres": ["Sports", "Shonen"], "studio": "Production I.G",
        "poster_theme": {"bg1": "#1c1917", "bg2": "#ea580c", "accent": "#facc15", "icon": "🏐", "subtitle": "Fly High, Karasuno!"},
        "tips": [
            "A short, orange-haired boy with an incredible vertical jump joins Karasuno High School's volleyball team.",
            "Forced to team up with his former middle-school rival, the genius setter Tobio Kageyama.",
            "Together they perfect the unstoppable 'Freak Quick' attack with Hinata spiking with his eyes closed!"
        ],
        "normal_clue": "Determined to be like the volleyball championship's star player nicknamed 'the Little Giant', a short boy joins his school's flightless crows volleyball club.",
        "progressive_clues": [
            "Shoyo Hinata and 'King of the Court' setter Tobio Kageyama turn Karasuno High back into national contenders.",
            "Features intense rallies against rival schools Aoba Johsai (Oikawa), Nekoma (Kenma), and Shiratorizawa (Ushijima).",
            "Karasuno's black jerseys earn them the nickname 'The Flightless Crows' until they learn to fly again."
        ],
        "cryptic_clue": "Clipped black crows soar over a white net when a pint-sized decoy trusts a tyrant setter's pinpoint toss.",
        "letter_hint": "H _ _ _ _ _ ! !",
        "fun_fact": "Sales of real-life Mikasa volleyballs and high school volleyball club enrollments in Japan surged dramatically after the anime premiered!"
    },
    {
        "id": "anime_23", "category": "anime", "name": "Vinland Saga",
        "aliases": ["thorfinn", "askeladd"], "difficulty": "hard",
        "year": 2019, "director": "Makoto Yukimura", "actor": "Thorfinn", "rated": "TV-MA",
        "genres": ["Action", "Drama"], "studio": "WIT Studio",
        "poster_theme": {"bg1": "#0f172a", "bg2": "#7f1d1d", "accent": "#fbbf24", "icon": "⛵", "subtitle": "You Have No Enemies"},
        "tips": [
            "Set in 11th-century Viking-era England and Iceland, following young Thorfinn's quest for vengeance against Askeladd.",
            "Remembering his father Thors's wisdom: 'A true warrior doesn't need a sword. You have no enemies.'",
            "Dual-wields two short daggers before seeking a peaceful land across the western ocean."
        ],
        "normal_clue": "Young Thorfinn grows up serving in the mercenary band of his father's killer, Askeladd, seeking an honorable duel for revenge amidst the Viking invasion of England.",
        "progressive_clues": [
            "Son of Thors, the legendary 'Troll of Jom' who abandoned war for a quiet life in Iceland.",
            "Serves King Canute and battles the giant axe-wielding warrior Thorkell the Tall.",
            "Later journeys from slavery on Ketil's farm to seek a war-free paradise in North America."
        ],
        "cryptic_clue": "Twin daggers chase a cunning Welsh-blooded mercenary's neck until a broken slave learns that no man has an enemy.",
        "letter_hint": "V _ _ _ _ _ _   S _ _ _",
        "fun_fact": "Thorfinn Karlsefni, Leif Erikson, Canute the Great, and Thorkell the Tall were all real historical 11th-century figures!"
    },
    {
        "id": "anime_24", "category": "anime", "name": "Chainsaw Man",
        "aliases": ["csm", "denji", "pochita", "makima"], "difficulty": "medium",
        "year": 2022, "director": "Tatsuki Fujimoto", "actor": "Denji", "rated": "TV-MA",
        "genres": ["Action", "Dark Fantasy"], "studio": "MAPPA",
        "poster_theme": {"bg1": "#1c1917", "bg2": "#991b1b", "accent": "#f97316", "icon": "🪚", "subtitle": "Pull The Starter Cord"},
        "tips": [
            "An impoverished teenager merges with his pet devil-dog Pochita, gaining a starter cord in his chest.",
            "Pulling the cord on his sternum sprouts roaring chainsaws from his head and both arms.",
            "Recruited into Public Safety Devil Hunters by the mysterious Makima alongside Aki and Power."
        ],
        "normal_clue": "Following a betrayal, a young man left for dead is reborn as a powerful devil-human hybrid after merging with his pet devil Pochita.",
        "progressive_clues": [
            "Denji's biggest life dream at the start is simply to eat bread with jam on it.",
            "Paired up in Tokyo Public Safety Division 4 with the Blood Fiend Power and sword-wielder Aki Hayakawa.",
            "Features a completely different ending theme song and animation style for every single episode!"
        ],
        "cryptic_clue": "A ripcord rooted in a starving boy's sternum revs roaring steel teeth from his skull and forearms.",
        "letter_hint": "C _ _ _ _ _ _ _   M _ _",
        "fun_fact": "The iconic opening sequence by MAPPA pays shot-for-shot homage to over a dozen classic Hollywood movies including Pulp Fiction, Fight Club, and The Big Lebowski!"
    },

    # --- MORE COMMON OBJECTS (With distinct silhouettes in app.py) ---
    {
        "id": "objects_17", "category": "common_objects", "name": "Magnifying Glass",
        "aliases": ["magnifier", "hand lens", "loupe"], "difficulty": "easy",
        "year": 1250, "director": "Office & Desk", "actor": "Glass & Metal", "rated": "Manual",
        "genres": ["Optics", "Science"], "studio": "Handheld", "silhouette_type": "magnifying_glass",
        "tips": [
            "A circular convex glass lens mounted in a metal rim with a straight handheld grip.",
            "Makes tiny print, stamps, or fingerprints appear much larger when held over a page.",
            "The signature tool of detectives like Sherlock Holmes and also the universal 'Search' icon!"
        ],
        "normal_clue": "A convex lens mounted in a circular frame with a handle, used to make small text or objects appear larger.",
        "progressive_clues": [
            "Hint 1: Consists of a round metal rim holding a curved glass lens attached to a handle.",
            "Hint 2: Used by detectives to inspect clues and by readers to see tiny fine print.",
            "Hint 3: Its silhouette is used on almost every website and phone as the 'Search' icon!"
        ],
        "cryptic_clue": "A single crystal eye on a stick that swells tiny letters into giants and focuses sunbeams into smoke.",
        "letter_hint": "M _ _ _ _ _ _ _ _ _   G _ _ _ _",
        "fun_fact": "Franciscan friar Roger Bacon described the scientific properties of the magnifying glass in England in 1268!"
    },
    {
        "id": "objects_18", "category": "common_objects", "name": "Padlock",
        "aliases": ["lock", "combination lock", "master lock"], "difficulty": "medium",
        "year": 1857, "director": "Everyday Carry", "actor": "Brass & Steel", "rated": "Manual",
        "genres": ["Security", "Hardware"], "studio": "Pocket-Sized", "silhouette_type": "padlock",
        "tips": [
            "Has a solid rectangular or rounded brass body topped with a U-shaped metal loop ('shackle').",
            "Secures gym lockers, bicycles, gates, and treasure chests until opened with a key or dial code.",
            "Its silhouette appears in your web browser's address bar to show a secure HTTPS website!"
        ],
        "normal_clue": "A detachable lock with a U-shaped metal shackle that loops through a staple or chain and clicks shut.",
        "progressive_clues": [
            "Hint 1: Features a curved U-shaped steel loop on top of a heavy brass or steel block.",
            "Hint 2: Used every day on school gym lockers, garden sheds, and bike chains.",
            "Hint 3: Appears next to website URLs in your browser to indicate a secure connection!"
        ],
        "cryptic_clue": "A brass block with a steel horseshoe collar that bites shut on chains until a notched key or three-number spin sets it free.",
        "letter_hint": "P _ _ _ _ _ _",
        "fun_fact": "Couples around the world attach 'love padlocks' to bridge railings and throw the key into the river below as a symbol of unbreakable love!"
    },
    {
        "id": "objects_19", "category": "common_objects", "name": "Teapot",
        "aliases": ["tea kettle", "kettle", "pot"], "difficulty": "easy",
        "year": 1500, "director": "Kitchen", "actor": "Ceramic", "rated": "Manual",
        "genres": ["Drinkware", "Kitchen"], "studio": "Handheld", "silhouette_type": "teapot",
        "tips": [
            "Has a rounded belly, a removable top lid, a C-shaped handle on one side, and a curved pouring spout on the other.",
            "Immortalized in a classic nursery rhyme: 'Here is my handle, here is my spout!'",
            "Used for steeping loose-leaf tea or herbs in boiling hot water."
        ],
        "normal_clue": "A round vessel with a lid, a curved pouring spout, and a side handle, used for brewing and pouring tea.",
        "progressive_clues": [
            "Hint 1: Short and stout with a handle on one side and a curved S-shaped spout on the other.",
            "Hint 2: Filled with boiling water and tea leaves for afternoon tea.",
            "Hint 3: A famous children's song tells you to 'tip me over and pour me out!'"
        ],
        "cryptic_clue": "Short and stout with one arm on its hip and the other curved to pour steaming amber leaves into porcelain cups.",
        "letter_hint": "T _ _ _ _ _",
        "fun_fact": "In 3D computer graphics, the 'Utah Teapot' (modeled in 1975) is the most famous standard test object in computer history!"
    },
    {
        "id": "objects_20", "category": "common_objects", "name": "Microphone",
        "aliases": ["mic", "studio microphone", "vocal mic"], "difficulty": "medium",
        "year": 1876, "director": "Music & Stage", "actor": "Steel & Mesh", "rated": "Electric",
        "genres": ["Audio", "Music"], "studio": "Handheld", "silhouette_type": "microphone",
        "tips": [
            "A tapered cylindrical grip topped with a spherical wire-mesh grille dome.",
            "Converts the sound waves of your voice into an electrical signal for speakers or recording.",
            "Singers, comedians, and podcasters speak into it—and 'drop' it after making a bold final point!"
        ],
        "normal_clue": "An acoustic-to-electric device with a wire mesh head that amplifies or records a speaker's or singer's voice.",
        "progressive_clues": [
            "Hint 1: Topped with a silver wire-mesh ball attached to a tapered black handle.",
            "Hint 2: Held by lead singers on stage, stand-up comedians, and karaoke fans.",
            "Hint 3: People often tap it and say 'Testing, testing, 1, 2, 3' to check if it's on!"
        ],
        "cryptic_clue": "A silver wire-mesh sphere atop a black wand that turns a whisper into a stadium roar.",
        "letter_hint": "M _ _ _ _ _ _ _ _ _",
        "fun_fact": "The expression 'mic drop' became popular in the 1980s when comedians like Eddie Murphy and rappers dropped their microphones to signal a performance too good to top!"
    },
    {
        "id": "objects_21", "category": "common_objects", "name": "Trophy",
        "aliases": ["cup", "championship trophy", "award cup"], "difficulty": "easy",
        "year": 1700, "director": "Home & Ceiling", "actor": "Gold & Marble", "rated": "Manual",
        "genres": ["Sports", "Household"], "studio": "Medium", "silhouette_type": "trophy",
        "tips": [
            "A shiny golden two-handled chalice cup mounted atop a square dark pedestal base.",
            "Awarded to the 1st-place champion of a tournament, race, or championship.",
            "Displayed proudly on a shelf or held high over the winner's head while confetti falls!"
        ],
        "normal_clue": "A decorative golden cup with two curved handles mounted on a pedestal base, awarded as a prize for first-place victory.",
        "progressive_clues": [
            "Hint 1: Has two symmetrical ear-like handles flanking a gleaming gold cup on a dark base.",
            "Hint 2: Engraved with the winner's name and lifted overhead after winning a championship.",
            "Hint 3: Also the icon used for achievements and leaderboards in video games!"
        ],
        "cryptic_clue": "A gleaming two-eared golden chalice hoisted skyward in a storm of confetti by the last contender standing.",
        "letter_hint": "T _ _ _ _ _",
        "fun_fact": "The Stanley Cup (awarded in NHL hockey since 1893) is the oldest existing trophy competed for by professional athletes in North America!"
    },
    {
        "id": "objects_22", "category": "common_objects", "name": "Anchor",
        "aliases": ["ship anchor", "boat anchor"], "difficulty": "medium",
        "year": 1600, "director": "Outdoor", "actor": "Forged Iron", "rated": "Manual",
        "genres": ["Outdoor", "Transport"], "studio": "Large", "silhouette_type": "anchor",
        "tips": [
            "A heavy forged-iron nautical device with a central shank, a top ring, a crossbar stock, and two curved pointed flukes at the bottom.",
            "Dropped overboard on a heavy chain to hook into the seabed and keep a ship from drifting away.",
            "A classic sailor tattoo and the universal symbol of stability and naval tradition."
        ],
        "normal_clue": "A heavy metal device with two curved barbed arms attached to a chain and dropped to the sea bottom to hold a ship in place.",
        "progressive_clues": [
            "Hint 1: Shaped like a cross at the top with a wide smiling crescent and two pointed arrowheads at the bottom.",
            "Hint 2: Connected to a ship by a heavy iron chain and dropped into the ocean with a splash.",
            "Hint 3: Found on captain hats, sailor tattoos (like Popeye's forearms!), and yacht club flags."
        ],
        "cryptic_clue": "Twin iron hooks lowered into the abyss to tether floating timber against the pull of ocean tides.",
        "letter_hint": "A _ _ _ _ _",
        "fun_fact": "Large modern cruise ship anchors can weigh over 15 tons each—about as heavy as three adult elephants!"
    },
    {
        "id": "objects_23", "category": "common_objects", "name": "Crown",
        "aliases": ["royal crown", "king crown", "tiara"], "difficulty": "easy",
        "year": 1200, "director": "Everyday Carry", "actor": "Gold & Jewels", "rated": "Manual",
        "genres": ["Accessory", "Classic"], "studio": "Wearable", "silhouette_type": "crown",
        "tips": [
            "A circular golden headband topped with pointed peaks and studded with rubies, emeralds, and pearls.",
            "Worn on the head of a king, queen, or emperor as the ultimate symbol of royal sovereignty.",
            "Placed upon a monarch's head during a formal coronation ceremony."
        ],
        "normal_clue": "An ornate circular headdress made of gold and precious jewels worn by a king or queen as a symbol of royalty.",
        "progressive_clues": [
            "Hint 1: Has a distinctive zigzag silhouette of golden points topped with small spheres or crosses.",
            "Hint 2: Encrusted with sparkling diamonds, rubies, and velvet lining.",
            "Hint 3: Worn by kings, queens, and chess pieces at the top of the royal hierarchy."
        ],
        "cryptic_clue": "A jagged ring of gold and rubies resting heavy upon a monarch's brow.",
        "letter_hint": "C _ _ _ _",
        "fun_fact": "St Edward's Crown, used at British coronations since 1661, is made of solid 22-karat gold and weighs nearly 5 pounds (2.23 kg)!"
    },
    {
        "id": "objects_24", "category": "common_objects", "name": "Frying Pan",
        "aliases": ["skillet", "pan", "cast iron skillet"], "difficulty": "easy",
        "year": 1800, "director": "Kitchen", "actor": "Cast Iron", "rated": "Manual",
        "genres": ["Cooking", "Kitchen"], "studio": "Handheld", "silhouette_type": "frying_pan",
        "tips": [
            "A flat-bottomed circular metal pan with low flared sides and a single long straight handle.",
            "Used on a kitchen stove burner to sizzle eggs, bacon, pancakes, and stir-fry.",
            "Often coated with black non-stick Teflon or seasoned heavy cast iron."
        ],
        "normal_clue": "A flat-bottomed circular metal pan with low sides and a long straight handle, used for searing and frying food on a stovetop.",
        "progressive_clues": [
            "Hint 1: Looks like a wide flat circle with a long handle sticking out of one side.",
            "Hint 2: Sits on a gas or electric stove burner sizzling butter, sunny-side-up eggs, and pancakes.",
            "Hint 3: Also Rapunzel's favorite improvised weapon in Disney's Tangled and a bulletproof shield in PUBG!"
        ],
        "cryptic_clue": "A long-handled iron disc that sizzles morning eggs over blue kitchen flames.",
        "letter_hint": "F _ _ _ _ _   P _ _",
        "fun_fact": "Well-seasoned cast iron skillets can last over 100 years and are often passed down as family heirlooms across generations!"
    }
]

for nq in new_questions:
    if nq["id"] not in existing_ids and (nq["category"], nq["name"].lower()) not in existing_names:
        existing_questions.append(nq)

with open("data/questions.json", "w", encoding="utf-8") as f:
    json.dump(existing_questions, f, indent=2)

print(f"Updated data/questions.json with {len(existing_questions)} total questions!")
