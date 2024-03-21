from functools import reduce
from rich.console import Console
from rich.traceback import install

install()
console = Console()


def count_words_and_shortest_length(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    punctuation = '!@#$%^&*()_+{}|:"<>?`~'
    translation_table = str.maketrans("", "", punctuation)
    words = text.translate(translation_table).split()
    wordsCount = len(words)
    shortestWordLength = reduce(
        lambda acc, word: min(acc, len(word)), words, float("inf")
    )

    return wordsCount, shortestWordLength


# Usage
file_path = "D:\\everything\\University\\y2t2\\SA\\tasks\\lb2\\dev\\data\\input.txt"
word_count, shortest_length = count_words_and_shortest_length(file_path)
print(f"Number of words: {word_count}")
print(f"Length of shortest word: {shortest_length}")
