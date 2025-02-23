from src.tmdl_format_column_names.replace_column_name import rename_columns
from tests.conftest import (
    CAPITALIZED_COLUMN_NAMES,
    EXCLUDED_COLUMNS_STARTING_WITH_CHARACTER,
    EXCLUDED_COLUMNS_WITH_PRESERVED_WORDS,
)


def test_rename_columns(
    columns_in_string: str,
):
    assert rename_columns(content=columns_in_string) == CAPITALIZED_COLUMN_NAMES


def test_rename_columns_ignore_columns_starting_with_character(
    columns_starting_with_character_in_string: str,
):
    assert (
        rename_columns(
            content=columns_starting_with_character_in_string,
            ignore_columns_starting_with=["_", "#_"],
        )
        == EXCLUDED_COLUMNS_STARTING_WITH_CHARACTER
    )


def test_rename_columns_with_preserved_words(
    columns_with_preserved_words: str,
):
    assert (
        rename_columns(
            content=columns_with_preserved_words,
            preserved_words=["VAT"],
        )
        == EXCLUDED_COLUMNS_WITH_PRESERVED_WORDS
    )
