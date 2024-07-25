from HW43_REST_API.helpers import get_base_url
from HW43_REST_API.helpers import get_token
from operator import itemgetter
from urllib.parse import urljoin
import requests


class API:

    VALID_HEADERS = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"{get_token()}"
    }

    INVALID_HEADERS = {
        "Authorization": f"{get_token()}"
    }

    @property
    def base_url(self):
        return get_base_url()

    def create_user(self, user_data):
        resource = 'users'
        path = urljoin(self.base_url, resource)
        return requests.post(path, json=user_data, headers=API.VALID_HEADERS)

    def delete_user(self, user_ID):
        resource = f"users/{user_ID}"
        path = urljoin(self.base_url, resource)
        return requests.delete(path, headers=API.VALID_HEADERS)

    def create_post(self, user_ID, post_body):
        resource = f"users/{user_ID}/posts"
        path = urljoin(self.base_url, resource)
        return requests.post(path, json=post_body, headers=API.VALID_HEADERS)

    def retrieve_user_posts(self, user_ID):
        resource = f"users/{user_ID}/posts"
        path = urljoin(self.base_url, resource)
        return requests.get(path, headers=API.VALID_HEADERS)

    def retrieve_posts_ids(self, user_ID):
        posts = self.retrieve_user_posts(user_ID).json()
        return list(map(itemgetter('id'), posts))

    def retrieve_post_data(self, post_id):
        resource = f"posts/{post_id}"
        path = urljoin(self.base_url, resource)
        post_data = requests.get(path, headers=API.VALID_HEADERS).json()
        return post_data

    def retrieve_post_title(self, post_id):
        return self.retrieve_post_data(post_id)["title"]

    def retrieve_post_body(self, post_id):
        return self.retrieve_post_data(post_id)["body"]


