from src.tmdl_format_column_names.replace_column_name_references import (
    get_column_names,
    rename_column_names_in_measure_file,
)
from tests.conftest import COLUMN_NAMES_CHANGES_IN_MEASURES


def test_get_column_names(columns_in_string):
    assert get_column_names(content=columns_in_string) == [
        "'my_table'[street name]",
        "'my_table'[city name]",
        "'my_table'[AREA name]",
    ]


def test_rename_column_names_in_measure_file(measures_with_column_references):
    assert (
        rename_column_names_in_measure_file(
            content=measures_with_column_references,
            column_names=["'my_table'[Street name]"],
        )
        == COLUMN_NAMES_CHANGES_IN_MEASURES
    )
