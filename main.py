from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="span", class_='titleline')
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.contents[0].getText()
    article_texts.append(text)
    link = article_tag.contents[0].get('href')
    article_links.append(link)

article_upvotes = []

for td in soup.find_all(name="td", class_='subtext'):
    score = td.find(name="span", class_='score')
    if score:
        score = int(score.getText().split()[0])
    else:
        score = 0
    article_upvotes.append(score)

highest_upvote_no = article_upvotes.index(max(article_upvotes))

print(f"Highest number of upvotes: {article_upvotes[highest_upvote_no]}\nTitle: {article_texts[highest_upvote_no]}\n"
      f"Url: {article_links[highest_upvote_no]}")
