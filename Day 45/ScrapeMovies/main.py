from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best"
                        "-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]
titles.reverse()

with open(file="movies.txt", mode="w", encoding="utf-8") as f:
    for title in titles:
        if title[2] == ":":
            title = title[:2] + ")" + title[3:]
        f.write(title+"\n")
