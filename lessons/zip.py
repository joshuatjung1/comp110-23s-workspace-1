"""Challenge Question 04."""

__author__ = "730578892"

def zip(str_list: list[str], int_list: list[int]) -> dict[str, int]:
    return_dict: dict[str, int] = {}
    idx: int = 0

    if len(str_list) != len(int_list) or len(str_list) == 0:
        return {}

    while idx < len(str_list):
        return_dict[str_list[idx]] = int_list[idx]
        idx += 1
    return return_dict

