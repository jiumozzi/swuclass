from unittest import mock

from count_variant import count_variant


@mock.patch(
    "builtins.open",
    new_callable=mock.mock_open,
    read_data=(
        "##META\n"
        "#CHROM\tPOS\tID\tREF\tALT\n"
        "chr1\t100\t.\tA\tC\n"
        "chr1\t200\t.\tT\tG\n"
        "chr2\t100\t.\tAA\tA\n"
        "chr3\t100\t.\tA\tAAT\n"
        "chr3\t200\t.\tA\tAATG\n"
    ),
)
def test_count_variant(mock_open):
    res = count_variant("sample.vcf")
    assert res == {"deletion": 1, "insertion": 2, "snp": 2}
