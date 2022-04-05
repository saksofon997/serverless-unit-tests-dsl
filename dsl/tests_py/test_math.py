# Autogenerated Lambda test
# Template: PY

import os
import pytest

from unittest import mock
from math import handler


@pytest.fixture()
def mock_env_vars_mathCase1():
    with mock.patch.dict(os.environ, {
        "OPERATION": "multiply"
    }):
        yield


def mathCase1(mock_env_vars_mathCase1):
    event = {
        "a": 2,
        "b": 3
    }

    result = handler(event, [])

    assert result == 6


@pytest.fixture()
def mock_env_vars_mathCase2():
    with mock.patch.dict(os.environ, {
        "OPERATION": "add"
    }):
        yield


def mathCase2(mock_env_vars_mathCase2):
    event = {
        "a": 2,
        "b": 3
    }

    result = handler(event, [])

    assert result == 5
