import requests


class Post:
    def __init__(self):
        self.posts = []
        self.get_posts()

    def get_posts(self):
        response = requests.get("https://api.npoint.io/5deaf41b4f8078c817e6")
        response.raise_for_status()
        self.posts = response.json()
