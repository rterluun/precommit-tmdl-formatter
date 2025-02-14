from typing import List

from src.tmdl_formatter.measures.sorting import extract_measures, replace_measures, sort_measures
from tests.conftest import MEASURES_SORTED_IN_STRING


def test_extract_measures(measures_in_string: str, unsorted_measures_in_list):
    assert extract_measures(content=measures_in_string) == unsorted_measures_in_list


def test_sort_measures(unsorted_measures_in_list: List[str], sorted_measures_in_list: List[str]):

    assert sort_measures(measures=unsorted_measures_in_list) == sorted_measures_in_list


def test_replace_measures(measures_in_string: str, sorted_measures_in_list: List[str]):
    assert (
        replace_measures(
            content=measures_in_string,
            measures=sorted_measures_in_list,
        )
        == MEASURES_SORTED_IN_STRING
    )
