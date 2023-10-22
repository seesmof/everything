from spotipy.oauth2 import SpotifyOAuth
import spotipy
from env import *
import re

# STEP 1: Parse markdown table with song names and authors


def parseSpotifyTable(markdownTable):
    extractedData = []
    pattern = r"\| (.+?)\s*\| (.+?)\s*\|"
    matches = re.findall(pattern, markdownTable)
    for match in matches:
        song_name = match[0]
        artist = match[1]
        extractedData.append(
            {
                "song": song_name,
                "artist": artist
            }
        )
    return extractedData


spotifyPlaylistData = parseSpotifyTable(markdownTable)

# STEP 2: Authenticate with Spotify with my credentials

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientID,
                                               client_secret=clientSecret,
                                               redirect_uri=redirectURL, scope="playlist-modify-public"))
user = sp.current_user()
username = user['display_name']
userID = user['id']

# STEP 3: Create a playlist on Spotify

playlistName = username + " Playlist"
playlistDescription = "Created by " + username

playlist = sp.user_playlist_create(
    user=userID, name=playlistName, description=playlistDescription)
playlistID = playlist['id']


def seePlaylistContents(playlistID):
    playlistContents = sp.playlist_items(playlistID)
    if len(playlistContents['items']) == 0:
        print("Playlist is empty")
    else:
        for item in playlistContents['items']:
            track = item['track']
            author = track['artists'][0]['name']
            print(author + " - " + track['name'])

# STEP 4: Look for songs


for song in spotifyPlaylistData:
    track = song['song']
    artist = song['artist']

    results = sp.search(q=track, type='track')

    if results["tracks"]["total"] > 0:
        songUrl = results["tracks"]["items"][0]["uri"]
        songName = results["tracks"]["items"][0]["name"]
        sp.playlist_add_items(playlistID, [songUrl])
        print(songName + " added to " + playlistName)
    else:
        print("No mathces found")
