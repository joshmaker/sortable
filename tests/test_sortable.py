import pytest
from sortable.py import insertion, quicksort, bubble
from sortable.c import (
    bubble as c_bubble,
    insertion as c_insertion,
    quicksort as c_quicksort,
)


sort_algorithms = [
    bubble,
    insertion,
    quicksort,
    c_bubble,
    c_insertion,
    c_quicksort,
]


@pytest.mark.parametrize("sort_algorithm", sort_algorithms)
def test_insertion_empty(sort_algorithm):
    arr = []
    sort_algorithm(arr)
    assert arr == []


@pytest.mark.parametrize("sort_algorithm", sort_algorithms)
def test_single(sort_algorithm):
    arr = [1]
    sort_algorithm(arr)
    assert arr == [1]


@pytest.mark.parametrize("sort_algorithm", sort_algorithms)
def test_list(sort_algorithm):
    arr = [1, 2, 1, 4, 5, 6, 0, 0]
    sort_algorithm(arr)
    assert arr == sorted(arr)


@pytest.mark.parametrize("sort_algorithm", sort_algorithms)
def test_with_key(sort_algorithm):
    arr = ["b", "A", "c", "f", "E", "G", "a"]
    sort_algorithm(arr, key=str.lower)
    assert arr == sorted(arr, key=str.lower)
