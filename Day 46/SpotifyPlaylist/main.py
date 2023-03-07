from bs4 import BeautifulSoup
import requests
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_ID = "09a1c6f2446a47928a551417396108de"
SPOTIFY_SECRET = os.environ.get("SPOTIFY_SECRET")


def parse_songs(d: str) -> dict:
    response = requests.get(f"https://www.billboard.com/charts/hot-100/{d}")

    soup = BeautifulSoup(response.text, "html.parser")

    titles_list = []
    titles = [title.getText() for title in soup.find_all(name="h3", class_="c-title")]
    for i in range(0, len(titles)):
        titles[i] = titles[i].replace("\n", "")
        titles[i] = titles[i].replace("\t", "")
        if titles[i] == "Songwriter(s):":
            titles_list.append(titles[i - 1])
    titles_list.pop(0)

    artists_list = []
    artists = [artist.getText() for artist in soup.find_all(name="span", class_="c-label")]

    i = 0
    del artists[:4]

    for _ in range(0, len(artists)):
        if artists[i] == "\n\t\n\tNEW\n":
            artists.pop(i)
            continue
        if i % 8 == 0:
            artists[i] = artists[i].replace("\n", "")
            artists[i] = artists[i].replace("\t", "")
            artists_list.append(artists[i])
        i += 1

    return dict(zip(artists_list, titles_list))


date = input("Which date do you want to use? Type in format YYYY-MM-DD: ")
songs = parse_songs(date)

auth_manager = SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com/callback/",
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
sp = spotipy.Spotify(auth_manager=auth_manager)
url = "https://api.spotify.com/v1/search"

uri_list = []
for key, value in songs.items():
    results = sp.search(q=f"track:{value} artist:{key}", type="track", limit=1)
    try:
        uri_list.append(results['tracks']['items'][0]['uri'])
    except IndexError:
        continue

# Create the playlist and get its ID
playlist_name = f"{date} Billboard 100"
playlist = sp.user_playlist_create(user=sp.current_user()["id"], name=playlist_name, public=False)
playlist_id = playlist["id"]
# Add the tracks to the playlist
sp.playlist_add_items(playlist_id=playlist_id, items=uri_list)
