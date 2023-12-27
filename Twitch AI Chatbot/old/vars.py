import os

TOKEN = "m56jxhrfo0hdjuieersxj9gk1gjsvl"
BOT_NICK = "piprly"
DELAY = 3.0
WANTED_CHANNELS = ["PixelFedya", "seesmof", "apek90"]
ALLOW_MEMORY = True
LOGGING = True
PERSONA = "Be as brief as you possible can unless asked otherwise."

if LOGGING:
    log_dir = "./logs/"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
