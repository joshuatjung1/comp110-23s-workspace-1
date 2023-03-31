"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730578892"

secret_word: str = "python"
word: str = input("What is your 6-letter guess? ")
playing: bool = True
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index: int = 0
alternate: int = 0
emoji_guess: str = ""
letter_in_word: bool = False

while playing:
    if len(word) != 6:
        word = input("That was not 6 letters! Try again: ")
    else:
        while index < 6:
            if word[index] == secret_word[index]:
                emoji_guess += GREEN_BOX
            else:
                while letter_in_word is False and alternate < 6:
                    if secret_word[alternate] == word[index]:
                        letter_in_word = True
                        emoji_guess += YELLOW_BOX
                    else:
                        alternate += 1
                if letter_in_word is False:
                    emoji_guess += WHITE_BOX
            index += 1  
            letter_in_word = False
            alternate = 0           

        print(emoji_guess)
        if word != secret_word:
            print("Not quite. Play again soon! ")
            playing = False
        else:
            print("Woo! You got it!")
            playing = False