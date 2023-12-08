import polars as pl
from polars.testing import assert_frame_equal

from .data_pull import MockData, MockTables, run_query


MOCK_TABLES: MockTables = {
    "test_tbl": MockData(
        columns=["attr_1", "attr_2"],
        values=[[0, -99], [1, 101]],
    )
}

EXPECTED = pl.from_dict({"attr_1": [1, 2], "attr_2": [-98, 102]})


def test_query_1() -> None:
    output = run_query("query_1.sql", MOCK_TABLES)
    # TODO dtypes should match
    assert_frame_equal(output, EXPECTED, check_dtype=False)
