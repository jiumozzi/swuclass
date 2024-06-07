import pytest

from p15964 import sumsubmul


@pytest.mark.parametrize(
    ("A", "B", "exp"),
    [
        (3, 2, 5),
        (6, 4, 20),
    ],
)
def test_p15964(A, B, exp):
    assert sumsubmul(A, B) == exp
