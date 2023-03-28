from bs4 import BeautifulSoup
# import lxml

with open("website.html") as file:
    contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# # print(soup.title.name)
# print(soup.title.string)
#
# # print(soup.prettify())
# print(soup.a)
# print(soup.li)
# print(soup.p)

#getting hold of a attributes
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# all_anchor_tags = soup.find_all(name="p")
# print(all_anchor_tags)


# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     # Getting value inside the tags
#     # print(tag.getText())
#
#     # Getting link inside the href
#     print(tag.get("href"))

# #Searching by the attribute name id=, class
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.getText)
# # print(section_heading.name)
# print(section_heading.get("class"))
#
# #select_one gives the first matching item in the list and select gives all of the items in the list
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# #selecting by id
# name = soup.select_one(selector="#name")
# print(name)
#
# #selecting all of the elements that have class of heading
# headings = soup.select(selector=".heading")
# print(headings)

# If we make soup with the HTML code below,
# how would you get hold of the value of maxlength?
with open("test.html") as test_file:
    content = test_file.read()

soup = BeautifulSoup(content, 'html.parser')


form_tag = soup.find("input")
print(form_tag.get("maxlength"))