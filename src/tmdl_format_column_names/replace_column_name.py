from re import IGNORECASE
from re import compile as re_compile


def rename_columns(
    content: str,
    quote_columns: bool = True,
) -> str:
    pattern = re_compile(r"(\s+column\s+)'?(.*)", IGNORECASE)
    quotechar = "'" if quote_columns else ""

    def replace(match):
        prefix = match.group(1)
        new_column_name = match.group(2).strip("'").lower().capitalize()
        return f"{prefix}{quotechar}{new_column_name}{quotechar}"

    return pattern.sub(replace, content)
