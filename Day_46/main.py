from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "ba0d4e5122a2408ca976166d98270131"
CLIENT_SECRET = "acd4c380df2b4404bf08d27555cf3e87"

# this format - 2000-08-12
date = input("Введите дату в формате (2000-08-12): ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
billboard_html = response.text

soup = BeautifulSoup(billboard_html, "html.parser")
all_music = soup.find_all(name="span", class_="chart-element__information__song")
song_names = [song.getText() for song in all_music]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} не существует в spotify.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
