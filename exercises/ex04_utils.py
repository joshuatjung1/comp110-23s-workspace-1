"""EX04 - 'list' Utility Functions."""

__author__ = "730578892"


def all(number_list: list[int], num: int) -> bool:
    """Determines if x,y,z all equal int."""
    idx: int = 0
    if len(number_list) == 0:
        return False
    while idx < len(number_list):
        if num != number_list[idx]:
            return False
        else:
            idx += 1
    return True


def max(numlist: list[int]) -> int:
    """Finds the largest number in the list."""
    idx: int = 0

    if len(numlist) == 0:
        raise ValueError("max()arg is an empty List")
    
    value: int = numlist[0]

    if len(numlist) == 0:
        raise ValueError("max()arg is an empty List")
    
    while idx < len(numlist):
        if numlist[idx] > value:
            value = numlist[idx]
        idx += 1
    return value


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Determines if the two lists are equal."""
    idx: int = 0
    count: int = 0
    if len(list1) != len(list2):
        return False
    while idx < len(list1):
        if list1[idx] == list2[idx]:
            count += 1
        idx += 1
    if count == len(list1):
        return True
    else:
        return False