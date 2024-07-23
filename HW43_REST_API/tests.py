from HW43_REST_API.api_client import API
from HW43_REST_API.resources import Resources
import pytest

api_client = API()


def test_valid_post_creation(user_id):
    post = api_client.create_post(user_id, Resources.VALID_POST_BODY)
    post_id = post.json()["id"]
    user_posts = api_client.retrieve_posts_ids(user_id)
    assert post.status_code == 201
    assert post_id in user_posts


def test_post_creation_with_empty_field(user_id):
    post = api_client.create_post(user_id, Resources.INVALID_POST_BODY)
    post_error_message = post.json()[0]["message"]
    assert post.status_code == 422
    assert post_error_message == Resources.BLANK_POST_FIELD_ERROR
