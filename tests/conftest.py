import pytest

from src.api import PlaceholderAPI
from test_data.default_data import USER_ID, BODY, TITLE


def pytest_addoption(parser):
    parser.addoption('--host', action='store', default='http://localhost:3000', help='host')


@pytest.fixture(scope='session')
def placeholder_api(request):
    host = request.config.getoption('--host')
    return PlaceholderAPI(host=host)


@pytest.fixture(scope='function')
def create_default_post(placeholder_api):
    status_code, response_data = placeholder_api.create_post(user_id=USER_ID,
                                                             body=BODY,
                                                             title=TITLE)
    default_post_id = response_data.get('id')
    yield default_post_id
    placeholder_api.delete_post(default_post_id)
