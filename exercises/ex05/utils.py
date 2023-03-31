"""EX05 - Utils."""

__authors__ = "730578892"


def only_evens(number_list: list[int]) -> list[int]:
    """Picks out only the evens out of the list."""
    idx = 0
    even_list: list = []
    while idx < len(number_list):
        if number_list[idx] % 2 == 0:
            even_list.append(number_list[idx])
        idx += 1
    return even_list


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Combines the two lists."""
    combined_list: list = []
    idx: int = 0
    while idx < len(list1):
        combined_list.append(list1[idx])
        idx += 1
    idx = 0
    while idx < len(list2):
        combined_list.append(list2[idx])
        idx += 1
    return combined_list


def sub(number_list: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Will put numbers of list in between start_idx and end_idx in another list, includes the start but not the end."""
    return_list: list = []
    if start_idx < 0:
        start_idx = 0
    
    if end_idx > len(number_list):
        end_idx = len(number_list)
    if len(number_list) == 0 or end_idx < 0 or len(number_list) == start_idx:
        return return_list
    
    while start_idx < end_idx:
        return_list.append(number_list[start_idx])
        start_idx += 1
    return return_list