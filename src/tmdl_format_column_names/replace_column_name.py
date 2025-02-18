from re import IGNORECASE
from re import compile as re_compile


def rename_columns(
    content: str,
    quotechar: str = "'",
) -> str:
    pattern = re_compile(r"(\s+column\s+)'?(.*)", IGNORECASE)

    def replace(match):
        prefix = match.group(1)
        new_column_name = (
            quotechar + match.group(2).strip("'").lower().capitalize() + quotechar
        )
        return f"{prefix}{new_column_name}"

    return pattern.sub(replace, content)
