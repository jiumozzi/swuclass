import pytest


def test_function1():
    assert (1, 2, 3) == (1, 2, 3)  # 1 passed


def test_function2():
    assert (1, 2, 3) == (1, 4, 3)  # 1 failed
