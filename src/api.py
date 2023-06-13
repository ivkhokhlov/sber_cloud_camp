import requests


class PlaceholderAPI():
    def __init__(self, host):
        self.session = requests.Session()
        self.host = host
        pass

    def get_posts(self):
        response = self.session.get(f"{self.host}/posts")
        return response.status_code, response.json()

    def get_post(self, post_id):
        response = self.session.get(f"{self.host}/posts/{post_id}")
        return response.status_code, response.json()

    def create_post(self, data):
        response = self.session.post(f"{self.host}/posts", data=data)
        return response.status_code, response.json()

    def delete_post(self, post_id):
        response = self.session.delete(f"{self.host}/posts/{post_id}")
        return response.status_code, response.json()
