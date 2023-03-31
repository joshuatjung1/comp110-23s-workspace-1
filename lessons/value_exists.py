def value_exists(dictionary: dict[str,int], num: int) -> bool:
    """returns blah blah blah"""
    if len(dictionary) == 0:
        return False
    for integer in dictionary:
        if dictionary[integer] == num:
            return True
    return False


