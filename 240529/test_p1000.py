import pytest
from p1000 import add

# p1000 python script에서 add 함수를 가져온다


def test_add():
    assert add(1, 2) == 3


def test_add2():
    assert add(2, 3) == 5


def test_add3():
    assert add(4, 5) == 9
