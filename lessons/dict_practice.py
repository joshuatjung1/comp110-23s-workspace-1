"""LS19: Learning about Dictionaries."""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
    #you can use single quotes in the dict definition if you want
ice_cream["mint"] = 3
    #to add to the dict, use this^^^^

print("After adding mint: ")
print(ice_cream)


ice_cream.pop("mint")
    #used to delete from the dict

print("After removing mint: ")
print(ice_cream)

"""Accessing values"""
print(f"Number of vanilla orders: {ice_cream['vanilla']}")
#for f-string, this is where you switch to single quotes so as to not interfere with the f-string syntax

"""To modify value:"""
ice_cream["vanilla"] += 1
print("After adding 1 vanilla: ")
print(ice_cream)
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

"""How to find if a certain key is within a dict"""
print("mint" in ice_cream)
    #output is a boolean
print("chocolate" in ice_cream)

#YOU CANNOT HAVE KEYS OF THE SAME NAME