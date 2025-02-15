from re import DOTALL
from re import compile as re_compile
from re import search as re_search
from typing import List

MEASURE_REGEX = re_compile(
    r"(\s+measure\s.*?lineageTag: .+?(?:\n\s*annotation PBI_FormatHint = .+?)?\n)",
    DOTALL,
)


def extract_measures(content: str) -> List[str]:

    measures: List[str] = MEASURE_REGEX.findall(content)
    return measures


def sort_measures(measures: List[str]) -> List[str]:

    measures.sort(key=lambda x: re_search(r"measure\s+([^=]+)", x).group(1).lower())  # type: ignore
    return measures


def replace_measures(content: str, measures: List[str]) -> str:

    new_content = MEASURE_REGEX.sub(lambda _: measures.pop(0), content)
    return new_content
