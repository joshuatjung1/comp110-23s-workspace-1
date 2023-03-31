"""Testing Functions in 'Utils' File."""

__author__ = "730578892"

from exercises.ex05.utils import only_evens, sub, concat

"""Testing 'only_evens' function."""


def test_only_evens_negative() -> None:
    """Testing for negative numbers."""
    test_list: list[int] = [-5, -2, 1, 4]
    assert only_evens(test_list) == [-2, 4]


def test_only_evens_empty() -> None:
    """Testing for an empty list in 'only_evens' function."""
    test_list: list[int] = []
    assert only_evens(test_list) == []


def test_only_evens_no_evens() -> None:
    """Testing for a list with no evens."""
    test_list: list[int] = [1, 5, 35, 75]
    assert only_evens(test_list) == []


"""Testing 'concat' function."""


def test_concat_dif_length_lists() -> None:
    """Testing to see if 'concat' works with different lengthed lists."""
    test_list: list[int] = [1, 2, 3]
    test_list2: list[int] = [1, 2, 3, 4, 5]
    assert concat(test_list, test_list2) == [1, 2, 3, 1, 2, 3, 4, 5]


def test_concat_empty() -> None:
    """Testing to see if 'concat' works one blank list."""
    test_list1: list[int] = []
    test_list2: list[int] = [1, 3, 4, 7]
    assert concat(test_list1, test_list2) == [1, 3, 4, 7]


def test_concat_identical() -> None:
    """Testing to see if 'concat' works with identical lists."""
    test_list: list[int] = [1, 4, 6, 8]
    assert concat(test_list, test_list) == [1, 4, 6, 8, 1, 4, 6, 8]


"""Testing 'sub' function."""


def test_sub_same_start_and_end() -> None:
    """Testing to see if making the two integers the same number would output an empty list."""
    test_list: list[int] = [1, 2, 3, 4, 5]
    assert sub(test_list, 2, 2) == []


def test_sub_start_negative() -> None:
    """Testing to see if 'sub' will still work with a negative start variable."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7]
    assert sub(test_list, -5, 3) == [1, 2, 3]


def test_sub_end_greater_than_list_length() -> None:
    """Testing to see if 'sub' will work with an end variable greater than the length of the list."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7]
    assert sub(test_list, 3, 99) == [4, 5, 6, 7]