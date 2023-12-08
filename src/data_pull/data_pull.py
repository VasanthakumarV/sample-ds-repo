from typing import Optional, Mapping, NamedTuple

import polars as pl
from jinja2 import Environment, FileSystemLoader


# TODO should come from a config file and should be secure
conn_str = """\
Driver={PostgreSQL UNICODE};\
Server=localhost;\
Port=5432;\
Database=test;\
Uid=postgres;\
Pwd=password\
"""


def run_seq() -> pl.DataFrame:
    # TODO should be able to run multiple queries and join them
    df = run_query("query_1.sql")
    return df


# Only useful in tests
MockData = NamedTuple(
    "MockData", [("columns", list[str]), ("values", list[list[object]])]
)
MockTables = Mapping[str, MockData]


def run_query(query_name: str, mock_data: Optional[MockTables] = None) -> pl.DataFrame:
    # TODO location shouldn't be hardcoded
    env = Environment(loader=FileSystemLoader(searchpath="src/data_pull/"))

    if mock_data is None:
        query = env.get_template(query_name).render()
    else:
        sub_queries_mapping = {
            k: env.from_string(SUB_QUERY_TEMPL).render(
                columns=v.columns, values=v.values
            )
            for k, v in mock_data.items()
        }
        query = env.get_template(query_name).render(sub_queries_mapping)

    df = pl.read_database(query, conn_str)
    return df


SUB_QUERY_TEMPL = """(
    SELECT *
    FROM (
        VALUES
        {% for value in values -%}
            ({%- for v in value -%}
                {{ v }}{% if not loop.last %}, {% endif %}
            {%- endfor %}){% if not loop.last %},{% endif %}
        {% endfor %}
    ) AS temp ({% for c in columns %}{{ c }}{% if not loop.last %}, {% endif %}{% endfor %})
)"""
