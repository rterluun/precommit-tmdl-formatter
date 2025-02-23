from re import IGNORECASE
from re import compile as re_compile
from re import escape as re_escape
from re import sub as re_sub
from typing import List


def get_column_names(content: str) -> List[str]:
    table_name = re_compile(r"table\s+'?([^'\n]+)", IGNORECASE).findall(content)
    column_names = re_compile(r"\s+column\s+'?([^'\n]+)", IGNORECASE).findall(content)

    if table_name:
        table_name_prefix = table_name[0]
        column_names = [
            f"'{table_name_prefix}'[{column_name}]" for column_name in column_names
        ]

    return column_names


def rename_column_names_in_measure_file(content: str, column_names: List[str]) -> str:
    for column_name in column_names:
        pattern = re_escape(column_name)
        content = re_sub(pattern, column_name, content, flags=IGNORECASE)

    return content
