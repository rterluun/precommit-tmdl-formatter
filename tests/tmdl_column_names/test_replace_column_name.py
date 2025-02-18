from src.tmdl_column_names.replace_column_name import rename_columns
from tests.conftest import CAPITALIZED_COLUMN_NAMES


def test_rename_columns(
    columns_in_string: str,
):
    assert rename_columns(content=columns_in_string) == CAPITALIZED_COLUMN_NAMES
