import pytest

from p2744 import lowupp


@pytest.mark.parametrize(
    ("str", "exp"),
    [
        ("WrongAnswer", "wRONGaNSWER"),
        ("ABcd", "abCD"),
    ],
)
def test_p2744(str, exp):
    assert lowupp(str) == exp
