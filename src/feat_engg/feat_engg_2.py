import polars as pl
from polars import col


def feat_engg_2(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(col("attr_2").mul(2).alias("feat_2"))
