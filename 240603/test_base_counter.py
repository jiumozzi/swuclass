import pytest

from base_counter import base_count


def test_base_count():
    seq = "AATC"
    exp = {"A": 2, "C": 1, "T": 1}
    assert base_count(seq) == exp
