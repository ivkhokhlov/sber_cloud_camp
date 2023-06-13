import pytest

from config import HOST
from src.api import PlaceholderAPI


@pytest.fixture(scope='session')
def placeholder_api(request):
    return PlaceholderAPI(host=HOST)


@pytest.fixture(scope='function')
def create_new_post(placeholder_api):
    pass
