import random


class Resources:

    VALID_POST_BODY = {"title": "Test post", "body": "test test test"}
    INVALID_POST_BODY = {"title": "Test post, body: test test test"}

    BLANK_POST_FIELD_ERROR = "can't be blank"

    VALID_USER_DATA = {"name": "Test User", "gender": "female", "email": f"test.{random.randint(100, 999)}@ce.com", "status": "active"}

