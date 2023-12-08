SELECT
    tbl.attr_1 + 1 AS attr_1,
tbl.attr_2 + 1 AS attr_2
FROM {{ test_tbl or 'actual_tbl_here' }} AS tbl
