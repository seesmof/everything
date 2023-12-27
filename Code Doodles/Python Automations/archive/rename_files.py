import os

dir_path = r"C:/Users/seesm/OneDrive/Програми/Obsidian/obsidian-main-vault/journal/"

replacements = {
    "Oct": "жовт",
    "Nov": "лист",
    "Dec": "груд",
    "Jan": "січ",
    "Feb": "лют",
    "Mar": "бер",
    "Apr": "квіт",
    "May": "трав",
    "Jun": "черв",
    "Jul": "лип",
    "Aug": "серп",
    "Sep": "верес",
}

for file_name in os.listdir(dir_path):
    new_file_name = file_name
    for old, new in replacements.items():
        if old in new_file_name.lower():
            new_file_name = new_file_name.replace(old, new)
    os.rename(os.path.join(dir_path, file_name), os.path.join(dir_path, new_file_name))
