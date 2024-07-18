import requests
from operator import itemgetter
from urllib.parse import urljoin
import pytest


class ApiClient:

    VALID_HEADERS = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer 1c8b84b5a585449b0f30ad658b06331afaf7144e36bbafb34b8e801cf610fe2b"
        }

    HEADERS_FOR_DELETE_REQUEST = {
        "Authorization": "Bearer 1c8b84b5a585449b0f30ad658b06331afaf7144e36bbafb34b8e801cf610fe2b"
    }

    valid_post_body = {"title": "Test post", "body": "test test test"}
    invalid_post_body = {"title": "Test post, body: test test test"}
    valid_user_data = {"name": "Test User", "gender": "female", "email": "test.92329854@1ce.com", "status": "active"}

    def create_valid_user(self, url):
        resource = 'users'
        path = urljoin(url, resource)
        return requests.post(path, json=self.valid_user_data, headers=self.VALID_HEADERS)

    def delete_user(self, user_ID, url):
        resource = f"users/{user_ID}"
        path = urljoin(url, resource)
        return requests.delete(path, headers=self.VALID_HEADERS)

    def create_post(self, user_ID, url):
        resource = f"users/{user_ID}/posts"
        path = urljoin(url, resource)
        return requests.post(path, json=self.valid_post_body, headers=self.VALID_HEADERS)

    def retrieve_user_posts(self, user_ID, url):
        resource = f"users/{user_ID}/posts"
        path = urljoin(url, resource)
        return requests.get(path, headers=self.VALID_HEADERS)

    def retrieve_posts_ids(self, user_ID, url):
        posts = self.retrieve_user_posts(user_ID, url).json()
        return list(map(itemgetter('id'), posts))







