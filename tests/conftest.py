import pytest

from config import HOST
from src.api import PlaceholderAPI
from test_data.default_data import USER_ID, BODY, TITLE


@pytest.fixture(scope='session')
def placeholder_api():
    return PlaceholderAPI(host=HOST)


@pytest.fixture(scope='function')
def create_default_post(placeholder_api):
    status_code, response_data = placeholder_api.create_post(user_id=USER_ID,
                                                             body=BODY,
                                                             title=TITLE)
    default_post_id = response_data.get('id')
    yield default_post_id
    placeholder_api.delete_post(default_post_id)
