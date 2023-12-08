import polars as pl

from .feat_engg_1 import feat_engg_1
from .feat_engg_2 import feat_engg_2


def run_seq(df: pl.DataFrame) -> pl.DataFrame:
    return df.pipe(feat_engg_1).pipe(feat_engg_2)
