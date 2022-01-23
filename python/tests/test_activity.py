import os
import pytest

from unittest import mock
from activity import handler


@pytest.fixture(autouse=True)
def mock_env_vars():
    with mock.patch.dict(os.environ, {"API_URL": "https://www.boredapi.com/api/activity"}):
        yield


def test_case():
    result = handler([], [])

    assert result == result | {"statusCode": 200}
