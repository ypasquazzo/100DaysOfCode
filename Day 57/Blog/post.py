import requests


class Post:
    def __init__(self):
        self.posts = []
        self.get_posts()

    def get_posts(self):
        response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
        response.raise_for_status()
        self.posts = response.json()
