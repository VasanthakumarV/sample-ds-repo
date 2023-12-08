import polars as pl
from polars.testing import assert_frame_equal

from .feat_engg_1 import feat_engg_1


def test_feat_engg_1() -> None:
    input = pl.from_dict({"attr_1": [1, 2, 3]})
    expected = pl.from_dict({"attr_1": [1, 2, 3], "feat_1": [2, 4, 6]})

    output = feat_engg_1(input)

    assert_frame_equal(output, expected)
