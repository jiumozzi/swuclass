import pytest
from add import add


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (1, 2, 3),
        (2, 3, 5),
        (5, 6, 11),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected
