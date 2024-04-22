import io
from html.parser import HTMLParser
from os import path


class MLRemover(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = io.StringIO()

    def handle_data(self, d):
        self.text.write(d)

    def get_data(self):
        return self.text.getvalue()


def strip_tags(html, file_path):
    s = MLRemover()
    s.feed(html)
    return s.get_data()


def clean_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    cleaned_text = strip_tags(html, file_path)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print(f"File {file_path} cleaned and saved.")


currentDir: str = path.dirname(path.abspath(__file__))
filePath: str = path.join(currentDir, "cleanText.txt")
result = clean_file(filePath)
