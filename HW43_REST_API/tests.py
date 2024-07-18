import pytest
from HW43_REST_API.api_client import ApiClient

client = ApiClient()


def test_valid_post_creation(user_id, base_url):
    post = client.create_post(user_id, base_url)
    post_id = post.json()["id"]
    user_posts = client.retrieve_posts_ids(user_id, base_url)
    assert post.status_code == 201
    assert post_id in user_posts


def test_post_creation_with_empty_field(user_id, base_url):
    post = client.create_post(user_id, base_url)
    post_error_message = post.json()[0]["message"]
    assert post.status_code == 422
    assert post_error_message == "can't be blank"


