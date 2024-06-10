from unittest import mock

from rna import transcribe


@mock.patch("builtins.open", new_callable=mock.mock_open, read_data="ACGTAAA")
def test_transcribe(mock_open):
    res = transcribe("mock.txt")
    assert res == "ACGUAAA"
