from unittest import mock
from dna import count_base


@mock.patch("builtins.open", new_callable=mock.mock_open, read_data="ACGTAAA")
def test_count_base(mock_open):
    res = count_base("mock.txt")
    assert res == f"4 1 1 1"
