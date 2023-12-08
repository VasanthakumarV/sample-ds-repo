import polars as pl
from polars import col
def feat_engg_1(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(col("attr_1").mul(2).alias("feat_1"))
