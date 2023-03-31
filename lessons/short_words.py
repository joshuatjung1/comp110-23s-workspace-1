"""docstring"""
__author__ = "730578892"


def short_words(word_list: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    return_list: list[str] = []
    for word in word_list:
        if len(word) < 5:
            return_list.append(word)
        else:
            print(f"{word} is too long!")
    return return_list

my_list: list[str] = ["sun", "cloud", "sky"]
print(short_words(my_list))
