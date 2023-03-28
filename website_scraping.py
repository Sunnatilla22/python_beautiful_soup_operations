from bs4 import BeautifulSoup
import requests
from pprint import pprint

#Step one
response = requests.get("https://news.ycombinator.com/news")
#Step two
yc_web_page = response.text
#Step three
soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

# article_tag = soup.find(name="span", class_="titleline")
# print(article_tag)

articles = soup.select(selector=".titleline a")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.string
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)


article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

#
# print(article_texts)
largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])

# print(article_upvote)

# article_tag = soup.select(selector=".titleline a")
# print(article_text)
# print(article_link)


# article_upvote = article_tag.string
# headings = soup.select(selector=".titleline a")
# print(headings[0].string)

#One of the ways
# score_tag = soup.select_one(selector="#score_34303497")
# article_upvote = score_tag.string
# print(article_upvote)

# news_response = requests.get("https://www.aljazeera.com/")
# print(news_response.text)