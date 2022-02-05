import pytest
from src.main import lucky_number
import re

user = "Donke"
left = 1
right = 100


@pytest.fixture
def response() -> str:
    return lucky_number(user, left=left, right=right)


def test_lucky_number_user(response: str) -> None:
    assert user in response


def test_lucky_number_range(response: str) -> None:
    res = re.search(r"\d+", response)
    if res:
        res = int(res.group())  # type: ignore
        assert left <= res <= right  # type: ignore


# TODO: include an example of a test with mock (https://stackoverflow.com/a/2666006/9816164)
