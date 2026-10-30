import json

questions = [
    # =========================================================================
    # 🎌 ANIME CATEGORY (16 Iconic Anime Series with 6-Attribute Metadata)
    # =========================================================================
    {
        "id": "anime_01",
        "category": "anime",
        "name": "Dragon Ball Z",
        "aliases": ["dragon ball", "dbz", "goku", "son goku"],
        "difficulty": "easy",
        "year": 1989,
        "director": "Akira Toriyama",
        "actor": "Son Goku",
        "rated": "TV-PG",
        "genres": ["Action", "Shonen"],
        "studio": "Toei Animation",
        "poster_theme": {
            "bg1": "#431407",
            "bg2": "#ea580c",
            "accent": "#facc15",
            "icon": "🐉",
            "subtitle": "Seven Wish Orbs"
        },
        "tips": [
            "Follows a Saiyan warrior raised on Earth who unleashes the signature Kamehameha wave.",
            "Collecting all seven orange crystalline spheres summons the eternal dragon Shenron.",
            "Features iconic transformations including Super Saiyan on Planet Namek."
        ],
        "normal_clue": "A Saiyan warrior raised on Earth defends the planet against intergalactic tyrants while searching for seven wish-granting orbs.",
        "progressive_clues": [
            "Sent to Earth in a pod as an infant, this warrior loves martial arts and eating massive feasts.",
            "He wielded the Flying Nimbus and Power Pole before discovering his golden Super Saiyan form.",
            "Main protagonist is Son Goku, father of Gohan and Goten, facing Frieza, Cell, and Majin Buu."
        ],
        "cryptic_clue": "An orange gi holds an alien tail-less monkey god whose scream shakes galaxies and turns black hair into golden fire.",
        "letter_hint": "D _ _ _ _ _   B _ _ _   Z",
        "fun_fact": "Goku's Japanese voice actress, Masako Nozawa, voiced Goku, Gohan, and Goten across the entire franchise!"
    },
    {
        "id": "anime_02",
        "category": "anime",
        "name": "Naruto",
        "aliases": ["naruto uzumaki", "naruto shippuden"],
        "difficulty": "easy",
        "year": 2002,
        "director": "Masashi Kishimoto",
        "actor": "Naruto Uzumaki",
        "rated": "TV-PG",
        "genres": ["Action", "Shonen"],
        "studio": "Studio Pierrot",
        "poster_theme": {
            "bg1": "#1c1917",
            "bg2": "#ea580c",
            "accent": "#38bdf8",
            "icon": "🍥",
            "subtitle": "Way Of The Ninja"
        },
        "tips": [
            "An orange-clad ninja of the Hidden Leaf Village dreams of becoming the Hokage.",
            "Houses the powerful Nine-Tailed Fox spirit (Kurama) sealed inside him at birth.",
            "Masters the Shadow Clone Jutsu and the spiraling Rasengan sphere."
        ],
        "normal_clue": "An orange-clad ninja of the Hidden Leaf who dreams of becoming Hokage and houses the Nine-Tailed Fox.",
        "progressive_clues": [
            "Ostracized by his village since childhood, he loves miso ramen at Ichiraku.",
            "Master of the Shadow Clone Technique and the spiraling Rasengan sphere.",
            "Trains under Jiraiya and Kakashi in Team 7 alongside Sasuke Uchiha and Sakura Haruno."
        ],
        "cryptic_clue": "A whisker-cheeked boy sealed with an orange beast, sworn to bring back his rogue rival.",
        "letter_hint": "N _ _ _ _ _",
        "fun_fact": "Ichiraku Ramen was inspired by a real-world ramen shop near Kyushu Sangyo University where creator Masashi Kishimoto ate in college!"
    },
    {
        "id": "anime_03",
        "category": "anime",
        "name": "One Piece",
        "aliases": ["monkey d luffy", "luffy", "straw hat pirates"],
        "difficulty": "easy",
        "year": 1999,
        "director": "Eiichiro Oda",
        "actor": "Monkey D. Luffy",
        "rated": "TV-14",
        "genres": ["Adventure", "Shonen"],
        "studio": "Toei Animation",
        "poster_theme": {
            "bg1": "#0c2d57",
            "bg2": "#dc2626",
            "accent": "#fde047",
            "icon": "👒",
            "subtitle": "Grand Line Pirates"
        },
        "tips": [
            "A stretchy pirate captain wearing a straw hat sails the Grand Line to become King of the Pirates.",
            "Eating a Devil Fruit grants supernatural powers but permanently robs the user of the ability to swim.",
            "Features a three-sword-style swordsman named Roronoa Zoro and the ships Going Merry & Thousand Sunny."
        ],
        "normal_clue": "A rubber pirate captain wearing a straw hat sails the Grand Line with his crew to find the ultimate treasure.",
        "progressive_clues": [
            "Ate the Gum-Gum Fruit as a boy, giving him a rubber body at the cost of never swimming again.",
            "Captains the Straw Hat Pirates alongside Zoro, Nami, Usopp, Sanji, and Chopper.",
            "Over 1,100 episodes chronicling the voyage toward the final island, Laugh Tale."
        ],
        "cryptic_clue": "Stretchy captain wearing Shanks's woven crown, immune to lightning but doomed to sink in brine.",
        "letter_hint": "O _ _   P _ _ _ _",
        "fun_fact": "Eiichiro Oda originally planned One Piece to last only five years when it began serialization in 1997!"
    },
    {
        "id": "anime_04",
        "category": "anime",
        "name": "Attack on Titan",
        "aliases": ["shingeki no kyojin", "aot", "eren yeager", "levi ackerman"],
        "difficulty": "easy",
        "year": 2013,
        "director": "Hajime Isayama",
        "actor": "Eren Yeager",
        "rated": "TV-MA",
        "genres": ["Action", "Dark Fantasy"],
        "studio": "WIT Studio",
        "poster_theme": {
            "bg1": "#1c1917",
            "bg2": "#451a03",
            "accent": "#ef4444",
            "icon": "⚔️",
            "subtitle": "Beyond The Three Walls"
        },
        "tips": [
            "Humanity lives inside three concentric walls (Maria, Rose, Sina) to hide from man-eating giants.",
            "Soldiers use Omni-Directional Mobility (ODM) gas-grappling gear to slice the nape of giants' necks.",
            "Follows Eren Yeager, Mikasa Ackerman, Armin Arlert, and Captain Levi of the Survey Corps."
        ],
        "normal_clue": "Humanity fights for survival inside three giant concentric walls against towering man-eating humanoids.",
        "progressive_clues": [
            "The Colossal and Armored giants breach Wall Maria in the Shiganshina District.",
            "Scout Regiment soldiers soar through the air using gas-powered grappling hooks and twin steel blades.",
            "Eren Yeager discovers the power to transform into a giant himself and uncover the basement's truth."
        ],
        "cryptic_clue": "Grappling wires hiss behind concentric stone rings as humanity slices the napes of smiling giants.",
        "letter_hint": "A _ _ _ _ _   o _   T _ _ _ _",
        "fun_fact": "The fortified city of Nördlingen in Germany, built inside a massive meteor crater, inspired the walled cities!"
    },
    {
        "id": "anime_05",
        "category": "anime",
        "name": "Death Note",
        "aliases": ["the death note", "light yagami", "kira"],
        "difficulty": "easy",
        "year": 2006,
        "director": "Tsugumi Ohba",
        "actor": "Light Yagami",
        "rated": "TV-14",
        "genres": ["Thriller", "Supernatural"],
        "studio": "Madhouse",
        "poster_theme": {
            "bg1": "#09090b",
            "bg2": "#27272a",
            "accent": "#dc2626",
            "icon": "📓",
            "subtitle": "Forty Seconds To Die"
        },
        "tips": [
            "A bored Shinigami (God of Death) named Ryuk drops a supernatural black notebook into the human world.",
            "Anyone whose name is written inside the notebook dies of a heart attack within 40 seconds.",
            "Features a tense cat-and-mouse battle of wits between genius student Light Yagami ('Kira') and detective L."
        ],
        "normal_clue": "A supernatural black notebook dropped by a Shinigami kills anyone whose name is written in its pages.",
        "progressive_clues": [
            "Requires the writer to know the victim's name and picture their face while writing.",
            "Dropped by apple-loving Shinigami Ryuk and picked up by top high school student Light Yagami.",
            "World-famous barefoot detective 'L' leads the task force hunting the vigilante killer 'Kira'."
        ],
        "cryptic_clue": "Forty seconds for cardiac arrest when ink stains obsidian parchment dropped by an apple-eating specter.",
        "letter_hint": "D _ _ _ _   N _ _ _",
        "fun_fact": "In the original pilot manga chapter, there was a 'Death Eraser' that could bring people back to life if their name was rubbed out!"
    },
    {
        "id": "anime_06",
        "category": "anime",
        "name": "Fullmetal Alchemist: Brotherhood",
        "aliases": ["fullmetal alchemist", "fma", "fmab", "edward elric"],
        "difficulty": "medium",
        "year": 2009,
        "director": "Hiromu Arakawa",
        "actor": "Edward Elric",
        "rated": "TV-14",
        "genres": ["Adventure", "Fantasy"],
        "studio": "Bones",
        "poster_theme": {
            "bg1": "#2a0808",
            "bg2": "#7f1d1d",
            "accent": "#fbbf24",
            "icon": "⚙️",
            "subtitle": "Law Of Equivalent Exchange"
        },
        "tips": [
            "Two brothers lose their bodies attempting forbidden human transmutation to bring back their mother.",
            "The older brother has steel automail limbs; the younger brother's soul is bound inside a suit of armor.",
            "Governed by the Law of Equivalent Exchange as they search for the Philosopher's Stone."
        ],
        "normal_clue": "Two alchemist brothers search for the Philosopher's Stone to restore their bodies after a failed human transmutation.",
        "progressive_clues": [
            "Edward Elric despises milk and flies into a rage whenever anyone calls him short.",
            "His younger brother Alphonse is a gentle soul bound inside a towering suit of steel armor.",
            "They confront the seven Homunculi named after the Seven Deadly Sins."
        ],
        "cryptic_clue": "Braided gold, automail limbs, and an equivalent exchange that cost flesh before the Truth's white gate.",
        "letter_hint": "F _ _ _ _ _ _ _ _   A _ _ _ _ _ _ _ _",
        "fun_fact": "Edward's silver pocket watch is inscribed inside with 'Don't forget 3.OCT.11', the day the brothers burned down their home."
    },
    {
        "id": "anime_07",
        "category": "anime",
        "name": "One Punch Man",
        "aliases": ["saitama", "opm", "caped baldy"],
        "difficulty": "medium",
        "year": 2015,
        "director": "ONE",
        "actor": "Saitama",
        "rated": "TV-14",
        "genres": ["Action", "Comedy"],
        "studio": "Madhouse",
        "poster_theme": {
            "bg1": "#422006",
            "bg2": "#ca8a04",
            "accent": "#ef4444",
            "icon": "👊",
            "subtitle": "Hero For Fun"
        },
        "tips": [
            "The protagonist grew completely bald after doing 100 pushups, 100 situps, 100 squats, and a 10km run every day.",
            "He suffers from boredom because every monster explodes with a single normal punch.",
            "Accompanied by his earnest cyborg disciple Genos in the Hero Association."
        ],
        "normal_clue": "A hero for fun who grew completely bald from basic daily workouts can defeat any foe with a single punch.",
        "progressive_clues": [
            "Suffers from existential boredom and cares deeply about catching Saturday supermarket sales.",
            "Mentors the S-Class cyborg youth Genos while registered as 'Caped Baldy'.",
            "Wears a bright yellow jumpsuit with red gloves, red boots, and a white cape."
        ],
        "cryptic_clue": "A cracked ceiling of biological limits earned through mundane calisthenics, longing for a fight that lasts two blows.",
        "letter_hint": "O _ _   P _ _ _ _   M _ _",
        "fun_fact": "Saitama's yellow suit and red gloves are a color-inverted homage to the classic Japanese children's superhero Anpanman!"
    },
    {
        "id": "anime_08",
        "category": "anime",
        "name": "Demon Slayer",
        "aliases": ["kimetsu no yaiba", "tanjiro kamado", "demon slayer kimetsu no yaiba"],
        "difficulty": "easy",
        "year": 2019,
        "director": "Koyoharu Gotouge",
        "actor": "Tanjiro Kamado",
        "rated": "TV-MA",
        "genres": ["Action", "Dark Fantasy"],
        "studio": "Ufotable",
        "poster_theme": {
            "bg1": "#062e22",
            "bg2": "#0d9488",
            "accent": "#f43f5e",
            "icon": "🗡️",
            "subtitle": "Water & Sun Breathing"
        },
        "tips": [
            "A kind-hearted charcoal seller carries his demon-turned sister Nezuko in a wooden box on his back.",
            "Wears a distinctive green-and-black checkered haori coat and hanafuda earrings.",
            "Swordsmen use elemental Breathing Styles (Water, Thunder, Flame, Beast) with Nichirin blades."
        ],
        "normal_clue": "A young boy joins a secret corps of swordsmen to cure his sister Nezuko after she is turned into a demon.",
        "progressive_clues": [
            "Tanjiro Kamado possesses a superhuman sense of smell and wears a green-and-black checkered haori.",
            "Travels alongside the cowardly thunder-swordsman Zenitsu and boar-masked Inosuke.",
            "Hunts the progenitor of all demons, Muzan Kibutsuji, alongside the elite Hashira."
        ],
        "cryptic_clue": "Checkered emerald cloth and hanafuda earrings guard a bamboo-muzzled sister inside a cedar backpack.",
        "letter_hint": "D _ _ _ _   S _ _ _ _ _",
        "fun_fact": "The Mugen Train film became the highest-grossing movie in Japanese box office history, surpassing Spirited Away!"
    },
    {
        "id": "anime_09",
        "category": "anime",
        "name": "Jujutsu Kaisen",
        "aliases": ["jjk", "yuji itadori", "satoru gojo", "gojo"],
        "difficulty": "medium",
        "year": 2020,
        "director": "Gege Akutami",
        "actor": "Yuji Itadori",
        "rated": "TV-MA",
        "genres": ["Action", "Supernatural"],
        "studio": "MAPPA",
        "poster_theme": {
            "bg1": "#0f0728",
            "bg2": "#311068",
            "accent": "#38bdf8",
            "icon": "🤞",
            "subtitle": "Domain Expansion"
        },
        "tips": [
            "A high school teenager swallows a rotting cursed finger belonging to Ryomen Sukuna, the King of Curses.",
            "His blindfolded white-haired teacher Satoru Gojo wields the Limitless and Six Eyes.",
            "Sorcerers unleash ultimate barrier techniques known as 'Domain Expansion'."
        ],
        "normal_clue": "A high schooler swallows a rotting cursed finger to save his friends and enrolls in Tokyo Jujutsu High under Satoru Gojo.",
        "progressive_clues": [
            "Yuji Itadori becomes the host of the four-armed King of Curses, Ryomen Sukuna.",
            "Forms a first-year trio with shadow-summoner Megumi Fushiguro and hammer-wielding Nobara Kugisaki.",
            "Features Black Flash strikes and supreme techniques called Domain Expansion."
        ],
        "cryptic_clue": "Twenty mummified digits feed a double-eyed parasite while a blindfolded mentor crosses fingers for Infinite Void.",
        "letter_hint": "J _ _ _ _ _ _   K _ _ _ _ _",
        "fun_fact": "Author Gege Akutami was heavily inspired by Bleach, YuYu Hakusho, and Hunter x Hunter when designing the Cursed Energy system!"
    },
    {
        "id": "anime_10",
        "category": "anime",
        "name": "My Hero Academia",
        "aliases": ["boku no hero academia", "mha", "izuku midoriya", "deku"],
        "difficulty": "easy",
        "year": 2016,
        "director": "Kohei Horikoshi",
        "actor": "Izuku Midoriya",
        "rated": "TV-14",
        "genres": ["Action", "Shonen"],
        "studio": "Bones",
        "poster_theme": {
            "bg1": "#063b27",
            "bg2": "#15803d",
            "accent": "#facc15",
            "icon": "🦸",
            "subtitle": "Plus Ultra!"
        },
        "tips": [
            "Set in a world where 80% of humanity is born with superpowers called 'Quirks'.",
            "A Quirkless fanboy inherits the transferable power 'One For All' from the #1 hero, All Might.",
            "Students train at the prestigious U.A. High School under the motto 'Plus Ultra!'"
        ],
        "normal_clue": "In a world where 80% of humans have superpowers called Quirks, a powerless boy inherits the ultimate ability from his idol All Might.",
        "progressive_clues": [
            "Izuku 'Deku' Midoriya eats a strand of All Might's glowing hair to inherit the Quirk 'One For All'.",
            "Attends Class 1-A at U.A. High School alongside explosive rival Katsuki Bakugo and Shoto Todoroki.",
            "Battles Tomura Shigaraki and the League of Villains under the school motto 'Plus Ultra!'"
        ],
        "cryptic_clue": "A quirkless notebook keeper swallows a smiling titan's golden hair to smash villains beyond hundred-percent bone limits.",
        "letter_hint": "M _   H _ _ _   A _ _ _ _ _ _ _",
        "fun_fact": "All Might's signature move names are all named after US states and cities (Detroit Smash, Texas Smash, United States of Smash)!"
    },
    {
        "id": "anime_11",
        "category": "anime",
        "name": "Cowboy Bebop",
        "aliases": ["spike spiegel", "bebop"],
        "difficulty": "hard",
        "year": 1998,
        "director": "Shinichiro Watanabe",
        "actor": "Spike Spiegel",
        "rated": "TV-14",
        "genres": ["Sci-Fi", "Action"],
        "studio": "Sunrise",
        "poster_theme": {
            "bg1": "#111827",
            "bg2": "#312e81",
            "accent": "#f59e0b",
            "icon": "🎷",
            "subtitle": "See You Space Cowboy"
        },
        "tips": [
            "Follows a ragtag crew of futuristic space bounty hunters ('Cowboys') in the year 2071.",
            "Features an iconic big-band jazz opening theme song called 'Tank!' by Yoko Kanno.",
            "Crew includes Spike Spiegel, Jet Black, Faye Valentine, hacker Ed, and a Welsh Corgi named Ein."
        ],
        "normal_clue": "A ragtag crew of bounty hunters aboard the spaceship Bebop chase criminals across the solar system to a jazz soundtrack.",
        "progressive_clues": [
            "Spike Spiegel practices Jeet Kune Do, pilots the red Swordfish II, and has one artificial eye.",
            "Travels alongside ex-cop Jet Black, amnesia-stricken gambler Faye Valentine, Ed, and data-dog Ein.",
            "Every episode is named after a musical genre or classic rock/jazz song, ending with 'See You Space Cowboy...'"
        ],
        "cryptic_clue": "Green-haired jazz cowboy with one eye seeing the past and one seeing the present, signing off with a finger-gun 'Bang'.",
        "letter_hint": "C _ _ _ _ _   B _ _ _ _",
        "fun_fact": "Spike Spiegel's martial arts fighting style and philosophy ('Be like water') were directly modeled after Bruce Lee!"
    },
    {
        "id": "anime_12",
        "category": "anime",
        "name": "Spirited Away",
        "aliases": ["sen to chihiro", "chihiro"],
        "difficulty": "medium",
        "year": 2001,
        "director": "Hayao Miyazaki",
        "actor": "Chihiro Ogino",
        "rated": "PG",
        "genres": ["Fantasy", "Adventure"],
        "studio": "Studio Ghibli",
        "poster_theme": {
            "bg1": "#2e1065",
            "bg2": "#701a75",
            "accent": "#fde047",
            "icon": "🏮",
            "subtitle": "Bathhouse Of The Spirits"
        },
        "tips": [
            "A 10-year-old girl's parents are transformed into pigs after eating food meant for spirits.",
            "She must work at a magical bathhouse run by the witch Yubaba and aided by river spirit Haku.",
            "Features the masked spirit No-Face (Kaonashi) who offers gold nuggets."
        ],
        "normal_clue": "A young girl wanders into a world of kami spirits after her parents are turned into pigs, working in a magical bathhouse to free them.",
        "progressive_clues": [
            "Chihiro has her name stolen by the bathhouse witch Yubaba, becoming 'Sen'.",
            "Befriends the dragon river spirit Haku and the lonely masked spirit No-Face.",
            "Directed by Hayao Miyazaki at Studio Ghibli, winning the Academy Award for Best Animated Feature."
        ],
        "cryptic_clue": "Gluttonous parents squeal in stalls while a nameless child scrubs river mud from a stink god beneath red lanterns.",
        "letter_hint": "S _ _ _ _ _ _ _   A _ _ _",
        "fun_fact": "Hayao Miyazaki wrote the film without a completed script, developing the story board by board as animation progressed!"
    },
    {
        "id": "anime_13",
        "category": "anime",
        "name": "Hunter x Hunter",
        "aliases": ["hxh", "gon freecss", "killua zoldyck"],
        "difficulty": "medium",
        "year": 2011,
        "director": "Yoshihiro Togashi",
        "actor": "Gon Freecss",
        "rated": "TV-14",
        "genres": ["Adventure", "Shonen"],
        "studio": "Madhouse",
        "poster_theme": {
            "bg1": "#052e16",
            "bg2": "#166534",
            "accent": "#facc15",
            "icon": "🎣",
            "subtitle": "Aura Of Nen"
        },
        "tips": [
            "A cheerful boy in green with a fishing rod takes a deadly exam to find his legendary father, Ging.",
            "His best friend is a silver-haired boy from the notorious Zoldyck family of assassins.",
            "Fighters use a life-energy aura system called 'Nen' and face the Phantom Troupe & Chimera Ants."
        ],
        "normal_clue": "Young Gon Freecss takes the grueling Hunter Exam to track down his absentee father, befriending ex-assassin Killua along the way.",
        "progressive_clues": [
            "Forms a core group with Killua Zoldyck, scarlet-eyed survivor Kurapika, and aspiring doctor Leorio.",
            "Masters the complex aura system 'Nen' and the rock-paper-scissors technique Jajanken.",
            "Features the sinister magician Hisoka, the Phantom Troupe spiders, and the Chimera Ant King Meruem."
        ],
        "cryptic_clue": "A fishing rod and a skateboard forge brotherhood between a beast-hunter's son and a lightning-palmed assassin heir.",
        "letter_hint": "H _ _ _ _ _   x   H _ _ _ _ _",
        "fun_fact": "Creator Yoshihiro Togashi is married to Naoko Takeuchi, the legendary creator of Sailor Moon!"
    },
    {
        "id": "anime_14",
        "category": "anime",
        "name": "Bleach",
        "aliases": ["ichigo kurosaki", "bleach thousand year blood war"],
        "difficulty": "medium",
        "year": 2004,
        "director": "Tite Kubo",
        "actor": "Ichigo Kurosaki",
        "rated": "TV-14",
        "genres": ["Action", "Supernatural"],
        "studio": "Studio Pierrot",
        "poster_theme": {
            "bg1": "#090d16",
            "bg2": "#1e293b",
            "accent": "#fb923c",
            "icon": "🌙",
            "subtitle": "Soul Reaper Bankai"
        },
        "tips": [
            "An orange-haired teenager who can see ghosts accidentally absorbs the powers of a Soul Reaper named Rukia.",
            "Wields an oversized cleaver-like sword called Zangetsu to purify corrupted spirits called Hollows.",
            "Captains of the Gotei 13 in Soul Society unleash two-stage sword releases: Shikai and Bankai."
        ],
        "normal_clue": "High schooler Ichigo Kurosaki obtains the powers of a Soul Reaper and defends humans from evil spirits called Hollows.",
        "progressive_clues": [
            "Rukia Kuchiki transfers her Soul Reaper powers to Ichigo to save his family in Karakura Town.",
            "Soul Reapers wield spirit swords called Zanpakuto that unlock ultimate transformations known as 'Bankai'.",
            "Invades Soul Society and Hueco Mundo to battle the traitorous Captain Sosuke Aizen."
        ],
        "cryptic_clue": "A scowling tangerine-haired ghost-seer swings a bandaged butcher blade shouting 'Getsuga Tensho' across Soul Society.",
        "letter_hint": "B _ _ _ _ _",
        "fun_fact": "Tite Kubo originally wanted the Soul Reapers to use guns instead of swords, calling the early concept 'Snipe'!"
    },
    {
        "id": "anime_15",
        "category": "anime",
        "name": "Code Geass",
        "aliases": ["lelouch", "code geass lelouch of the rebellion", "lelouch vi britannia"],
        "difficulty": "hard",
        "year": 2006,
        "director": "Goro Taniguchi",
        "actor": "Lelouch Lamperouge",
        "rated": "TV-14",
        "genres": ["Sci-Fi", "Thriller"],
        "studio": "Sunrise",
        "poster_theme": {
            "bg1": "#1e052b",
            "bg2": "#581c87",
            "accent": "#ef4444",
            "icon": "👁️",
            "subtitle": "Power Of Absolute Obedience"
        },
        "tips": [
            "An exiled prince of the Holy Britannian Empire gains a glowing red bird-sigil in his left eye.",
            "His power of 'Absolute Obedience' forces anyone who makes direct eye contact to obey any single command.",
            "Leads the Black Knights rebellion in a masked persona called 'Zero' piloting Knightmare Frames."
        ],
        "normal_clue": "Exiled prince Lelouch gains the ocular power of Absolute Obedience from a mysterious green-haired girl and leads a masked rebellion.",
        "progressive_clues": [
            "Granted the King's Power by the immortal witch C.C. in Area 11 (occupied Japan).",
            "Dons a theatrical cape and helmet as the vigilante tactician 'Zero' commanding the Black Knights.",
            "His childhood friend Suzaku Kururugi fights on the opposing side piloting the white mecha Lancelot."
        ],
        "cryptic_clue": "A crimson avian sigil in a prince's iris moves Knightmare chess pieces toward a self-sacrificing Zero Requiem.",
        "letter_hint": "C _ _ _   G _ _ _ _",
        "fun_fact": "The character designs were created by the famous all-female manga artist collective CLAMP!"
    },
    {
        "id": "anime_16",
        "category": "anime",
        "name": "Steins;Gate",
        "aliases": ["steins gate", "okabe rintaro", "hououin kyouma"],
        "difficulty": "insane",
        "year": 2011,
        "director": "Hiroshi Hamasaki",
        "actor": "Rintaro Okabe",
        "rated": "TV-14",
        "genres": ["Sci-Fi", "Thriller"],
        "studio": "White Fox",
        "poster_theme": {
            "bg1": "#1c1917",
            "bg2": "#44403c",
            "accent": "#f59e0b",
            "icon": "⏳",
            "subtitle": "El Psy Kongroo"
        },
        "tips": [
            "A self-proclaimed 'mad scientist' in Akihabara accidentally invents a microwave that sends text messages to the past.",
            "Sending a 'D-Mail' shifts the Divergence Meter across parallel worldlines.",
            "Drinks Dr Pepper and signs off phone calls to the 'Organization' with the phrase 'El Psy Kongroo'."
        ],
        "normal_clue": "An eccentric self-proclaimed mad scientist and his friends in Akihabara accidentally modify a microwave that can send text messages into the past.",
        "progressive_clues": [
            "Rintaro Okabe ('Hououin Kyouma') discovers that microwaving bananas turns them into green gel and teleports them.",
            "Teaming up with genius neuroscientist Kurisu Makise and hacker Daru at the Future Gadget Lab.",
            "Desperately leaps through time loops to save childhood friend Mayuri from fate while SERN hunts them."
        ],
        "cryptic_clue": "Gelatinous green bananas and a Nixie-tube divergence meter trap a lab-coated Dr Pepper drinker in Akihabara time loops.",
        "letter_hint": "S _ _ _ _ _ ; G _ _ _",
        "fun_fact": "The mysterious 2000 internet forum time-traveler 'John Titor' featured in the story was a real-world internet urban legend!"
    },

    # =========================================================================
    # 🔦 COMMON OBJECTS CATEGORY (16 Everyday Objects with Black Silhouette + Hints)
    # =========================================================================
    {
        "id": "objects_01",
        "category": "common_objects",
        "name": "Umbrella",
        "aliases": ["parasol", "rain umbrella", "brolly"],
        "difficulty": "easy",
        "year": 1750,
        "director": "Everyday Carry",
        "actor": "Fabric & Metal",
        "rated": "Manual",
        "genres": ["Outdoor", "Weather"],
        "studio": "Handheld",
        "silhouette_type": "umbrella",
        "tips": [
            "Features a curved J-shaped handle, a central shaft, and collapsible metal ribs.",
            "Pops open into a waterproof dome canopy whenever dark clouds start pouring rain.",
            "Superstition says opening one of these indoors brings bad luck!"
        ],
        "normal_clue": "A collapsible folding canopy supported by metal ribs on a central rod, held overhead to shield you from rain or sunlight.",
        "progressive_clues": [
            "Hint 1: It stays folded up neatly in a hallway stand until the weather turns stormy.",
            "Hint 2: Built from waterproof nylon fabric stretched across flexible metal spokes and a J-hook handle.",
            "Hint 3: You hold it above your head in a downpour so you don't get soaked!"
        ],
        "cryptic_clue": "A nylon mushroom that blooms only when the sky weeps and folds its steel bones when the sun returns.",
        "letter_hint": "U _ _ _ _ _ _ _",
        "fun_fact": "The word 'umbrella' comes from the Latin word 'umbra', meaning shade or shadow, as they were originally used to block the sun!"
    },
    {
        "id": "objects_02",
        "category": "common_objects",
        "name": "Scissors",
        "aliases": ["pair of scissors", "shears"],
        "difficulty": "easy",
        "year": 1500,
        "director": "Office & Desk",
        "actor": "Stainless Steel",
        "rated": "Manual",
        "genres": ["Cutting", "Craft"],
        "studio": "Handheld",
        "silhouette_type": "scissors",
        "tips": [
            "Consists of two pivoted metal blades with two finger loops on the handle.",
            "Used every day in classrooms, offices, and kitchens to slice paper, ribbon, or fabric.",
            "Also one of the three choices in the classic hand game alongside Rock and Paper!"
        ],
        "normal_clue": "A hand-operated cutting instrument consisting of two metal blades pivoted together so the sharp edges slide against each other.",
        "progressive_clues": [
            "Hint 1: Has two plastic or metal finger rings at one end and a central screw pivot in the middle.",
            "Hint 2: Beats Paper, but loses to Rock in the world's most famous hand game.",
            "Hint 3: Teachers always remind kids not to run while holding a pair of these!"
        ],
        "cryptic_clue": "Twin steel beaks joined at the waist that devour paper in a single snap of thumb and forefinger.",
        "letter_hint": "S _ _ _ _ _ _ _",
        "fun_fact": "Spring-activated bronze scissors were invented in ancient Mesopotamia and Egypt over 3,500 years ago!"
    },
    {
        "id": "objects_03",
        "category": "common_objects",
        "name": "Light Bulb",
        "aliases": ["lightbulb", "bulb", "lamp bulb", "incandescent bulb"],
        "difficulty": "easy",
        "year": 1879,
        "director": "Home & Ceiling",
        "actor": "Glass & Metal",
        "rated": "Electric",
        "genres": ["Lighting", "Household"],
        "studio": "Handheld",
        "silhouette_type": "lightbulb",
        "tips": [
            "Has a rounded pear-shaped glass globe on top of a threaded metal screw base.",
            "Popularized by Thomas Edison in 1879 using a glowing filament inside a vacuum.",
            "Appears above a cartoon character's head whenever they suddenly get a brilliant idea!"
        ],
        "normal_clue": "A pear-shaped glass globe with a threaded metal base that glows brightly when electric current flows through it.",
        "progressive_clues": [
            "Hint 1: Screws clockwise into lamps and ceiling sockets across every room in your house.",
            "Hint 2: Symbolizes a sudden 'Eureka!' moment or bright idea in comic strips.",
            "Hint 3: Perfected by Thomas Edison to banish darkness at the flip of a wall switch."
        ],
        "cryptic_clue": "A glass pear with a tungsten heart that banishes midnight at the flick of a wall switch.",
        "letter_hint": "L _ _ _ _   B _ _ _",
        "fun_fact": "The Centennial Light in Livermore, California is a hand-blown light bulb that has been burning almost continuously since 1901!"
    },
    {
        "id": "objects_04",
        "category": "common_objects",
        "name": "Headphones",
        "aliases": ["headset", "earphones", "earbuds"],
        "difficulty": "easy",
        "year": 1910,
        "director": "Everyday Carry",
        "actor": "Plastic & Foam",
        "rated": "Electric",
        "genres": ["Audio", "Music"],
        "studio": "Wearable",
        "silhouette_type": "headphones",
        "tips": [
            "Two cushioned ear cups connected by a curved headband that arches over the top of your head.",
            "Lets you listen to music, podcasts, or game audio privately without disturbing anyone nearby.",
            "Modern versions use Bluetooth wireless technology and active noise cancellation."
        ],
        "normal_clue": "A pair of padded speaker cups joined by a curved band worn over the head for listening to music or audio privately.",
        "progressive_clues": [
            "Hint 1: Arches over your head with soft cushions marked 'L' and 'R' for your left and right ears.",
            "Hint 2: Gamers, DJs, and commuters wear them to block out background noise.",
            "Hint 3: Plugs into an audio jack or pairs via Bluetooth to play your favorite songs."
        ],
        "cryptic_clue": "A padded arch bridging two private concert halls clamped over your left and right temples.",
        "letter_hint": "H _ _ _ _ _ _ _ _ _",
        "fun_fact": "The first modern headphones were invented in 1910 by Nathaniel Baldwin on his kitchen table and sold to the U.S. Navy!"
    },
    {
        "id": "objects_05",
        "category": "common_objects",
        "name": "Key",
        "aliases": ["house key", "door key", "keys"],
        "difficulty": "easy",
        "year": 1848,
        "director": "Everyday Carry",
        "actor": "Brass & Steel",
        "rated": "Manual",
        "genres": ["Security", "Hardware"],
        "studio": "Pocket-Sized",
        "silhouette_type": "key",
        "tips": [
            "Small flat metal tool with a rounded bow handle and a jagged, notched blade ('teeth').",
            "Carried on a ring in your pocket and inserted into a keyhole to unlock a door or padlock.",
            "Turning it aligns internal brass pins inside a lock cylinder."
        ],
        "normal_clue": "A small notched metal instrument that is inserted into a lock and turned to open or secure a door.",
        "progressive_clues": [
            "Hint 1: Jingles on a metal ring in your pocket alongside fobs and chains.",
            "Hint 2: Has a unique pattern of jagged metal teeth cut into its shaft.",
            "Hint 3: If you lose it outside, you might get locked out of your house or car!"
        ],
        "cryptic_clue": "A jagged brass tongue that whispers to tumblers and opens bolted thresholds with a single twist.",
        "letter_hint": "K _ _",
        "fun_fact": "The modern flat pin-tumbler key was patented by Linus Yale Jr. in 1861, a design still used on billions of doors today!"
    },
    {
        "id": "objects_06",
        "category": "common_objects",
        "name": "Coffee Mug",
        "aliases": ["mug", "cup", "teacup", "coffee cup"],
        "difficulty": "easy",
        "year": 1700,
        "director": "Kitchen",
        "actor": "Ceramic",
        "rated": "Manual",
        "genres": ["Drinkware", "Household"],
        "studio": "Handheld",
        "silhouette_type": "mug",
        "tips": [
            "A sturdy cylindrical ceramic vessel with a single C-shaped loop handle on the side.",
            "Used every morning to hold steaming hot coffee, tea, or hot chocolate.",
            "Often decorated with funny quotes, company logos, or travel souvenirs on office desks."
        ],
        "normal_clue": "A heavy cylindrical ceramic cup with a looped side handle used for drinking hot beverages like coffee, tea, or cocoa.",
        "progressive_clues": [
            "Hint 1: Sits on a coaster on almost every office desk in the morning.",
            "Hint 2: The curved side handle keeps your fingers from getting burned by hot liquid.",
            "Hint 3: Filled with freshly brewed espresso, tea, or hot cocoa with marshmallows."
        ],
        "cryptic_clue": "A glazed clay cylinder with a single ear that cradles morning caffeine and leaves rings on wooden desks.",
        "letter_hint": "C _ _ _ _ _   M _ _",
        "fun_fact": "Bone china mugs were invented in England in the 1740s to create cups strong enough to hold boiling liquids without cracking!"
    },
    {
        "id": "objects_07",
        "category": "common_objects",
        "name": "Bicycle",
        "aliases": ["bike", "cycle", "mountain bike"],
        "difficulty": "easy",
        "year": 1885,
        "director": "Outdoor",
        "actor": "Aluminum & Rubber",
        "rated": "Manual",
        "genres": ["Transport", "Sports"],
        "studio": "Large",
        "silhouette_type": "bicycle",
        "tips": [
            "Has two spoked rubber wheels in a line, handlebars for steering, a saddle seat, and two pedals.",
            "Powered entirely by your legs turning a metal chain connected to the rear wheel.",
            "Usually parked in a rack and secured with a U-lock, and you wear a helmet when riding it!"
        ],
        "normal_clue": "A human-powered two-wheeled vehicle steered with handlebars and propelled by pushing pedals connected to a chain.",
        "progressive_clues": [
            "Hint 1: Kids often learn to ride it using two small training wheels on the back.",
            "Hint 2: Features rubber tires, hand brakes, a bell, gears, and a metal chain.",
            "Hint 3: Ridden by athletes in the Tour de France and commuters in bike lanes worldwide."
        ],
        "cryptic_clue": "Two spoked circles linked by a diamond frame that turns human legwork into silent wind.",
        "letter_hint": "B _ _ _ _ _ _",
        "fun_fact": "Over 1 billion bicycles have been manufactured worldwide, more than twice the number of automobiles!"
    },
    {
        "id": "objects_08",
        "category": "common_objects",
        "name": "Eyeglasses",
        "aliases": ["glasses", "spectacles", "reading glasses", "sunglasses"],
        "difficulty": "easy",
        "year": 1286,
        "director": "Everyday Carry",
        "actor": "Glass & Metal",
        "rated": "Manual",
        "genres": ["Vision", "Accessory"],
        "studio": "Wearable",
        "silhouette_type": "glasses",
        "tips": [
            "Consists of two prescription lenses held in a frame with a nose bridge and two folding ear stems.",
            "Worn on the face to correct nearsightedness, farsightedness, or blurry reading vision.",
            "Kept inside a hard protective case with a microfiber cleaning cloth."
        ],
        "normal_clue": "A pair of optical lenses mounted in a frame that rests on the nose and ears to correct vision or protect the eyes.",
        "progressive_clues": [
            "Hint 1: Rests on the bridge of your nose with two hinged arms ('temples') hooking behind your ears.",
            "Hint 2: Fogs up when you walk into a warm room from the cold or drink hot soup.",
            "Hint 3: Helps millions of people read books, drive, and see clearly every single day."
        ],
        "cryptic_clue": "Twin crystal windows perched upon the nose that sharpen a blurry world.",
        "letter_hint": "E _ _ _ _ _ _ _ _ _",
        "fun_fact": "Benjamin Franklin invented bifocal glasses in the 1780s because he was tired of switching between two pairs of spectacles!"
    },
    {
        "id": "objects_09",
        "category": "common_objects",
        "name": "Guitar",
        "aliases": ["acoustic guitar", "electric guitar"],
        "difficulty": "medium",
        "year": 1850,
        "director": "Music & Stage",
        "actor": "Wood & Steel",
        "rated": "Manual",
        "genres": ["Music", "Instrument"],
        "studio": "Medium",
        "silhouette_type": "guitar",
        "tips": [
            "Has a figure-eight hourglass wooden body, a circular sound hole, and a long fretted neck.",
            "Typically features six taut strings tuned using six pegs at the headstock.",
            "Played by strumming or plucking the strings with your fingers or a small plastic pick."
        ],
        "normal_clue": "A six-stringed musical instrument with a curvaceous hourglass body and a fretted neck, played by strumming or plucking.",
        "progressive_clues": [
            "Hint 1: Features six tuning pegs at the top of a long neck divided by metal frets.",
            "Hint 2: Strummed with a triangular plastic pick ('plectrum') around campfires or on rock stages.",
            "Hint 3: Comes in acoustic hollow-body wood and solid-body electric varieties."
        ],
        "cryptic_clue": "A wooden hourglass strung with six taut wires that sings when fingernails or plastic triangles brush its waist.",
        "letter_hint": "G _ _ _ _ _",
        "fun_fact": "The modern acoustic guitar shape was perfected by Spanish carpenter Antonio de Torres Jurado in the 1850s!"
    },
    {
        "id": "objects_10",
        "category": "common_objects",
        "name": "Hammer",
        "aliases": ["claw hammer", "mallet"],
        "difficulty": "medium",
        "year": 1840,
        "director": "Workshop",
        "actor": "Steel & Wood",
        "rated": "Manual",
        "genres": ["Tools", "Hardware"],
        "studio": "Handheld",
        "silhouette_type": "hammer",
        "tips": [
            "A heavy T-shaped hand tool with a wooden or fiberglass grip and a forged steel head.",
            "One side of the metal head is flat for driving nails into wood; the other side has a curved V-claw.",
            "The curved claw uses leverage to pry bent nails back out of timber!"
        ],
        "normal_clue": "A hand tool with a heavy metal head mounted at right angles to a handle, used for driving nails into wood and prying them out.",
        "progressive_clues": [
            "Hint 1: Found in every toolbox alongside screwdrivers, wrenches, and measuring tape.",
            "Hint 2: Has a flat striking face on one side and a split curved claw on the back.",
            "Hint 3: Swung down to drive iron nails into wooden boards when building or hanging a picture."
        ],
        "cryptic_clue": "An iron head with a flat face to drive steel pins in and a split talon to yank mistakes back out.",
        "letter_hint": "H _ _ _ _ _",
        "fun_fact": "Hammers are humanity's oldest tool—stone hammers dating back 3.3 million years have been discovered by archaeologists in Kenya!"
    },
    {
        "id": "objects_11",
        "category": "common_objects",
        "name": "Wristwatch",
        "aliases": ["watch", "clock", "smartwatch"],
        "difficulty": "medium",
        "year": 1904,
        "director": "Everyday Carry",
        "actor": "Steel & Leather",
        "rated": "Battery",
        "genres": ["Timekeeping", "Accessory"],
        "studio": "Wearable",
        "silhouette_type": "watch",
        "tips": [
            "A circular dial with hour, minute, and second hands attached to a leather or metal strap.",
            "Buckled around your wrist so you can check the time at a glance.",
            "Ticks 60 times a minute using either mechanical gears or a quartz crystal battery."
        ],
        "normal_clue": "A small portable timepiece with a circular dial and a strap designed to be worn buckled around the wrist.",
        "progressive_clues": [
            "Hint 1: Strapped around your left or right wrist with a buckle or metal clasp.",
            "Hint 2: Features twelve numbers around a circular glass face and two or three rotating hands.",
            "Hint 3: Tells you the exact hour, minute, and second whenever you glance at your arm."
        ],
        "cryptic_clue": "Three tireless hands sweeping twelve stations while strapped to your pulse.",
        "letter_hint": "W _ _ _ _ _ _ _ _ _",
        "fun_fact": "Men wore pocket watches until aviation pioneer Alberto Santos-Dumont asked Louis Cartier in 1904 to make a watch he could check while keeping both hands on airplane controls!"
    },
    {
        "id": "objects_12",
        "category": "common_objects",
        "name": "Camera",
        "aliases": ["photo camera", "dslr", "digital camera"],
        "difficulty": "medium",
        "year": 1888,
        "director": "Everyday Carry",
        "actor": "Glass & Metal",
        "rated": "Battery",
        "genres": ["Photography", "Optics"],
        "studio": "Handheld",
        "silhouette_type": "camera",
        "tips": [
            "A rectangular body with a protruding circular glass zoom lens on the front and a shutter button on top.",
            "Flashes a bright light and clicks when capturing a photograph or recording video.",
            "People smile and say 'Cheese!' whenever one of these is pointed at them."
        ],
        "normal_clue": "An optical device with a circular glass lens and shutter button used to capture still photographs or video.",
        "progressive_clues": [
            "Hint 1: Hangs from a neck strap on tourists and journalists or sits atop a three-legged tripod.",
            "Hint 2: Features a round focusing lens on the front, a viewfinder, and a bright flash.",
            "Hint 3: Everyone smiles and says 'Cheese!' right before you press the top button!"
        ],
        "cryptic_clue": "A one-eyed black box that blinks for a fraction of a second to freeze a fleeting moment forever.",
        "letter_hint": "C _ _ _ _ _",
        "fun_fact": "The word 'camera' comes from 'camera obscura', which is Latin for 'dark chamber'!"
    },
    {
        "id": "objects_13",
        "category": "common_objects",
        "name": "Toothbrush",
        "aliases": ["tooth brush", "electric toothbrush"],
        "difficulty": "easy",
        "year": 1938,
        "director": "Bathroom",
        "actor": "Plastic & Nylon",
        "rated": "Manual",
        "genres": ["Hygiene", "Household"],
        "studio": "Handheld",
        "silhouette_type": "toothbrush",
        "tips": [
            "A slender plastic stick with a small rectangular cluster of soft nylon bristles at one end.",
            "Topped with a pea-sized swirl of minty paste and used at the bathroom sink twice a day.",
            "Dentists recommend replacing it every three months to keep your smile clean and cavity-free!"
        ],
        "normal_clue": "A small long-handled brush with soft nylon bristles used with minty paste to clean teeth and gums at the bathroom sink.",
        "progressive_clues": [
            "Hint 1: Stands upright in a cup beside the bathroom sink mirror.",
            "Hint 2: Topped with a ribbon of minty fluoride toothpaste morning and night.",
            "Hint 3: Used for two minutes twice a day to prevent cavities and plaque."
        ],
        "cryptic_clue": "A slender wand crowned with nylon bristles that foams with mint twice daily to guard thirty-two ivory pearls.",
        "letter_hint": "T _ _ _ _ _ _ _ _ _",
        "fun_fact": "The first bristle toothbrush was invented in China during the Tang Dynasty using stiff hairs from Siberian hogs attached to bamboo!"
    },
    {
        "id": "objects_14",
        "category": "common_objects",
        "name": "Backpack",
        "aliases": ["rucksack", "bookbag", "schoolbag", "knapsack"],
        "difficulty": "medium",
        "year": 1938,
        "director": "Everyday Carry",
        "actor": "Nylon & Fabric",
        "rated": "Manual",
        "genres": ["Storage", "Travel"],
        "studio": "Wearable",
        "silhouette_type": "backpack",
        "tips": [
            "A zippered fabric bag with two padded shoulder straps worn on your back.",
            "Used by students to carry textbooks, notebooks, and laptops to school every day.",
            "Hikers and travelers pack clothes, water bottles, and gear inside its compartments."
        ],
        "normal_clue": "A zippered cloth bag with two shoulder straps that allow you to carry books, laptops, and supplies hands-free on your back.",
        "progressive_clues": [
            "Hint 1: Has two adjustable padded straps that slip over both of your shoulders.",
            "Hint 2: Packed with textbooks, binders, pencils, and a laptop by students every morning.",
            "Hint 3: Features a main zippered compartment, a front pouch, and side mesh pockets for water bottles."
        ],
        "cryptic_clue": "A zippered fabric turtle shell slung over two shoulders to haul knowledge and gear hands-free.",
        "letter_hint": "B _ _ _ _ _ _ _",
        "fun_fact": "The first zippered backpack was invented in 1938 by outdoor enthusiast Gerry Cunningham so his gear wouldn't fall out while rock climbing!"
    },
    {
        "id": "objects_15",
        "category": "common_objects",
        "name": "Hourglass",
        "aliases": ["sand timer", "sandglass", "egg timer"],
        "difficulty": "hard",
        "year": 1338,
        "director": "Office & Desk",
        "actor": "Glass & Sand",
        "rated": "Manual",
        "genres": ["Timekeeping", "Classic"],
        "studio": "Handheld",
        "silhouette_type": "hourglass",
        "tips": [
            "Two connected vertical glass bulbs pinched into a narrow waist in the center.",
            "Fine grains of sand trickle steadily from the top bulb to the bottom bulb through gravity.",
            "Once all the sand reaches the bottom, you flip it upside down to start the timer again!"
        ],
        "normal_clue": "A classic timekeeping device made of two connected glass bulbs with a narrow neck that measures time as sand trickles from top to bottom.",
        "progressive_clues": [
            "Hint 1: Uses gravity instead of gears or batteries to measure a fixed span of time.",
            "Hint 2: Fine golden sand pours through a tiny pinched glass waist between two bulbs.",
            "Hint 3: Also the classic computer cursor icon shown when a program is loading or waiting!"
        ],
        "cryptic_clue": "Twin crystal bulbs pinched at the waist where falling desert grains measure the flight of minutes until flipped anew.",
        "letter_hint": "H _ _ _ _ _ _ _ _",
        "fun_fact": "Sailors on historic wooden ships preferred hourglasses over mechanical clocks because ocean waves didn't affect the flow of sand!"
    },
    {
        "id": "objects_16",
        "category": "common_objects",
        "name": "Flashlight",
        "aliases": ["torch", "electric torch"],
        "difficulty": "medium",
        "year": 1899,
        "director": "Everyday Carry",
        "actor": "Aluminum & Glass",
        "rated": "Battery",
        "genres": ["Lighting", "Outdoor"],
        "studio": "Handheld",
        "silhouette_type": "flashlight",
        "tips": [
            "A cylindrical handheld tube containing batteries and a bright LED bulb behind a reflector lens.",
            "Projects a focused cone beam of light in whatever direction you point it.",
            "Essential during power outages, camping trips, or telling spooky stories in a tent!"
        ],
        "normal_clue": "A portable battery-powered tubular light source that projects a focused beam when you press its side button.",
        "progressive_clues": [
            "Hint 1: Kept in a kitchen drawer or glovebox for power outages and dark nights.",
            "Hint 2: Runs on cylindrical batteries inside a metal or plastic tube with a flared lens head.",
            "Hint 3: Campers and night guards point its bright beam to see down dark trails."
        ],
        "cryptic_clue": "A battery-fed cylinder that carves a white cone through pitch-black woods at the press of a thumb.",
        "letter_hint": "F _ _ _ _ _ _ _ _ _",
        "fun_fact": "It was originally called a 'flash light' in 1899 because early dry-cell batteries couldn't provide a steady current and could only be turned on in brief flashes!"
    },

    # =========================================================================
    # 🎬 MOVIES CATEGORY (24 Iconic Films with 6-Attribute Metadata)
    # =========================================================================
    {
        "id": "movies_01",
        "category": "movies",
        "name": "Inception",
        "aliases": ["inception movie", "inception 2010"],
        "difficulty": "easy",
        "year": 2010,
        "director": "Christopher Nolan",
        "actor": "Leonardo DiCaprio",
        "rated": "PG-13",
        "genres": ["Sci-Fi", "Action"],
        "studio": "Warner Bros.",
        "poster_theme": {
            "bg1": "#0f172a",
            "bg2": "#1e3a5f",
            "accent": "#f59e0b",
            "icon": "🌀",
            "scene": "spinning_top",
            "subtitle": "Dream Within A Dream"
        },
        "tips": [
            "The protagonist uses a spinning pewter top totem to check if he is in reality.",
            "Features a mind-bending zero-gravity hotel hallway fight scene.",
            "Shares its director and studio with The Dark Knight and Interstellar."
        ],
        "normal_clue": "Christopher Nolan's sci-fi heist movie where thieves enter dreams within dreams to plant an idea.",
        "progressive_clues": [
            "A spinning pewter totem determines whether the protagonist is in reality or still dreaming.",
            "Dom Cobb leads a crew through multiple recursive subconscious dream layers with a zero-gravity hallway fight.",
            "Stars Leonardo DiCaprio and ends on a cliffhanger with a spinning top on a wooden table."
        ],
        "cryptic_clue": "A brass spindle wobbles as architectural mirrors fold cities into gravity-defying recursive slumbers.",
        "letter_hint": "I _ _ _ _ _ _ _ _",
        "fun_fact": "The famous revolving hallway fight scene was shot using an enormous 100-foot rotating centrifuge set!"
    },
    {
        "id": "movies_02",
        "category": "movies",
        "name": "The Matrix",
        "aliases": ["matrix", "the matrix 1999"],
        "difficulty": "easy",
        "year": 1999,
        "director": "The Wachowskis",
        "actor": "Keanu Reeves",
        "rated": "R",
        "genres": ["Sci-Fi", "Action"],
        "studio": "Warner Bros.",
        "poster_theme": {
            "bg1": "#021a08",
            "bg2": "#063b16",
            "accent": "#22c55e",
            "icon": "🕶️",
            "scene": "matrix_rain",
            "subtitle": "Digital Simulation"
        },
        "tips": [
            "Offers a famous choice between a red pill and a blue pill.",
            "Pioneered 'bullet-time' slow-motion gunfight photography in black trench coats.",
            "A computer hacker named Neo discovers humanity is trapped inside a machine simulation."
        ],
        "normal_clue": "A sci-fi blockbuster where a hacker named Neo learns humanity is trapped in a simulated reality by AI machines.",
        "progressive_clues": [
            "A choice between a blue pill to stay in illusion or a red pill to see how deep the rabbit hole goes.",
            "Pioneered bullet-time visual effects with leather trench coats and sunglasses.",
            "Morpheus guides Neo to become 'The One' and dismantle Agent Smith's control."
        ],
        "cryptic_clue": "Green cascading digital rain masks a battery farm; pick the scarlet capsule to wake in Zion's grim machine world.",
        "letter_hint": "T _ _   M _ _ _ _ _",
        "fun_fact": "The iconic falling green code is actually comprised of Japanese katakana characters copied from sushi cookbooks!"
    },
    {
        "id": "movies_03",
        "category": "movies",
        "name": "Titanic",
        "aliases": ["titanic 1997"],
        "difficulty": "easy",
        "year": 1997,
        "director": "James Cameron",
        "actor": "Leonardo DiCaprio",
        "rated": "PG-13",
        "genres": ["Drama", "Romance"],
        "studio": "Paramount Pictures",
        "poster_theme": {
            "bg1": "#09152b",
            "bg2": "#1d3557",
            "accent": "#38bdf8",
            "icon": "🚢",
            "scene": "ocean_ship",
            "subtitle": "Ship of Dreams"
        },
        "tips": [
            "Centers around the ill-fated 1912 maiden voyage of an 'unsinkable' luxury liner.",
            "Features the Heart of the Ocean blue diamond necklace and 'I'm the king of the world!'",
            "Won 11 Academy Awards including Best Picture and Best Director."
        ],
        "normal_clue": "James Cameron's romantic disaster epic featuring Jack and Rose aboard an ill-fated luxury passenger liner in 1912.",
        "progressive_clues": [
            "A wealthy aristocrat falls in love with a penniless artist on the ship of dreams.",
            "Features the Heart of the Ocean sapphire necklace and the iconic bow proclamation: 'I'm the king of the world!'",
            "Tragedy strikes at 11:40 PM when the starboard side collides with a North Atlantic iceberg."
        ],
        "cryptic_clue": "A floating door with room for two, blue diamond plunged into the icy abyss to the strains of Celine Dion.",
        "letter_hint": "T _ _ _ _ _ _",
        "fun_fact": "James Cameron spent more time at the actual wreckage of the Titanic than the passengers did on the original voyage!"
    },
    {
        "id": "movies_04",
        "category": "movies",
        "name": "Jurassic Park",
        "aliases": ["jurassic park 1993"],
        "difficulty": "medium",
        "year": 1993,
        "director": "Steven Spielberg",
        "actor": "Sam Neill",
        "rated": "PG-13",
        "genres": ["Sci-Fi", "Adventure"],
        "studio": "Universal Pictures",
        "poster_theme": {
            "bg1": "#1a1206",
            "bg2": "#3f2e0e",
            "accent": "#eab308",
            "icon": "🦖",
            "scene": "dino_island",
            "subtitle": "65 Million Years In The Making"
        },
        "tips": [
            "Prehistoric DNA is extracted from mosquitoes preserved in fossilized tree amber.",
            "A cup of water ripples on a Ford Explorer dashboard as a T-Rex approaches.",
            "Set on the remote island theme park of Isla Nublar off the coast of Costa Rica."
        ],
        "normal_clue": "Steven Spielberg's thriller where genetically cloned dinosaurs run amok on Isla Nublar.",
        "progressive_clues": [
            "Prehistoric DNA extracted from mosquitoes preserved in amber resurrected long-extinct monsters.",
            "A cup of water ripples on a dashboard just before a giant Tyrannosaurus Rex attacks a tour vehicle.",
            "Dr. Alan Grant and Dr. Ian Malcolm must survive after Dennis Nedry sabotages park security."
        ],
        "cryptic_clue": "Frogs mend shattered ancient spirals; an eccentric amber cane keeper assures 'spared no expense' while raptors test door handles.",
        "letter_hint": "J _ _ _ _ _ _ _   P _ _ _",
        "fun_fact": "The T-Rex's roar was a combination of sounds from a tiger, an alligator, and a baby elephant!"
    },
    {
        "id": "movies_05",
        "category": "movies",
        "name": "The Dark Knight",
        "aliases": ["dark knight", "the dark knight 2008"],
        "difficulty": "medium",
        "year": 2008,
        "director": "Christopher Nolan",
        "actor": "Christian Bale",
        "rated": "PG-13",
        "genres": ["Action", "Crime"],
        "studio": "Warner Bros.",
        "poster_theme": {
            "bg1": "#090d16",
            "bg2": "#1e293b",
            "accent": "#3b82f6",
            "icon": "🦇",
            "scene": "gotham_knight",
            "subtitle": "Why So Serious?"
        },
        "tips": [
            "Features an iconic opening bank heist where criminals wear clown masks.",
            "The main villain burns a giant pyramid of mob cash and asks, 'Why so serious?'",
            "Second installment in Christopher Nolan's Gotham superhero trilogy."
        ],
        "normal_clue": "Batman faces off against Heath Ledger's psychopathic Joker, who seeks to plunge Gotham City into total anarchy.",
        "progressive_clues": [
            "A masked vigilante teams with Lieutenant Gordon and District Attorney Harvey Dent.",
            "The villain burns a mountain of mob money, asks 'Why so serious?', and orchestrates a ferry dilemma.",
            "Heath Ledger won a posthumous Academy Award for Best Supporting Actor for this role."
        ],
        "cryptic_clue": "Two face coins flip in ashes, a scarred clown makes a pencil disappear, and a hero flees dogs to be the protector Gotham needs.",
        "letter_hint": "T _ _   D _ _ _   K _ _ _ _ _",
        "fun_fact": "Heath Ledger spent weeks locked in a London hotel room alone, crafting the Joker's journal and voice before filming."
    },
    {
        "id": "movies_06",
        "category": "movies",
        "name": "Interstellar",
        "aliases": ["interstellar 2014"],
        "difficulty": "hard",
        "year": 2014,
        "director": "Christopher Nolan",
        "actor": "Matthew McConaughey",
        "rated": "PG-13",
        "genres": ["Sci-Fi", "Adventure"],
        "studio": "Paramount Pictures",
        "poster_theme": {
            "bg1": "#070714",
            "bg2": "#1e1b4b",
            "accent": "#f97316",
            "icon": "🕳️",
            "scene": "black_hole",
            "subtitle": "Beyond Our Solar System"
        },
        "tips": [
            "On a water planet orbiting a supermassive black hole, 1 hour equals 7 years on Earth.",
            "A father communicates with his daughter Murph across time via a bedroom bookshelf.",
            "Features helpful rectangular robots named TARS and CASE."
        ],
        "normal_clue": "An ex-NASA pilot travels through a wormhole near Saturn to find a habitable new planet for dying humanity.",
        "progressive_clues": [
            "A dusty blight plagues Earth's crops, forcing Cooper to leave his daughter Murph behind.",
            "Visits Miller's planet where one hour equals seven years on Earth due to Gargantua's extreme gravity.",
            "Communicates across time through a tesseract bookshelf via the ticking second hand of a watch."
        ],
        "cryptic_clue": "Tick marks each decade by the sea of mountain waves, where love transcends dimensions behind a dusty nursery bookcase.",
        "letter_hint": "I _ _ _ _ _ _ _ _ _ _ _",
        "fun_fact": "The visual simulations of the Gargantua black hole were so scientifically accurate they resulted in published astrophysics research papers!"
    },
    {
        "id": "movies_07",
        "category": "movies",
        "name": "Pulp Fiction",
        "aliases": ["pulp fiction 1994"],
        "difficulty": "hard",
        "year": 1994,
        "director": "Quentin Tarantino",
        "actor": "John Travolta",
        "rated": "R",
        "genres": ["Crime", "Drama"],
        "studio": "Miramax",
        "poster_theme": {
            "bg1": "#2a0808",
            "bg2": "#5c1616",
            "accent": "#facc15",
            "icon": "💼",
            "scene": "glowing_briefcase",
            "subtitle": "Royale With Cheese"
        },
        "tips": [
            "Told out of chronological order, weaving together LA mobsters, a boxer, and two diner robbers.",
            "Revolves around a mysterious briefcase with a glowing golden interior and lock code 666.",
            "Two hitmen discuss what a Quarter Pounder with Cheese is called in Paris."
        ],
        "normal_clue": "Quentin Tarantino's non-linear neo-noir crime masterpiece starring John Travolta and Samuel L. Jackson.",
        "progressive_clues": [
            "Features the mysterious glowing golden briefcase with lock combination 666.",
            "Contains a twist dance competition at Jack Rabbit Slim's and an adrenaline syringe to the heart.",
            "Hitmen Vincent Vega and Jules Winnfield debate French McDonald's burger names and divine intervention."
        ],
        "cryptic_clue": "A five-dollar milkshake, Ezekiel 25:17 recited before gunpowder, and a royale with cheese in non-chronological order.",
        "letter_hint": "P _ _ _   F _ _ _ _ _ _",
        "fun_fact": "Vincent Vega's cherry-red 1964 Chevy Chevelle Malibu was actually Quentin Tarantino's personal car, and it was stolen during filming!"
    },
    {
        "id": "movies_08",
        "category": "movies",
        "name": "Back to the Future",
        "aliases": ["back to the future 1985", "bttf"],
        "difficulty": "insane",
        "year": 1985,
        "director": "Robert Zemeckis",
        "actor": "Michael J. Fox",
        "rated": "PG",
        "genres": ["Sci-Fi", "Adventure"],
        "studio": "Universal Pictures",
        "poster_theme": {
            "bg1": "#0c142c",
            "bg2": "#1e3a8a",
            "accent": "#fb923c",
            "icon": "⚡",
            "scene": "delorean_clock",
            "subtitle": "88 Miles Per Hour"
        },
        "tips": [
            "Time travel requires a flux capacitor, 1.21 gigawatts, and hitting 88 miles per hour.",
            "A teenager accidentally travels from 1985 back to 1955 in a stainless-steel DeLorean.",
            "He must get his parents to kiss at the Enchantment Under the Sea school dance."
        ],
        "normal_clue": "A teenager travels back to 1955 in a plutonium-powered stainless steel sports car and must make his parents fall in love.",
        "progressive_clues": [
            "Doc Brown invents time travel after slipping off a toilet seat and hitting his head, envisioning the flux capacitor.",
            "Requires exactly 1.21 gigawatts of electricity and a speed of 88 miles per hour.",
            "Marty McFly plays 'Johnny B. Goode' on electric guitar at the Enchantment Under the Sea dance."
        ],
        "cryptic_clue": "A gull-wing steel steed struck by clock tower lightning sends Calvin Klein on a hoverboard into twin pines.",
        "letter_hint": "B _ _ _   t _   t _ _   F _ _ _ _ _",
        "fun_fact": "In early drafts of the script, the time machine was not a DeLorean car at all, but rather an old lead-lined refrigerator!"
    },
    {
        "id": "movies_09",
        "category": "movies",
        "name": "Avengers: Endgame",
        "aliases": ["avengers endgame", "endgame"],
        "difficulty": "easy",
        "year": 2019,
        "director": "Russo Brothers",
        "actor": "Robert Downey Jr.",
        "rated": "PG-13",
        "genres": ["Action", "Sci-Fi"],
        "studio": "Marvel Studios",
        "poster_theme": {
            "bg1": "#170b2b",
            "bg2": "#3b1c71",
            "accent": "#c084fc",
            "icon": "🧤",
            "scene": "infinity_portals",
            "subtitle": "Whatever It Takes"
        },
        "tips": [
            "Set five years after half of all life in the universe was snapped into dust.",
            "Heroes pull off a 'Time Heist' through the Quantum Realm to collect six Infinity Stones.",
            "Features Captain America wielding Mjolnir and saying 'Avengers... Assemble!'"
        ],
        "normal_clue": "Earth's Mightiest Heroes travel through time to collect the Infinity Stones and undo Thanos's devastating snap.",
        "progressive_clues": [
            "Begins five years after half of all living creatures in the universe vanished into dust.",
            "Heroes use Pym Particles for a 'Time Heist' across New York, Asgard, Morag, and Vormir.",
            "Climaxes with portals opening across a ruined battlefield and the line 'I am Iron Man.'"
        ],
        "cryptic_clue": "Six cosmic gems borrowed from yesteryear mend a halved cosmos at the cost of a billionaire's final snap.",
        "letter_hint": "A _ _ _ _ _ _ _ :   E _ _ _ _ _ _",
        "fun_fact": "The line 'I love you 3000' was inspired by what Robert Downey Jr.'s real-life children used to say to him!"
    },
    {
        "id": "movies_10",
        "category": "movies",
        "name": "Avatar",
        "aliases": ["avatar 2009", "james cameron avatar"],
        "difficulty": "easy",
        "year": 2009,
        "director": "James Cameron",
        "actor": "Sam Worthington",
        "rated": "PG-13",
        "genres": ["Sci-Fi", "Adventure"],
        "studio": "20th Century Fox",
        "poster_theme": {
            "bg1": "#041f2e",
            "bg2": "#0c4a6e",
            "accent": "#2dd4bf",
            "icon": "🌿",
            "scene": "pandora_forest",
            "subtitle": "Welcome To Pandora"
        },
        "tips": [
            "Set on the bioluminescent alien moon of Pandora in the 22nd century.",
            "A paraplegic Marine inhabits a genetically engineered 10-foot-tall blue Na'vi body.",
            "The highest-grossing movie in box office history, directed by James Cameron."
        ],
        "normal_clue": "A paraplegic Marine on the alien moon Pandora is torn between following corporate orders and protecting the blue-skinned Na'vi.",
        "progressive_clues": [
            "Humans mine a priceless superconductor mineral called Unobtanium beneath Hometree.",
            "Jake Sully bonds with a winged mountain banshee (Ikran) and falls in love with Neytiri.",
            "Revolutionized 3D cinema in 2009 and became the highest-grossing film of all time."
        ],
        "cryptic_clue": "Neural braids link a wheelchair soldier to a ten-foot azure body beneath glowing bioluminescent willow roots.",
        "letter_hint": "A _ _ _ _ _",
        "fun_fact": "James Cameron waited over 10 years after writing the treatment in 1994 for motion-capture technology to become advanced enough to make the film!"
    },
    {
        "id": "movies_11",
        "category": "movies",
        "name": "The Lion King",
        "aliases": ["lion king", "the lion king 1994"],
        "difficulty": "easy",
        "year": 1994,
        "director": "Roger Allers",
        "actor": "Matthew Broderick",
        "rated": "G",
        "genres": ["Animation", "Family"],
        "studio": "Walt Disney Pictures",
        "poster_theme": {
            "bg1": "#3b1106",
            "bg2": "#7c2d12",
            "accent": "#facc15",
            "icon": "🦁",
            "scene": "pride_rock",
            "subtitle": "Circle Of Life"
        },
        "tips": [
            "Opens with a sunrise over the African savanna as animals gather at Pride Rock.",
            "A young cub grows up in exile with a meerkat and warthog learning 'Hakuna Matata'.",
            "Inspired by Shakespeare's Hamlet, featuring the treacherous uncle Scar."
        ],
        "normal_clue": "A young lion prince flees his kingdom after his father Mufasa is murdered by his treacherous uncle Scar.",
        "progressive_clues": [
            "Raised in the jungle on a diet of bugs by Timon and Pumbaa under the motto 'Hakuna Matata'.",
            "Guided by the mandrill shaman Rafiki and the spirit of his father in the starry night sky.",
            "Simba returns to Pride Rock to reclaim his rightful place in the Circle of Life."
        ],
        "cryptic_clue": "Wildebeest hooves echo in a gorge as a banished cub trades royal duty for grubs before reclaiming the savanna throne.",
        "letter_hint": "T _ _   L _ _ _   K _ _ _",
        "fun_fact": "The lion roars heard in the film were actually performed by voice actor Frank Welker using a metal trash can for resonance!"
    },
    {
        "id": "movies_12",
        "category": "movies",
        "name": "Toy Story",
        "aliases": ["toy story 1995"],
        "difficulty": "easy",
        "year": 1995,
        "director": "John Lasseter",
        "actor": "Tom Hanks",
        "rated": "G",
        "genres": ["Animation", "Family"],
        "studio": "Walt Disney Pictures",
        "poster_theme": {
            "bg1": "#0c2d57",
            "bg2": "#1d4ed8",
            "accent": "#fde047",
            "icon": "🤠",
            "scene": "clouds_star",
            "subtitle": "To Infinity And Beyond"
        },
        "tips": [
            "The very first feature-length film in history made entirely with computer animation.",
            "An old-fashioned pull-string cowboy doll gets jealous of a shiny new space ranger toy.",
            "Both toys have their owner 'ANDY' written on the bottom of their boot."
        ],
        "normal_clue": "A pull-string cowboy doll becomes deeply jealous when a flashy new space ranger action figure becomes their owner Andy's favorite toy.",
        "progressive_clues": [
            "The toys freeze lifelessly whenever a human enters the bedroom.",
            "Woody and Buzz Lightyear get stranded at Pizza Planet and captured by the toy-torturing neighbor Sid.",
            "First fully computer-animated feature film produced by Pixar Animation Studios."
        ],
        "cryptic_clue": "Painted boot soles bear a boy's name while a delusional plastic cosmonaut learns that falling with style beats flying.",
        "letter_hint": "T _ _   S _ _ _ _",
        "fun_fact": "Billy Crystal originally turned down the role of Buzz Lightyear, which he later called the biggest regret of his career!"
    },
    {
        "id": "movies_13",
        "category": "movies",
        "name": "Forrest Gump",
        "aliases": ["forrest gump 1994"],
        "difficulty": "medium",
        "year": 1994,
        "director": "Robert Zemeckis",
        "actor": "Tom Hanks",
        "rated": "PG-13",
        "genres": ["Drama", "Romance"],
        "studio": "Paramount Pictures",
        "poster_theme": {
            "bg1": "#112233",
            "bg2": "#2b4c6f",
            "accent": "#f8fafc",
            "icon": "🪶",
            "scene": "feather_bench",
            "subtitle": "Box Of Chocolates"
        },
        "tips": [
            "The narrator tells his life story to strangers while sitting on a bus stop bench in Savannah.",
            "Famous quote: 'Mama always said life was like a box of chocolates.'",
            "He becomes a college football star, Vietnam War hero, ping-pong champion, and shrimp boat captain."
        ],
        "normal_clue": "A kind-hearted Alabama man witnesses and unwittingly influences defining historical events of the 20th century from a bus stop bench.",
        "progressive_clues": [
            "Tells strangers that 'Life was like a box of chocolates. You never know what you're gonna get.'",
            "Becomes an All-American football player, ping-pong diplomat, and founder of Bubba Gump Shrimp.",
            "Spends decades devoted to his childhood friend and lifelong love, Jenny."
        ],
        "cryptic_clue": "A floating white feather lands by muddy running shoes on a Georgia bench as history bends around a simple man's sprint.",
        "letter_hint": "F _ _ _ _ _ _   G _ _ _",
        "fun_fact": "Tom Hanks was not paid a traditional salary for the film; instead he took a percentage of the box office gross, earning over $60 million!"
    },
    {
        "id": "movies_14",
        "category": "movies",
        "name": "The Shawshank Redemption",
        "aliases": ["shawshank redemption", "shawshank"],
        "difficulty": "medium",
        "year": 1994,
        "director": "Frank Darabont",
        "actor": "Morgan Freeman",
        "rated": "R",
        "genres": ["Drama", "Crime"],
        "studio": "Columbia Pictures",
        "poster_theme": {
            "bg1": "#0f172a",
            "bg2": "#334155",
            "accent": "#fbbf24",
            "icon": "🔨",
            "scene": "prison_rain",
            "subtitle": "Fear Can Hold You Prisoner"
        },
        "tips": [
            "A wrongful murder conviction sends banker Andy Dufresne to a Maine state penitentiary.",
            "A small rock hammer is hidden inside a Bible and a wall poster covers a secret tunnel.",
            "Number 1 highest-rated movie on IMDb's Top 250 list for decades."
        ],
        "normal_clue": "A soft-spoken banker wrongfully convicted of murder forms a lifelong friendship with a fellow inmate over two decades in prison.",
        "progressive_clues": [
            "Andy Dufresne requests a small rock hammer and a large poster of Rita Hayworth from prison smuggler Red.",
            "Plays an Italian opera record over the prison PA system, locking the guards out of the warden's office.",
            "Crawls through five hundred yards of foul-smelling sewage pipe to freedom in Zihuatanejo."
        ],
        "cryptic_clue": "Behind pin-up paper, a tiny geologist's pick carves nineteen years of patient liberty toward a Mexican Pacific beach.",
        "letter_hint": "T _ _   S _ _ _ _ _ _ _ _   R _ _ _ _ _ _ _ _ _",
        "fun_fact": "Based on Stephen King's novella 'Rita Hayworth and Shawshank Redemption', which King sold the film rights to for $5,000—and he never even cashed the check!"
    },
    {
        "id": "movies_15",
        "category": "movies",
        "name": "Gladiator",
        "aliases": ["gladiator 2000"],
        "difficulty": "medium",
        "year": 2000,
        "director": "Ridley Scott",
        "actor": "Russell Crowe",
        "rated": "R",
        "genres": ["Action", "Drama"],
        "studio": "Universal Pictures",
        "poster_theme": {
            "bg1": "#291507",
            "bg2": "#5c2d0c",
            "accent": "#f59e0b",
            "icon": "⚔️",
            "scene": "colosseum_arena",
            "subtitle": "Are You Not Entertained?"
        },
        "tips": [
            "A betrayed Roman general is forced into slavery and fights in the Colosseum arena.",
            "Shouts to the crowd: 'Are you not entertained?!'",
            "Seeks vengeance against the corrupt Emperor Commodus who murdered his family."
        ],
        "normal_clue": "A betrayed Roman general is reduced to slavery and rises through the Colosseum ranks to avenge his murdered family and emperor.",
        "progressive_clues": [
            "Maximus Decimus Meridius rubs dirt in his palms before battle and dreams of Elysium's wheat fields.",
            "Roars to the bloodthirsty crowd: 'Are you not entertained?'",
            "Unmasks himself before Emperor Commodus on the sands of the Roman Colosseum."
        ],
        "cryptic_clue": "A Spaniard's helmet conceals Rome's true northern commander until bloodied sand meets golden wheat in the afterlife.",
        "letter_hint": "G _ _ _ _ _ _ _ _",
        "fun_fact": "Russell Crowe initially hated the famous 'My name is Maximus Decimus Meridius...' speech, calling it rubbish, yet insisted on delivering it with maximum gravitas!"
    },
    {
        "id": "movies_16",
        "category": "movies",
        "name": "Oppenheimer",
        "aliases": ["oppenheimer 2023"],
        "difficulty": "medium",
        "year": 2023,
        "director": "Christopher Nolan",
        "actor": "Cillian Murphy",
        "rated": "R",
        "genres": ["Biography", "Drama"],
        "studio": "Universal Pictures",
        "poster_theme": {
            "bg1": "#270e04",
            "bg2": "#6b2408",
            "accent": "#fb923c",
            "icon": "💥",
            "scene": "trinity_fire",
            "subtitle": "Destroyer Of Worlds"
        },
        "tips": [
            "Chronicles the secret Manhattan Project laboratory built in Los Alamos, New Mexico.",
            "Quotes the Bhagavad Gita: 'Now I am become Death, the destroyer of worlds.'",
            "Released on the same day as Barbie in July 2023, sparking the 'Barbenheimer' phenomenon."
        ],
        "normal_clue": "Theoretical physicist J. Robert Oppenheimer leads the secret Los Alamos laboratory to build the first atomic bomb during WWII.",
        "progressive_clues": [
            "Culminates in the tense desert countdown to the Trinity nuclear test in New Mexico.",
            "Haunted by the Hindu scripture quote: 'Now I am become Death, the destroyer of worlds.'",
            "Directed by Christopher Nolan, winning 7 Oscars including Best Picture and Best Actor for Cillian Murphy."
        ],
        "cryptic_clue": "Marbles fill a glass bowl in the desert while silent blinding fire precedes a thunderclap that haunts a porkpie-hatted physicist.",
        "letter_hint": "O _ _ _ _ _ _ _ _ _ _",
        "fun_fact": "Christopher Nolan refused to use CGI for the Trinity nuclear explosion, instead recreating the fireball with practical pyrotechnics!"
    },
    {
        "id": "movies_17",
        "category": "movies",
        "name": "The Godfather",
        "aliases": ["godfather", "the godfather 1972"],
        "difficulty": "hard",
        "year": 1972,
        "director": "Francis Ford Coppola",
        "actor": "Marlon Brando",
        "rated": "R",
        "genres": ["Crime", "Drama"],
        "studio": "Paramount Pictures",
        "poster_theme": {
            "bg1": "#0a0a0a",
            "bg2": "#261717",
            "accent": "#ef4444",
            "icon": "🌹",
            "scene": "puppet_rose",
            "subtitle": "An Offer He Can't Refuse"
        },
        "tips": [
            "Opens at a lavish wedding as an aging Mafia patriarch strokes a cat in his dark study.",
            "Famous quote: 'I'm gonna make him an offer he can't refuse.'",
            "Follows war hero Michael Corleone's transformation into the ruthless new Don."
        ],
        "normal_clue": "The aging patriarch of an organized crime dynasty transfers control of his clandestine New York empire to his reluctant youngest son.",
        "progressive_clues": [
            "Don Vito Corleone strokes a cat during his daughter's wedding and promises 'an offer he can't refuse.'",
            "A Hollywood producer wakes up to find a severed horse's head in his silk bedsheets.",
            "Michael Corleone retrieves a hidden pistol behind a restaurant toilet tank and ascends to become the new Don."
        ],
        "cryptic_clue": "Puppeteer strings above a tuxedo red rose; oranges herald gunfire as a war hero closes the office door on his wife.",
        "letter_hint": "T _ _   G _ _ _ _ _ _ _ _",
        "fun_fact": "The cat held by Marlon Brando in the opening scene was an unscripted stray cat that Francis Ford Coppola found wandering on the studio lot!"
    },
    {
        "id": "movies_18",
        "category": "movies",
        "name": "Star Wars: A New Hope",
        "aliases": ["star wars", "a new hope", "star wars episode iv"],
        "difficulty": "easy",
        "year": 1977,
        "director": "George Lucas",
        "actor": "Mark Hamill",
        "rated": "PG",
        "genres": ["Sci-Fi", "Adventure"],
        "studio": "20th Century Fox",
        "poster_theme": {
            "bg1": "#090a19",
            "bg2": "#1e1b4b",
            "accent": "#fde047",
            "icon": "⚔️",
            "scene": "twin_suns",
            "subtitle": "A Galaxy Far, Far Away"
        },
        "tips": [
            "A farm boy on the desert planet Tatooine gazes out at a binary twin-sun sunset.",
            "Princess Leia hides secret battle station blueprints inside the droid R2-D2.",
            "Culminates in a trench run assault to destroy the moon-sized Death Star."
        ],
        "normal_clue": "Luke Skywalker joins a Jedi Master, a cocky smuggler, and two droids to rescue a rebel princess and destroy the Death Star.",
        "progressive_clues": [
            "Begins with a yellow scrolling text crawl and two droids escaping to the desert planet Tatooine.",
            "Han Solo and Chewbacca pilot the Millennium Falcon out of Mos Eisley spaceport.",
            "Obi-Wan Kenobi teaches Luke to trust the Force during the final trench run against the Empire's battle station."
        ],
        "cryptic_clue": "Twin suns set on a moisture farm before an ancient laser sword and a tin astromech guide a torpedo down an exhaust port.",
        "letter_hint": "S _ _ _   W _ _ _ :   A   N _ _   H _ _ _",
        "fun_fact": "Almost every major studio turned down George Lucas's script before 20th Century Fox took a chance on it!"
    },
    {
        "id": "movies_19",
        "category": "movies",
        "name": "Jaws",
        "aliases": ["jaws 1975"],
        "difficulty": "hard",
        "year": 1975,
        "director": "Steven Spielberg",
        "actor": "Roy Scheider",
        "rated": "PG",
        "genres": ["Adventure", "Thriller"],
        "studio": "Universal Pictures",
        "poster_theme": {
            "bg1": "#04182b",
            "bg2": "#075985",
            "accent": "#ef4444",
            "icon": "🦈",
            "scene": "shark_fin",
            "subtitle": "Don't Go In The Water"
        },
        "tips": [
            "Famous two-note suspenseful cello theme by composer John Williams.",
            "Delivering the classic line: 'You're gonna need a bigger boat.'",
            "A giant man-eating great white shark terrorizes the summer beach town of Amity Island."
        ],
        "normal_clue": "A police chief, a marine biologist, and a grizzled shark hunter set out to stop a giant great white shark terrorizing Amity Island.",
        "progressive_clues": [
            "John Williams's two-note menacing bass score signals the unseen predator's approach.",
            "Chief Brody backs away slowly after seeing the beast, muttering: 'You're gonna need a bigger boat.'",
            "Directed by a 27-year-old Steven Spielberg, becoming the first summer blockbuster in history."
        ],
        "cryptic_clue": "Three yellow barrels fail to hold twenty-five feet of cartilaginous terror beneath Amity's Fourth of July waves.",
        "letter_hint": "J _ _ _",
        "fun_fact": "The mechanical sharks (nicknamed 'Bruce') malfunctioned constantly in saltwater, forcing Spielberg to suggest the shark through music and POV shots!"
    },
    {
        "id": "movies_20",
        "category": "movies",
        "name": "Dune: Part Two",
        "aliases": ["dune", "dune part two", "dune 2"],
        "difficulty": "hard",
        "year": 2024,
        "director": "Denis Villeneuve",
        "actor": "Timothée Chalamet",
        "rated": "PG-13",
        "genres": ["Sci-Fi", "Adventure"],
        "studio": "Warner Bros.",
        "poster_theme": {
            "bg1": "#291404",
            "bg2": "#78350f",
            "accent": "#f59e0b",
            "icon": "🏜️",
            "scene": "sandworm_desert",
            "subtitle": "Long Live The Fighters"
        },
        "tips": [
            "Set on the desert planet Arrakis, the only source of the consciousness-expanding Spice Melange.",
            "Warriors with glowing blue-within-blue eyes use thumpers to summon and ride giant sandworms.",
            "Paul Atreides fulfills the Fremen prophecy of Lisan al-Gaib."
        ],
        "normal_clue": "Paul Atreides unites with Chani and the Fremen of Arrakis on a warpath of revenge against the conspirators who destroyed his family.",
        "progressive_clues": [
            "Uses a rhythmic thumper in the deep desert dunes to summon and ride a colossal sandworm (Shai-Hulud).",
            "Drinks the lethal blue Water of Life to unlock genetic memories and fulfill the Lisan al-Gaib prophecy.",
            "Directed by Denis Villeneuve and starring Timothée Chalamet and Zendaya."
        ],
        "cryptic_clue": "Blue-within-blue eyes hooks the scales of a desert leviathan where cinnamon spice rules galactic houses.",
        "letter_hint": "D _ _ _ :   P _ _ _   T _ _",
        "fun_fact": "Director Denis Villeneuve worked with linguists to create a complete, speakable Fremen language specifically for the films!"
    },
    {
        "id": "movies_21",
        "category": "movies",
        "name": "Spider-Man: Into the Spider-Verse",
        "aliases": ["into the spider-verse", "spider-verse", "spiderman into the spiderverse"],
        "difficulty": "medium",
        "year": 2018,
        "director": "Bob Persichetti",
        "actor": "Shameik Moore",
        "rated": "PG",
        "genres": ["Animation", "Action"],
        "studio": "Columbia Pictures",
        "poster_theme": {
            "bg1": "#1a0726",
            "bg2": "#be123c",
            "accent": "#38bdf8",
            "icon": "🕷️",
            "scene": "spider_verse",
            "subtitle": "Anyone Can Wear The Mask"
        },
        "tips": [
            "Brooklyn teenager Miles Morales is bitten by a glitching radioactive spider (#42).",
            "Kingpin's super-collider pulls web-slingers from alternate dimensions into one universe.",
            "Features comic-book halftone dots, Ben-Day shading, and the song 'Sunflower'."
        ],
        "normal_clue": "Teenager Miles Morales becomes the new Spider-Man of his reality and crosses paths with five counterparts from other dimensions.",
        "progressive_clues": [
            "Blends 3D computer animation with hand-drawn comic book panels, halftone dots, and action word bubbles.",
            "Miles teams up with Peter B. Parker, Gwen Stacy, Spider-Man Noir, Peni Parker, and Spider-Ham.",
            "Features an iconic upside-down 'Leap of Faith' off a Brooklyn skyscraper to the song 'What's Up Danger'."
        ],
        "cryptic_clue": "Halftone ink dots fracture Brooklyn's skyline as six arachnid totems collide around a grief-stricken crime boss's collider.",
        "letter_hint": "S _ _ _ _ _ - M _ _ :   I _ _ _   t _ _   S _ _ _ _ _ - V _ _ _ _",
        "fun_fact": "Miles Morales is animated at 12 frames per second ('on twos') while he is clumsy at the start, and levels up to smooth 24 frames per second once he masters his powers!"
    },
    {
        "id": "movies_22",
        "category": "movies",
        "name": "Fight Club",
        "aliases": ["fight club 1999"],
        "difficulty": "hard",
        "year": 1999,
        "director": "David Fincher",
        "actor": "Brad Pitt",
        "rated": "R",
        "genres": ["Drama", "Thriller"],
        "studio": "20th Century Fox",
        "poster_theme": {
            "bg1": "#1f0b18",
            "bg2": "#4a153b",
            "accent": "#f472b6",
            "icon": "🧼",
            "scene": "pink_soap",
            "subtitle": "First Rule: Do Not Talk"
        },
        "tips": [
            "An insomniac office worker meets a charismatic soap salesman named Tyler Durden on an airplane.",
            "Famous first rule: 'You do not talk about...' this underground basement club.",
            "Features a shocking twist about the narrator and Tyler Durden's true identity."
        ],
        "normal_clue": "An insomniac office worker and a devil-may-care soap maker form an underground bare-knuckle club that evolves into something much more.",
        "progressive_clues": [
            "The first rule and second rule of the basement gathering both strictly forbid ever talking about it.",
            "Tyler Durden manufactures luxury pink bars of soap for the Paper Street Soap Company.",
            "Reveals in a mind-bending twist that the narrator and Tyler Durden are the exact same person."
        ],
        "cryptic_clue": "Pink fat-rendered soap bars fund Project Mayhem while a sleepless narrator punches his own reflection in a tavern cellar.",
        "letter_hint": "F _ _ _ _   C _ _ _",
        "fun_fact": "Director David Fincher hid a Starbucks coffee cup in almost every single scene of the movie as a commentary on consumer culture!"
    },
    {
        "id": "movies_23",
        "category": "movies",
        "name": "The Wolf of Wall Street",
        "aliases": ["the wolf of wall street", "wolf of wall street"],
        "difficulty": "hard",
        "year": 2013,
        "director": "Martin Scorsese",
        "actor": "Leonardo DiCaprio",
        "rated": "R",
        "genres": ["Biography", "Crime"],
        "studio": "Paramount Pictures",
        "poster_theme": {
            "bg1": "#1c1917",
            "bg2": "#422006",
            "accent": "#eab308",
            "icon": "📈",
            "scene": "wall_street",
            "subtitle": "Sell Me This Pen"
        },
        "tips": [
            "Based on the true rise and fall of Long Island penny-stock broker Jordan Belfort.",
            "Features chest-thumping humming at lunch and the challenge: 'Sell me this pen.'",
            "Fifth collaboration between director Martin Scorsese and star Leonardo DiCaprio."
        ],
        "normal_clue": "Based on the true story of Jordan Belfort, from his rise to a wealthy stock-broker living the high life to his fall involving crime and the FBI.",
        "progressive_clues": [
            "Founds the boiler-room brokerage firm Stratton Oakmont on Long Island.",
            "Features Matthew McConaughey thumping his chest at lunch and the famous challenge: 'Sell me this pen.'",
            "Directed by Martin Scorsese and starring Leonardo DiCaprio and Margot Robbie."
        ],
        "cryptic_clue": "Penny stocks fund yacht debauchery until Swiss bankers and FBI wires bring down Long Island's loudest microphone speech.",
        "letter_hint": "T _ _   W _ _ _   o _   W _ _ _   S _ _ _ _ _",
        "fun_fact": "The chest-thumping chant Matthew McConaughey performs was actually his real-life vocal warm-up routine before takes, which Leonardo DiCaprio asked to put in the movie!"
    },
    {
        "id": "movies_24",
        "category": "movies",
        "name": "Mad Max: Fury Road",
        "aliases": ["mad max fury road", "mad max", "fury road"],
        "difficulty": "insane",
        "year": 2015,
        "director": "George Miller",
        "actor": "Tom Hardy",
        "rated": "R",
        "genres": ["Action", "Sci-Fi"],
        "studio": "Warner Bros.",
        "poster_theme": {
            "bg1": "#331403",
            "bg2": "#9a3412",
            "accent": "#f97316",
            "icon": "🔥",
            "scene": "desert_rig",
            "subtitle": "What A Lovely Day"
        },
        "tips": [
            "A high-octane chase across a post-apocalyptic desert wasteland aboard an armored War Rig.",
            "Features a blind guitarist (the Doof Warrior) playing a flame-throwing electric guitar on a truck.",
            "War Boys spray silver chrome paint on their mouths and shout 'Witness me!'"
        ],
        "normal_clue": "In a post-apocalyptic wasteland, a woman rebels against a tyrannical ruler in search for her homeland with the aid of a drifter named Max.",
        "progressive_clues": [
            "Imperator Furiosa drives an armored War Rig across the desert to rescue Immortan Joe's five wives.",
            "War Boys spray chrome on their teeth shouting 'Witness me!' while a blind guitarist shoots flames from his instrument.",
            "Starring Tom Hardy and Charlize Theron, winning 6 Academy Awards."
        ],
        "cryptic_clue": "Chrome-sprayed mouths chase a tanker toward a vanished green place to the roar of a bungee-mounted flamethrower guitar.",
        "letter_hint": "M _ _   M _ _ :   F _ _ _   R _ _ _",
        "fun_fact": "Over 80% of the visual effects in Mad Max: Fury Road were real practical stunts, including the working flame-throwing guitar!"
    },

    # --- SUPERHEROES ---
    {
        "id": "superheroes_01",
        "category": "superheroes",
        "name": "Spider-Man",
        "aliases": ["spiderman", "peter parker", "web slinger", "wall crawler"],
        "difficulty": "easy",
        "normal_clue": "Bitten by a radioactive spider, this Queens teenager swings between skyscrapers protecting New York City.",
        "progressive_clues": [
            "Lives with Aunt May and learned the tragic lesson: 'With great power comes great responsibility.'",
            "Invents mechanical web-shooters, works as a freelance photographer for the Daily Bugle, and possesses spider-sense.",
            "Peter Parker faces villains like Green Goblin, Doc Ock, and Venom in a red-and-blue suit."
        ],
        "cryptic_clue": "An arachnid prick in Queens yields wall-crawling acrobatics driven by Uncle Ben's dying ethical imperative.",
        "letter_hint": "S _ _ _ _ _ - M _ _",
        "fun_fact": "Stan Lee's publisher originally rejected Spider-Man, insisting that people hate spiders and teenagers could only be sidekicks!"
    },
    {
        "id": "superheroes_02",
        "category": "superheroes",
        "name": "Batman",
        "aliases": ["bruce wayne", "the dark knight", "caped crusader"],
        "difficulty": "easy",
        "normal_clue": "A billionaire vigilante who patrols Gotham City by night without superpowers, relying on genius intellect and martial arts.",
        "progressive_clues": [
            "Witnessed the murder of his parents, Thomas and Martha Wayne, in Crime Alley as a child.",
            "Operates out of a subterranean cave beneath Wayne Manor with trusty butler Alfred Pennyworth.",
            "Uses the Batarang, Batmobile, and the signal in the sky against rogues like the Joker, Riddler, and Penguin."
        ],
        "cryptic_clue": "Orphaned wealth shrouded in cowl and cape, weaponizing the fear of cave-dwelling winged mammals against Gotham's underworld.",
        "letter_hint": "B _ _ _ _ _",
        "fun_fact": "Batman does not kill or use firearms, a moral code introduced in 1940 after early issues depicted him carrying a handgun."
    },
    {
        "id": "superheroes_03",
        "category": "superheroes",
        "name": "Iron Man",
        "aliases": ["tony stark", "stark"],
        "difficulty": "easy",
        "normal_clue": "Genius, billionaire, playboy, philanthropist who builds a high-tech powered armor suit powered by an arc reactor.",
        "progressive_clues": [
            "Suffered a shrapnel chest injury in captivity before forging the Mark I suit in a cave with a box of scraps.",
            "Assisted by AI assistants JARVIS and Friday while leading Stark Industries.",
            "Tony Stark kicked off the Marvel Cinematic Universe in 2008 with the famous line: 'I am Iron Man.'"
        ],
        "cryptic_clue": "A glowing chest magnet fuels hot-rod red and gold alloy plate, forged in an Afghan grotto by an arrogant weapons magnate.",
        "letter_hint": "I _ _ _   M _ _",
        "fun_fact": "Stan Lee created Tony Stark as a challenge to make readers fall in love with a wealthy military industrialist during the height of the Cold War."
    },
    {
        "id": "superheroes_04",
        "category": "superheroes",
        "name": "Wonder Woman",
        "aliases": ["diana prince", "diana of themyscira"],
        "difficulty": "medium",
        "normal_clue": "Amazonian warrior princess of Themyscira who wields the Lasso of Truth and indestructible bracelets.",
        "progressive_clues": [
            "Daughter of Queen Hippolyta, sculpted from clay and blessed by the Olympian gods.",
            "Leaves Paradise Island alongside pilot Steve Trevor to bring peace to Man's World.",
            "Founds the Justice League alongside Superman and Batman, wielding a golden glowing lasso."
        ],
        "cryptic_clue": "Clay shaped on hidden shores, bearing bullet-deflecting silver bands and a golden rope that compels confession.",
        "letter_hint": "W _ _ _ _ _   W _ _ _ _",
        "fun_fact": "Her creator, William Moulton Marston, was also one of the early inventors of the systolic blood pressure lie detector test!"
    },
    {
        "id": "superheroes_05",
        "category": "superheroes",
        "name": "Wolverine",
        "aliases": ["logan", "james howlett"],
        "difficulty": "medium",
        "normal_clue": "A gruff Canadian mutant with an accelerated healing factor, animalistic senses, and retractable adamantium claws.",
        "progressive_clues": [
            "Survived the brutal Weapon X military experiment that coated his entire skeletal structure in unbreakable metal.",
            "Longtime core member of the X-Men who smokes cigars and frequently calls people 'bub'.",
            "Portrayed by Hugh Jackman for over two decades across numerous films."
        ],
        "cryptic_clue": "Unbreakable bone knives erupt through knuckles; centuries of wars survived beneath yellow spandex and mutton chops.",
        "letter_hint": "W _ _ _ _ _ _ _ _",
        "fun_fact": "Wolverine's first appearance in comic books was actually as an antagonist fighting the Incredible Hulk in 1974!"
    },
    {
        "id": "superheroes_06",
        "category": "superheroes",
        "name": "Captain America",
        "aliases": ["steve rogers", "cap", "first avenger"],
        "difficulty": "medium",
        "normal_clue": "A frail WWII Brooklyn recruit transformed into a super-soldier who wields an indestructible vibranium shield.",
        "progressive_clues": [
            "Injected with Dr. Erskine's Super-Soldier Serum during World War II to fight Hydra and Red Skull.",
            "Frozen in Arctic ice for nearly 70 years before waking up in the modern century.",
            "Steve Rogers leads the Avengers with the catchphrase: 'I can do this all day.'"
        ],
        "cryptic_clue": "Brooklyn grit amplified by serum, bearing a star-spangled disc of Wakandan metal across seven frozen decades.",
        "letter_hint": "C _ _ _ _ _ _   A _ _ _ _ _ _",
        "fun_fact": "Captain America #1 (1941), showing him punching Adolf Hitler on the cover, was published nine months before the US even entered World War II!"
    },
    {
        "id": "superheroes_07",
        "category": "superheroes",
        "name": "Deadpool",
        "aliases": ["wade wilson", "merc with a mouth"],
        "difficulty": "hard",
        "normal_clue": "The regeneratively gifted 'Merc with a Mouth' who constantly breaks the fourth wall and loves chimichangas.",
        "progressive_clues": [
            "Former special forces operative Wade Wilson who underwent a rogue mutation treatment for terminal cancer.",
            "Wields dual katanas and twin pistols while directly addressing the audience and comic readers.",
            "Wears a red-and-black suit so enemies can't see him bleed."
        ],
        "cryptic_clue": "Scarred regenerator in crimson spandex who chats with the camera between katana strikes and Mexican fried burritos.",
        "letter_hint": "D _ _ _ _ _ _ _",
        "fun_fact": "Deadpool's name comes from a betting pool ('the dead pool') run by inmates at the brutal lab where he was mutated!"
    },
    {
        "id": "superheroes_08",
        "category": "superheroes",
        "name": "Doctor Strange",
        "aliases": ["stephen strange", "sorcerer supreme", "dr strange"],
        "difficulty": "insane",
        "normal_clue": "A brilliant but arrogant neurosurgeon who loses the use of his hands and becomes the Sorcerer Supreme.",
        "progressive_clues": [
            "Travels to Kamar-Taj in Kathmandu after a devastating car crash ruins his surgical career.",
            "Wears the sentient Cloak of Levitation and guards the New York Sanctum Sanctorum.",
            "Wields the Eye of Agamotto and bargains with Dormammu in the Dark Dimension."
        ],
        "cryptic_clue": "Shattered surgeon's fingers trace fiery mandalas in the air, looping time against a cosmic tyrant from Bleecker Street.",
        "letter_hint": "D _ _ _ _ _   S _ _ _ _ _ _",
        "fun_fact": "The address of his Sanctum Sanctorum, 177A Bleecker Street in Greenwich Village, was the real-life apartment address of comic writers Roy Thomas and Gary Friedrich!"
    },

    # --- GAMES ---
    {
        "id": "games_01",
        "category": "games",
        "name": "Minecraft",
        "aliases": ["mine craft"],
        "difficulty": "easy",
        "normal_clue": "The best-selling sandbox game in history where players mine blocks, craft tools, and survive exploding green Creepers.",
        "progressive_clues": [
            "Punch trees for wood on your first day before skeletons and zombies spawn at nightfall.",
            "Build Nether portals out of obsidian to eventually slay the Ender Dragon in The End.",
            "Created by Notch and Mojang, featuring Steve, Alex, and blocky 3D voxel worlds."
        ],
        "cryptic_clue": "Cubic geometry where punching timber yields diamond pickaxes and a silent green quadruped hisses behind your back.",
        "letter_hint": "M _ _ _ _ _ _ _ _",
        "fun_fact": "The iconic Creeper was created by accident when creator Notch mixed up the height and length dimensions while coding a pig!"
    },
    {
        "id": "games_02",
        "category": "games",
        "name": "Super Mario Bros.",
        "aliases": ["super mario", "mario", "super mario bros"],
        "difficulty": "easy",
        "normal_clue": "Nintendo's flagship platformer featuring an Italian plumber who stomps Goombas and rescues Princess Peach from Bowser.",
        "progressive_clues": [
            "Eat Super Mushrooms to grow big, Fire Flowers to throw fireballs, and Super Stars for invincibility.",
            "Warp through green pipes across the Mushroom Kingdom alongside brother Luigi.",
            "Sorry, but our princess is in another castle!"
        ],
        "cryptic_clue": "Overalls dive down emerald plumbing as fungi grant stature to topple a spiked turtle king.",
        "letter_hint": "S _ _ _ _   M _ _ _ _   B _ _ _ .",
        "fun_fact": "Mario was originally named 'Jumpman' in 1981's Donkey Kong and was a carpenter, not a plumber!"
    },
    {
        "id": "games_03",
        "category": "games",
        "name": "The Legend of Zelda",
        "aliases": ["zelda", "legend of zelda", "breath of the wild", "ocarina of time"],
        "difficulty": "easy",
        "normal_clue": "Nintendo's action-adventure series where the green-tunic hero Link wields the Master Sword to save Hyrule and Princess Zelda.",
        "progressive_clues": [
            "Collect Rupees, smash clay pots, solve dungeon puzzles, and seek the golden Triforce of Courage.",
            "The hero is Link (not Zelda!), battling the dark warlord Ganondorf.",
            "Famous warning from an old man in a cave: 'It's dangerous to go alone! Take this.'"
        ],
        "cryptic_clue": "Three golden triangles govern Power, Wisdom, and Courage while a silent elfin swordsman shatters pottery across Hyrule.",
        "letter_hint": "T _ _   L _ _ _ _ _   o _   Z _ _ _ _",
        "fun_fact": "Creator Shigeru Miyamoto named Princess Zelda after Zelda Fitzgerald, the famous wife of author F. Scott Fitzgerald!"
    },
    {
        "id": "games_04",
        "category": "games",
        "name": "Grand Theft Auto V",
        "aliases": ["gta v", "gta 5", "grand theft auto 5", "grand theft auto"],
        "difficulty": "medium",
        "normal_clue": "Rockstar's blockbuster open-world crime epic set in Los Santos following three playable criminals: Michael, Franklin, and Trevor.",
        "progressive_clues": [
            "Set in a sprawling satirical recreation of Southern California called San Andreas.",
            "Switch in real time between a retired bank robber, a street hustler, and an unhinged desert maniac.",
            "Pull off high-stakes heists while evading a five-star police wanted level."
        ],
        "cryptic_clue": "Three antiheroes converge in sun-soaked Los Santos to rob federal vaults beneath five flashing police stars.",
        "letter_hint": "G _ _ _ _   T _ _ _ _   A _ _ _   V",
        "fun_fact": "Grand Theft Auto V generated over $1 billion in sales within just three days of release, faster than any entertainment product in history!"
    },
    {
        "id": "games_05",
        "category": "games",
        "name": "Pac-Man",
        "aliases": ["pacman", "pac man"],
        "difficulty": "medium",
        "normal_clue": "The classic 1980 arcade game where a yellow circle chomps dots through a dark maze while evading four colorful ghosts.",
        "progressive_clues": [
            "Pursued through a neon labyrinth by Blinky, Pinky, Inky, and Clyde.",
            "Swallowing a flashing Power Pellet turns the ghosts blue and edible.",
            "Inspired by the shape of a pizza with a single slice removed."
        ],
        "cryptic_clue": "A missing pizza slice devours glowing pellets in a neon labyrinth while four spectral pursuers turn cobalt in terror.",
        "letter_hint": "P _ _ - M _ _",
        "fun_fact": "The original Japanese name was 'Puck-Man', which was changed to 'Pac-Man' in North America to prevent arcade vandals from scratching the 'P' into an 'F'!"
    },
    {
        "id": "games_06",
        "category": "games",
        "name": "Elden Ring",
        "aliases": ["elden ring 2022"],
        "difficulty": "hard",
        "normal_clue": "FromSoftware's dark fantasy action RPG created with George R.R. Martin, where a Tarnished warrior journeys through the Lands Between.",
        "progressive_clues": [
            "Guided by the grace of gold and accompanied by spectral steed Torrent and Melina.",
            "Battle demigod shardbearers like Starscourge Radahn and Malenia, Blade of Miquella.",
            "Won Game of the Year in 2022, famous for punishing boss fights beneath the glowing golden Erdtree."
        ],
        "cryptic_clue": "Beneath a colossal golden canopy, a maidenless exile rides a horned spirit steed to mend a shattered rune.",
        "letter_hint": "E _ _ _ _   R _ _ _",
        "fun_fact": "George R.R. Martin wrote the ancient mythology and demigod backstory set thousands of years before the game's events!"
    },
    {
        "id": "games_07",
        "category": "games",
        "name": "God of War",
        "aliases": ["kratos", "god of war ragnarok"],
        "difficulty": "hard",
        "normal_clue": "Action series following the Spartan warrior Kratos as he wages war against the Greek pantheon and later Norse gods.",
        "progressive_clues": [
            "Wields the fiery chained Blades of Chaos and later the frost-infused Leviathan Axe.",
            "Tricked by Ares into slaying his own family, turning his skin ash-white as the 'Ghost of Sparta'.",
            "Journeys across Midgard with his son Atreus ('Boy') to scatter his wife Faye's ashes upon the highest peak."
        ],
        "cryptic_clue": "Pale Spartan warrior bound by chained twin blades slaughters pantheons before teaching an archer boy restraint across the Nine Realms.",
        "letter_hint": "G _ _   o _   W _ _",
        "fun_fact": "Christopher Judge (voice of Kratos in 2018) won the Game Award for Best Performance and famously gave an 8-minute acceptance speech!"
    },
    {
        "id": "games_08",
        "category": "games",
        "name": "Among Us",
        "aliases": ["among us 2018"],
        "difficulty": "insane",
        "normal_clue": "A multiplayer social deduction party game where colorful bean crewmates attempt to identify parasitic Impostors.",
        "progressive_clues": [
            "Perform wires, swipe cards, and fuel engines aboard The Skeld spaceship.",
            "Hit the Emergency Meeting button or report dead bodies to discuss and vote out suspicious crewmates in chat.",
            "Popularized internet slang 'sus' and features vents used exclusively by shapeshifting alien infiltrators."
        ],
        "cryptic_clue": "Armless primary-colored cosmonauts squabble in cafeteria tribunals to eject the deceptive vent-crawling shapeshifter.",
        "letter_hint": "A _ _ _ _   U _",
        "fun_fact": "InnerSloth nearly canceled development on Among Us because the initial player count in 2018 averaged fewer than 30 concurrent players before exploding two years later!"
    },

    # --- CHARACTERS ---
    {
        "id": "characters_01",
        "category": "characters",
        "name": "Sherlock Holmes",
        "aliases": ["sherlock", "holmes"],
        "difficulty": "easy",
        "normal_clue": "Arthur Conan Doyle's famous consulting detective who resides at 221B Baker Street in London.",
        "progressive_clues": [
            "Employs brilliant observation and forensic deduction alongside Dr. John Watson.",
            "Wears a deerstalker hat, smokes a calabash pipe, and plays the violin.",
            "His brilliant intellectual arch-nemesis is the sinister Professor James Moriarty."
        ],
        "cryptic_clue": "Baker Street chemist with a deerstalker cap unravelling impossible crimes through microscopic cigar ash and cold logic.",
        "letter_hint": "S _ _ _ _ _ _ _   H _ _ _ _ _",
        "fun_fact": "Holmes never actually utters the exact phrase 'Elementary, my dear Watson' in any of Arthur Conan Doyle's four novels and 56 short stories!"
    },
    {
        "id": "characters_02",
        "category": "characters",
        "name": "Harry Potter",
        "aliases": ["the boy who lived", "potter"],
        "difficulty": "easy",
        "normal_clue": "The Boy Who Lived, a young wizard with a lightning bolt scar on his forehead who attends Hogwarts School.",
        "progressive_clues": [
            "Discovers on his 11th birthday from Hagrid: 'Yer a wizard, Harry.'",
            "Sorted into Gryffindor House, plays Seeker on the Quidditch team, and casts the Patronus Charm (a stag).",
            "Destined to defeat Lord Voldemort, who gave him his iconic scar as a baby."
        ],
        "cryptic_clue": "Round spectacles cover a jagged lightning blemish; an eleven-year-old orphan pulled from beneath the stairs by an owl's letter.",
        "letter_hint": "H _ _ _ _   P _ _ _ _ _",
        "fun_fact": "The lightning bolt scar was applied by makeup artists approximately 5,800 times on Daniel Radcliffe and his stunt doubles across the 8 films!"
    },
    {
        "id": "characters_03",
        "category": "characters",
        "name": "Darth Vader",
        "aliases": ["anakin skywalker", "vader", "lord vader"],
        "difficulty": "easy",
        "normal_clue": "The black-armored Sith Lord in Star Wars who breathes mechanically and serves Emperor Palpatine.",
        "progressive_clues": [
            "Formerly Anakin Skywalker, a heroic Jedi Knight seduced by the dark side of the Force.",
            "Wields a red lightsaber and uses the dark Force choke to execute failing imperial officers.",
            "Shocks Luke Skywalker in Cloud City with the revelation: 'No, I am your father.'"
        ],
        "cryptic_clue": "Obsidian respirator marching to an imperial brass march; severed limbs restored by chrome armor after burning beside lava rivers.",
        "letter_hint": "D _ _ _ _   V _ _ _ _",
        "fun_fact": "His iconic breathing sound was created by sound designer Ben Burtt breathing into a scuba diving regulator modified with a microphone!"
    },
    {
        "id": "characters_04",
        "category": "characters",
        "name": "Gandalf",
        "aliases": ["gandalf the grey", "gandalf the white", "mithrandir"],
        "difficulty": "medium",
        "normal_clue": "The wise wizard of Middle-earth who guides Frodo Baggins and the Fellowship of the Ring.",
        "progressive_clues": [
            "Known as the Grey Pilgrim who smokes pipe-weed and crafts spectacular fireworks for hobbit parties.",
            "Confronts the Balrog of Morgoth upon the Bridge of Khazad-dûm, shouting: 'You shall not pass!'",
            "Falls into shadow and returns reincarnated as the White Wizard at Fangorn Forest."
        ],
        "cryptic_clue": "Pointed hat, wooden staff, and ring of fire; reborn from gray ashes to white radiance to command the riders of Rohan.",
        "letter_hint": "G _ _ _ _ _ _",
        "fun_fact": "J.R.R. Tolkien took the name 'Gandalf' directly from the Old Norse poetic compilation known as the Poetic Edda!"
    },
    {
        "id": "characters_05",
        "category": "characters",
        "name": "James Bond",
        "aliases": ["agent 007", "007", "commander bond"],
        "difficulty": "medium",
        "normal_clue": "MI6's suave British secret agent with a license to kill, known by the code number 007.",
        "progressive_clues": [
            "Drinks a vodka martini: 'Shaken, not stirred.'",
            "Equipped with ingenious gadgets and an Aston Martin DB5 by Q Branch.",
            "Created by author Ian Fleming, battling global syndicates like SPECTRE."
        ],
        "cryptic_clue": "A Savile Row tuxedo concealing a Walther PPK, ordering olives drenched in shaken grain spirits under her majesty's secret license.",
        "letter_hint": "J _ _ _ _   B _ _ _",
        "fun_fact": "Ian Fleming named his character after an American ornithologist whose book 'Birds of the West Indies' was sitting on Fleming's desk, wanting the dullest name possible!"
    },
    {
        "id": "characters_06",
        "category": "characters",
        "name": "Katniss Everdeen",
        "aliases": ["the girl on fire", "mockingjay", "katniss"],
        "difficulty": "hard",
        "normal_clue": "The courageous archer from District 12 who volunteers as tribute to save her younger sister Prim in The Hunger Games.",
        "progressive_clues": [
            "Hunts with a bow and arrow in the woods of the Seam with her friend Gale Hawthorne.",
            "Wears a golden Mockingjay pin and earns the moniker 'The Girl on Fire' thanks to stylist Cinna.",
            "Sparks a rebellion against President Snow and the opulent Capitol of Panem."
        ],
        "cryptic_clue": "A sister's sacrifice ignites a flame-dressed archer whose whistle turns a mocking avian brooch into a revolution's battle standard.",
        "letter_hint": "K _ _ _ _ _ _   E _ _ _ _ _ _ _",
        "fun_fact": "Katniss is named after Sagittaria sagittifolia, an edible water plant also known as 'arrowhead'!"
    },
    {
        "id": "characters_07",
        "category": "characters",
        "name": "Pikachu",
        "aliases": ["pikachu pokemon", "pokemon pikachu"],
        "difficulty": "hard",
        "normal_clue": "The Electric-type Mouse Pokémon who serves as the worldwide mascot of the Pokémon franchise.",
        "progressive_clues": [
            "Features yellow fur, red electric cheek pouches, and a lightning bolt-shaped tail.",
            "Refuses to stay inside a Poké Ball, riding instead on the shoulder of trainer Ash Ketchum.",
            "Discharges electric sparks via Thunderbolt and evolves into Raichu using a Thunder Stone."
        ],
        "cryptic_clue": "Yellow rodent with cheeks charged with kilowatt fury, refusing capsule confines to ride on a Pallet Town boy's shoulder.",
        "letter_hint": "P _ _ _ _ _ _",
        "fun_fact": "The name comes from Japanese onomatopoeia: 'pika' (the sound an electric spark makes) and 'chu' (the sound a mouse makes)!"
    },
    {
        "id": "characters_08",
        "category": "characters",
        "name": "Jack Sparrow",
        "aliases": ["captain jack sparrow", "jack sparrow"],
        "difficulty": "insane",
        "normal_clue": "The eccentric, swaggering pirate captain of the Black Pearl who relies on wits, luck, and a compass that doesn't point north.",
        "progressive_clues": [
            "Always demands to be addressed as 'Captain', and frequently wonders: 'Why is the rum gone?'",
            "Barters with Davy Jones, outwits Hector Barbossa, and carries a single shot in his flintlock pistol.",
            "Brought to life by Johnny Depp with dreadlocks, eyeliner, and drunken stumble-swagger."
        ],
        "cryptic_clue": "Braided beard, gold teeth, and a needle pointing only toward desires of the heart while lamenting the mysterious vanishing of fermented cane syrup.",
        "letter_hint": "J _ _ _   S _ _ _ _ _ _",
        "fun_fact": "Disney executives initially panicked upon seeing Johnny Depp's early acting dailies, fearing he was playing the character drunk or crazy!"
    }
]

with open("data/questions.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2)

print(f"Successfully wrote {len(questions)} questions to data/questions.json")
