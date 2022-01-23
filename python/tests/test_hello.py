import os
import pytest

from unittest import mock
from hello import handler


@pytest.fixture(autouse=True)
def mock_env_vars():
    with mock.patch.dict(os.environ, {"HELLO": "Hello Serverless!"}):
        yield


def test_case_1():
    event = {
        "headers": {
            "headerName1": "Value1",
            "headerName2": "Value2",
        },
        "body": {
            "fieldName": "Value3",
        },
    }

    result = handler(event, [])

    assert result == {
        'statusCode': 200,
        'body': '{"message": "Hello Serverless!"}'
    }


def test_case_2():
    event = {
        "headers": {
            "badHeader": "Value1"
        }
    }

    result = handler(event, [])

    assert result == {'statusCode': 400, 'body': '{"message": "Bad Request!"}'}
