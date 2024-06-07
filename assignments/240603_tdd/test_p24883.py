import pytest

from p24883 import Naver


@pytest.mark.parametrize(
    ("a", "result"),
    [
        ("n", "Naver D2"),
        ("N", "Naver D2"),
        ("a", "Naver Whale"),
    ],
)
def test_p24883(a, result):
    assert Naver(a) == result
