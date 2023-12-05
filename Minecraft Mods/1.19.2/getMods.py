import os


def get_file_names(path):
    return os.listdir(path)


print(get_file_names("D:/repos/everything/Minecraft Mods/1.19.2/mods"))
