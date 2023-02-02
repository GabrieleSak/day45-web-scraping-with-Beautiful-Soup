from bs4 import BeautifulSoup
# import lxml

with open('website.html', encoding='utf8') as f:
    contents = f.read()

soup = BeautifulSoup(contents, 'html.parser')

print(soup.title)