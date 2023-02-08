import pytest
import re


@pytest.fixture(scope="module")
def my_input():
    return [1, 12, 5, 7, 3, 875, 343, 8, 43, 56, 6, 2, 10, 54]
