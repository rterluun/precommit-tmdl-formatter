from re import IGNORECASE
from re import compile as re_compile
from typing import List, Optional


def rename_columns(
    content: str,
    quote_columns: bool = True,
    ignore_columns_starting_with: Optional[List[str]] = None,
) -> str:
    pattern = re_compile(r"(\s+column\s+)'?(.*)", IGNORECASE)
    quotechar = "'" if quote_columns else ""

    def replace(match):
        prefix = match.group(1)
        new_column_name = match.group(2).strip("'").lower()

        if ignore_columns_starting_with and any(
            new_column_name.startswith(prefix)
            for prefix in ignore_columns_starting_with
        ):
            pass  # Do not capitalize column names that start with the specified string
        else:
            new_column_name = new_column_name.capitalize()

        return f"{prefix}{quotechar}{new_column_name}{quotechar}"

    return pattern.sub(replace, content)
