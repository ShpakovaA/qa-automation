import requests
import pytest
from operator import itemgetter
from urllib.parse import urljoin


valid_headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer 1c8b84b5a585449b0f30ad658b06331afaf7144e36bbafb34b8e801cf610fe2b"
}

header_for_delete_request = {
        "Authorization": "Bearer 1c8b84b5a585449b0f30ad658b06331afaf7144e36bbafb34b8e801cf610fe2b"
    }

valid_post_body = {"title": "Test post", "body": "test test test"}
invalid_post_body = {"title": "Test post, body: test test test"}
valid_user_data = {"name": "Test User", "gender": "female", "email": "test.0089854@1ce.com", "status": "active"}

base_url = 'https://gorest.co.in/public/v2/'


def create_user(url, headers, user_data):
    resource = 'users'
    path = urljoin(url, resource)
    return requests.post(path, json=user_data, headers=headers)


def delete_user(url, headers, user_ID):
    resource = f"users/{user_ID}"
    path = urljoin(url, resource)
    return requests.delete(path, headers=headers)


def create_post(url, headers, user_ID, post_body):
    resource = f"users/{user_ID}/posts"
    path = urljoin(url, resource)
    return requests.post(path, json=post_body, headers=headers)


def retrieve_user_posts(url, headers, user_ID):
    resource = f"users/{user_ID}/posts"
    path = urljoin(url, resource)
    return requests.get(path, headers=headers)


def retrieve_posts_ids(url, headers, user_ID):
    posts = retrieve_user_posts(url, headers, user_ID).json()
    return list(map(itemgetter('id'), posts))


@pytest.fixture()
def user():
    user = create_user(base_url, valid_headers, valid_user_data)
    user_id_ = user.json()["id"]
    yield user
    delete_user(base_url, header_for_delete_request, user_id_)


@pytest.fixture()
def user_id(user):
    return user.json()["id"]


def test_valid_post_creation(user_id):
    post = create_post(base_url, valid_headers, user_id, valid_post_body)
    post_id = post.json()["id"]
    user_posts = retrieve_posts_ids(base_url, valid_headers, user_id)
    assert post.status_code == 201
    assert post_id in user_posts


def test_post_creation_with_empty_field(user_id):
    post = create_post(base_url, valid_headers, user_id, invalid_post_body)
    post_error_message = post.json()[0]["message"]
    assert post.status_code == 422
    assert post_error_message == "can't be blank"