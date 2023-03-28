from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession

#step one
response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

#step two
movies_web_page = response.text

with open("movies.html") as file:
    website_html = file.readlines()

string_website = ' '.join([str(elem) for elem in website_html])
# print(mystring)

# #Step three
soup = BeautifulSoup(string_website, "html.parser")
h3_element = soup.find_all(name="h3", class_="jsx-2692754980")
print(h3_element)

# movie_list = ' '.join([str(movie.getText()) for movie in h3_element])
movie_list = [movie.getText() for movie in h3_element]

#reversing list methon 1
reverse_movie_list = movie_list[::-1]

# with open("top_movies.txt", "w") as file:
#     file.write(movie_list)

with open("top_movies.txt", "w") as file:
    for movie in reverse_movie_list:
        file.write(f"{movie}\n")
        #second way
        # file.write("%s\n" % movie)





# title_find = soup.find_all(name="h3", class_=".jsx-4245974604")
# title_select = soup.select(selector=".jsx-4245974604")
#
# title_list = [movie.getText() for movie in soup.select(selector=".jsx-3523802742 .jsx-4245974604")]
#
# title_lists = [movie.getText() for movie in soup.find_all(name="h3", class_=".jsx-4245974604")]
#
# # print(soup.findNextSiblings(name="div"))
# print(title_list)
# print(soup.div.find("a"))
