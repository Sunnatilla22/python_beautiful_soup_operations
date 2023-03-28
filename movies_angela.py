import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
webiste_html = response.text

soup = BeautifulSoup(webiste_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="jsx-4245974604")
movie_title = [movie.getText() for movie in all_movies]
#reversing list methon 1
movies = movie_title[::-1]
#reversing list methon 2
for n in range(len(movie_title) - 1,-1, -1):
    print(movie_title[n])

with open("movie.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
