def odd_and_even(num_list: list[int]) -> list[int]:
    """Returns a list of odd nums in even idx's"""
    list1: list[int] = []
    list2: list[int] = []
    idx: int = 0
    if len(num_list) == 0:
        return list1
    while idx < len(num_list):
        if idx % 2 == 0:
            list1.append(num_list[idx])
        idx+=1
    for nums in list1:
        if nums % 2 == 1:
            list2.append(nums)
    
    return list2

print(odd_and_even([]))