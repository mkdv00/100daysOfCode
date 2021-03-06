from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
empire_online_html = response.text

soup = BeautifulSoup(empire_online_html, "html.parser")
movies = soup.find_all(name="h3")

all_movies_reverse = movies[::-1].getText()

print(all_movies_reverse)
