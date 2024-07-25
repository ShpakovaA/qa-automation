from HW43_REST_API.api_client import API
import pytest
from HW43_REST_API.test_data import TestData


@pytest.fixture()
def user():
    api_client = API()
    user = api_client.create_user(TestData.VALID_USER_DATA)
    user_id_ = user.json()["id"]
    yield user
    api_client.delete_user(user_id_)


@pytest.fixture()
def user_id(user):
    return user.json()["id"]
