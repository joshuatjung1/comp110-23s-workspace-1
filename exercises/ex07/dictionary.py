"""EX07 - Dictionary Functions."""

__author__ = "730578892"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Switches the key and the value for all rows."""
    return_dict: dict[str, str] = {}
    dict2: dict[str, str] = {}
    for key in dict1:
        if dict1[key] in dict2:
            raise KeyError
        else:
            dict2[dict1[key]] = 1
    for key in dict1:
        return_dict[dict1[key]] = key
    return return_dict


def favorite_color(dict1: dict[str, str]) -> str:
    """Returns a str of the favorite color that appears most frequently. If tie, returns the color that appeared in the dictionary first."""
    dict2: dict[str, int] = {}
    return_color: str = ""
    count: int = 0
    for name in dict1:
        if dict1[name] in dict2:
            dict2[dict1[name]] += 1
        else:
            dict2[dict1[name]] = 1
    for color in dict2:
        if dict2[color] > count:
            count = dict2[color]
            return_color = color
    return return_color        
        

def count(list1: list[str]) -> dict[str, int]:
    """Key of return dict is the values of list, and values of return dict are the frequency of the values in the list."""
    return_dict: dict[str, int] = {}
    for item in list1:
        if item in return_dict:
            return_dict[item] += 1
        else:
            return_dict[item] = 1
    return return_dict
