"""EX03 - Structured Wordle"""

__author__ = "730578892"

def contains_char(word_str: str, single_char: str) -> bool:
    """Determines if string a contains character b in any idx"""

    assert len (single_char) == 1
    idx: int = 0

    while idx < len(word_str):
        if word_str[idx] == single_char:
            return True
        else: idx += 1
    return False

def emojified(word: str, secret: str) -> str:
    """shows green or yellow boxes for secret and word depending on correct letter or not"""
  
    assert len(word) == len(secret)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    idx: int = 0
    alternate: int = 0
    emojis: str = ""
    char_in_word: bool = False
    
    while idx < len(secret):
        if contains_char(secret[idx], word[idx]) is True:
            emojis += GREEN_BOX
        else: 
            if contains_char(secret, word[idx]):
                emojis += YELLOW_BOX
            else:
                emojis += WHITE_BOX

        idx += 1
    
    return emojis

def input_guess(num: int) -> str:
    """Makes sure that inputed word is the correct length"""
    word: str = input(f"Enter a {num} character word: ")
    
    while len(word) != num:
        word = input(f"That wasn't {num} chars! Try again: ")
    return word

def main() -> None:
    """The entrypoint of the program and main game loop"""
    won: bool = False
    turns: int = 0
    secret_word: str = "codes"

    while turns < 6 and not won:
        turns += 1
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(len(secret_word))
        emojis: str = emojified(guess,secret_word) 
        print(emojis)
        if guess == secret_word:
            won = True
    if guess != secret_word:
        print("X/6 - Sorry, try again tomorrow!")
    if turns < 6:
        print(f"You won in {turns}/6 turns!")

if __name__ == "__main__":
    main()