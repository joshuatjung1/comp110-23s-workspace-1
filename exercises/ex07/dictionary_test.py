"""EX07 - Testing Dictionary Functions."""

__author__ = "730578892"

from exercises.ex07.dictionary import invert, favorite_color, count
import pytest


def test_invert_same_key() -> None:
    """Testing to see if 'KeyError' will show up if there are two keys that are the same."""
    with pytest.raises(KeyError):
        my_dictionary = {'danny': 'green', 'gerald': 'green'}
        invert(my_dictionary)


def test_invert_empty_dict() -> None:
    """Testing to see what function returns what is intended with empty dictionary."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_invert() -> None:
    """Testing 'invert' using general keys and values to see basic functioning."""
    test_dict: dict[str, str] = {'a': 'b', 'c': 'd', 'e': 'f'}
    assert invert(test_dict) == {'b': 'a', 'd': 'c', 'f': 'e'}


def test_fav_color_empty() -> None:
    """Testing what happens if an empty dict is entered in."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ""


def test_fav_color() -> None:
    """Testing to see function of 'favorite_color' with 2 of one color, and 1 of every other color."""
    test_dict: dict[str, str] = {'lebron': 'yellow', 'dwyane': 'red', 'chris': 'red', 'ray': 'green'}
    assert favorite_color(test_dict) == 'red'


def test_fav_color_same_frequency() -> None:
    """Testing what happens when there are two colors that have the same number of people that say it is their favorite."""
    test_dict: dict[str, str] = {"George": "red", "Greg": "blue", "Sally": "green", "Bryan": "green", "Grant": "blue"}
    assert favorite_color(test_dict) == "blue"


def test_count() -> None:
    """Testing regular function of count, 2 colors with different frequencies."""
    test_list: list[str] = ["red", "blue", "green", "blue", "green", "blue"]
    assert count(test_list) == {'red': 1, 'blue': 3, 'green': 2} 


def test_count_empty_list() -> None:
    """Testing to see what would happen if imput an empty list."""
    test_list: list[str] = []
    assert count(test_list) == {}


def test_count_only_contains_identical_values_only() -> None:
    """Testing a list that only has identical values."""
    test_list: list[str] = ["lavine", "lavine", "lavine", "lavine", "lavine", "lavine", "lavine", "lavine"]
    assert count(test_list) == {'lavine': 8}