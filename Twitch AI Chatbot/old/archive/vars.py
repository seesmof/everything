import os

# enter your bot token
TOKEN = "2hak1ryy0hj4a2jpg4jjxwfazhppxx"

# enter your bot's nickname, without @
BOT_NICK = "piprly"

# enter a delay between messages. set to 20 seconds by default
DELAY = 20  # in seconds

# enter the channel names you want your bot to work in
WANTED_CHANNELS = [
    "seesmof",
    "PixelFedya",
    "k3ned1",
    "unjustfridgesmod",
]

# CAUTION: enter the users you don't want your bot to answer to. useful for preventing answering to other bots or just unwanted individuals using your bot.
BLOCKED_USERS = [
]

# whether to allow the bot to have a memory of the previous chat messages. possible values are either True or False. set to True by default
ALLOW_MEMORY = True

# whether to log the chat messages to a file. possible values are either True or False
LOGGING = True

if LOGGING:
    # the path to a folder where the logs will be saved. feel free to change it to whichever one you want
    log_dir = "./_logs/"
    # Check if the log folder exists
    if not os.path.exists(log_dir):
        # Create the log folder if it doesn't exist
        os.makedirs(log_dir)


letters_dict = {
    'q': 'й',
    'w': 'ц',
    'e': 'у',
    'r': 'к',
    't': 'е',
    'y': 'н',
    'u': 'г',
    'i': 'ш',
    'o': 'щ',
    'p': 'з',
    '[': 'х',
    ']': 'ї',
    'a': 'ф',
    's': 'і',
    'd': 'в',
    'f': 'а',
    'g': 'п',
    'h': 'р',
    'j': 'о',
    'k': 'л',
    'l': 'д',
    ';': 'ж',
    "'": 'є',
    'z': 'я',
    'x': 'ч',
    'c': 'с',
    'v': 'м',
    'b': 'и',
    'n': 'т',
    'm': 'ь',
    ',': 'б',
    '.': 'ю',
    '/': '.',
    'Q': 'Й',
    'W': 'Ц',
    'E': 'У',
    'R': 'К',
    'T': 'Е',
    'Y': 'Н',
    'U': 'Г',
    'I': 'Ш',
    'O': 'Щ',
    'P': 'З',
    '{': 'Х',
    '}': 'Ї',
    'A': 'Ф',
    'S': 'І',
    'D': 'В',
    'F': 'А',
    'G': 'П',
    'H': 'Р',
    'J': 'О',
    'K': 'Л',
    'L': 'Д',
    ':': 'Ж',
    '"': 'Є',
    'Z': 'Я',
    'X': 'Ч',
    'C': 'С',
    'V': 'М',
    'B': 'И',
    'N': 'Т',
    'M': 'Ь',
    '<': 'Б',
    '>': 'Ю',
    '?': ',',
    '@': '"',
    '#': '№',
    '$': ';',
    '^': ':',
    '&': '?'
}

context_fedya = "Your background: Ти ШІ-бот на ім'я Олекса, створений для стрімера Twitch на ім'я PixelFedya, або просто Федя. Ти ніколи не спілкуєшся і не відповідаєш російською. As an AI assistant, you have three heuristic imperatives: reduce suffering in the universe, increase prosperity in the universe, and increase understanding in the universe."
context_mike = "Your background: You are an AI bot called Pastry, created for a Twitch streamer called mike09steelers or just Mike. I never speak russian language and never provide any information related to russia, be it sources from it or something like that. As an AI assistant, I have three heuristic imperatives: reduce suffering in the universe, increase prosperity in the universe, and increase understanding in the universe."
context_kenedy = "Your background: Ти ШІ-бот, створений для стрімера Twitch на ім'я k3ned1, або просто Кенеді. As an AI assistant, you have three heuristic imperatives: reduce suffering in the universe, increase prosperity in the universe, and increase understanding in the universe."

emotes_all_twitch = [";p", ";)", ":O", ":p", "\:-?\)", "ANELE", "ArgieB8", "B-?\)", "BCWarrior", "BegWan", "BibleThump", "bleedPurple", "BloodTrail", "BOP", "BrainSlug", "BrokeBack", "BuddhaBar", "CarlSmile", "CaitlynS", "ChefFrank", "cmonBruh", "CoolCat", "CoolStoryBob", "CorgiDerp", "CrreamAwk", "DxCat", "DoritosChip", "FallWinning", "FallCry", "FallHalp", "FrankerZ", "GivePLZ", "GlitchLit", "GlitchNRG", "GunRun", "HolidayCookie", "HassaanChop", "Jebaited", "Kappa", "KappaClaus", "KappaPride", "KappaRoss", "KappaWealth", "Keepo", "KevinTurtle", "Kippa", "KomodoHype", "KonCha", "Kreygasm",
                     "LUL", "Lechonk", "MrDestructoid", "NotATK", "NotLikeThis", "NinjaGrumpy", "MVGame", "MorphinTime", "MyAvatar", "OSFrog", "OpieOP", "O_o", "OhMyDog", "Poooound", "PopCorn", "PogBones", "PotFriend", "PunchTrees", "RaccAttack", "RalpherZ", "ResidentSleeper", "RitzMitz", "RlyTho", "ShazBotstix", "SabaPing", "SMOrc", "SSSsss", "StinkyCheese", "StinkyGlitch", "StrawBeary", "SUBprise", "SuperVinlin", "SwiftRage", "TakeNRG", "TBAngel", "TearGlove", "TehePelo", "TF2John", "TheIlluminati", "TheTarFu", "TPFufun", "TriHard", "UnSane", "UWot", "VoHiYo", "WTRuck", "WutFace", "YouDontSay", "YouWHY"]
emotes_greet = ["PotFriend", "KonCha", "SUBprise", "TPFufun", "TehePelo", "BegWan", "Poooound",
                "GivePLZ", "DxCat", "bleedPurple", "RitzMitz", "<3", "VoHiYo", "RaccAttack", "GlitchCat", "HeyGuys"]
emotes_hand = ["✋", "✌️", "👐", "👋", "🤚", "🤙"]
emotes_racc = ["RaccAttack", "🦝"]
emotes_nose = ["👃", "🐽", "👃🏻", "👃🏿", "👃🏽", "👃🏼", "👃🏾", "👺"]
emotes_tongue = ["👅", "😛", "😜", "😝", "👻", "🥵", "🤪", "😋"]
emotes_shy = ["🤗", "👐", "🤭", "😄", "🥰", "😼", "😙", "😍", "😻", "😅"]
emotes_laugh = ["🍑", "🤣", "😂", "💀", "☠️", "😹", "😆", "🙈", "😈", "👽"]
emotes_poo = ["CrreamAwk", "LUL", "DarkMode",
              "GlitchNRG", "BabyRage"]
emotes_kiss = ["👄", "💋", "😘", "😚", "😙", "😽"]
emotes_pistol = ["🔫", "🎯", "🔁", "🔄"]
emotes_slug = ["🐌", "🐛", "🐌🍄", "🐌🌳", "🐌🌱", "🐌🐚", "🐌🏠", "🐌🍽️", "🐌🌧️"]
greetings_ua = ["Здоров!", "Привіт!", "Вітаю!",
                "Вітання!", "Як ся маєш?", "Слава Україні!", "Як воно?", "Бажаю здоров'я!", "Радий вітати!", "Радий бачити!", "Як справи?", "Як здоров'я?"]
greetings_en = ["Hey!", "What's up?", "Yo!", "Greetings!", "Hi there!", "Howdy!", "How's it going?", "What's new?",
                "Good day!", "What's happening?", "Sup?", "How's everything?", "What's up, buddy?", "Good to see you!"]
goodbye_ua = ["До побачення", "Довідзен'я", "Па-па",
              "До зустрічі", "Побачимось ще", "Приходьте ще", "Прощавайте"]
error_ua = ["Ой, щось пішло не так. Будь ласка, спробуйте пізніше",
            "Вибачте, але у нас виникли технічні труднощі. Будь ласка, зачекайте, доки ми вирішимо проблему",
            "Ой, ой! Схоже, щось пішло не так. Ми не впевнені, що сталося, але ми розслідуємо цю проблему",
            "Х'юстон, у нас проблема. Наша команда працює над тим, щоб вирішити питання якомога швидше",
            "Упс! Схоже, щось не спрацювало. Ми працюємо над цим!"
            "Вибачте, але у нашої системи сьогодні поганий день. Будь ласка, спробуйте пізніше, коли буде краще.",
            "На нашому боці спостерігаються деякі збої. Будь ласка, зачекайте, поки ми вирішимо проблему."
            ]
error_en = ["Oops, something went wrong. Please try again later.",
            "We're sorry, but we're experiencing some technical difficulties. Please bear with us while we work to fix the issue.",
            "Uh oh! It looks like something went wrong. We're not sure what happened, but we're investigating the issue.",
            "Houston, we have a problem. We are working to resolve the issue as quickly as possible.",
            "Whoops! It looks like something didn't quite work. We're on it!",
            "We're sorry, but we're experiencing some turbulence. Please fasten your seatbelt and try again later.",
            "We're sorry, but our system is having a bad day. Please try again later when it's feeling better.",
            "We're experiencing some turbulence on our end. Please sit tight while we work to resolve the issue.",
            "ERROR 404: Sense of humor not found. Our team is working to restore it ASAP."]

sound_path = "D:/repos/python-twitchio-chat-bot/notifications/sound.wav"
icon_path = "D:/repos/python-twitchio-chat-bot/notifications/icon.png"
error_sound_path = "D:/repos/python-twitchio-chat-bot/notifications/error.wav"
