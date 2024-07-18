import pytest
from api_client import ApiClient

client = ApiClient()


@pytest.fixture(scope="session")
def base_url():
    return 'https://gorest.co.in/public/v2/'


@pytest.fixture(scope="session")
def token():
    return "Bearer 1c8b84b5a585449b0f30ad658b06331afaf7144e36bbafb34b8e801cf610fe2b"


@pytest.fixture
def user(base_url):
    user = client.create_valid_user(base_url)
    user_id_ = user.json()["id"]
    yield user
    client.delete_user(user_id_,base_url)


@pytest.fixture()
def user_id(user):
    return user.json()["id"]
