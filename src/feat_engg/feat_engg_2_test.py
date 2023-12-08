import polars as pl
from polars.testing import assert_frame_equal

from .feat_engg_2 import feat_engg_2


def test_feat_engg_2() -> None:
    input = pl.from_dict({"attr_2": [1, 2, 3]})
    expected = pl.from_dict({"attr_2": [1, 2, 3], "feat_2": [2, 4, 6]})

    output = feat_engg_2(input)

    assert_frame_equal(output, expected)
