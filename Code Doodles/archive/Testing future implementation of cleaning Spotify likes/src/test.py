import requests
from bs4 import BeautifulSoup


def get_lyrics(song_url):
    page = requests.get(song_url)
    soup = BeautifulSoup(page.content, "html.parser")
    lyrics = soup.find("div", {"class": "lyrics"}).get_text().strip()
    return lyrics


# Example usage:
song_url = "https://genius.com/Ed-sheeran-shape-of-you-lyrics"
print(get_lyrics(song_url))
