from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(response.text, "html.parser")

article_titles = [article.getText().split(" (")[0] for article in soup.find_all(name="span", class_="titleline")]
article_links = [article.find("a").get("href") for article in soup.find_all(name="span", class_="titleline")]
# We need to take care of the cases where there is no article score
article_upvotes = [0] * len(article_titles)
index = 0
for score in soup.find_all(name="span", class_="score"):
    article_upvotes[index] = int(score.getText().split(" ")[0])
    index += 1

print(article_titles)
print(article_links)
print(article_upvotes)

max_index = article_upvotes.index(max(article_upvotes))
print(f"Most voted article '{article_titles[max_index]}' ({article_upvotes[max_index]} votes)")
