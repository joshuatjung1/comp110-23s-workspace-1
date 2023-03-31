"""EX06 - Choose Your Own Adventure."""

__author__ = "730578892"

from random import randint

points: int = 105
secret: int = randint(1, 1000)
player: str = ""
idx: int = 77

SKULL_EMOJI: str = "\U0001F480"
CLOWN_EMOJI: str = "\U0001F921"
WIN_EMOJI: str = "\U0001F389"


def greet() -> None:
    """Asks player for name and introduces game."""
    global player
    player = input("Please Enter Your name: ")
    print(f"Hello {player}. Welcome to everyone's favorite game: 'Higher or Lower!' In this game, you will need to guess a random number between 1 and 1000 as fast as possible. You start at 100 points, and you will lose 5 points for every guess. Good Luck!")


def guess(num_guess: int) -> None:
    """Main function that runs the higher/lower game."""
    decision: int = 0
    global idx
    global points

    if num_guess < secret: 
        print(f"Sorry {player}, {num_guess} is less than the secret number {CLOWN_EMOJI}, try again: ")
    elif num_guess > secret:
        print(f"Sorry {player}, {num_guess} is more than the secret number {CLOWN_EMOJI}, try again: ")
      
    if num_guess == secret:
        print(f"{num_guess} is the secret number! Congratulations {player}! Point total: {points} {WIN_EMOJI}{WIN_EMOJI}")
        idx += 1
        decision = int(input("Press 1 to Play again or Press 2 to Quit: "))
        if decision == 2:
            print("See you next time!")
        if decision == 1:
            points = 105
            idx = 77
  

def point_func(prev_points: int) -> int:
    """Function that subtracts points from total."""
    point_total: int = prev_points
    global points
    point_total -= 5 
    points = point_total
    return points


def question() -> int:
    """Function that makes sure that num inputs are within range."""
    num: int = int(input("Choose a number between 1 and 1000: "))

    while num < 1 or num > 1000:
        num = int(input("Outside of range. Try again: "))
    return num


def play() -> None:
    """Main play function that combines the other functions."""
    playing: bool = True
    decision: int = 0
    global idx
    global points
    while playing:
        while points > 0 and idx == 77:
            guess(question())
            point_func(points)
            print(f"Point total: {points}")
        if points <= 0:
            print(f"You Lose {SKULL_EMOJI}")
            decision = int(input("Enter 1 to Play again, enter 2 to Go back to Menu: "))
            if decision == 2:
                playing = False
                points = 105
            if decision == 1:
                idx = 77
                points = 105


def main() -> None:
    """Where everything comes together, has the menu."""
    greet()
    idx: int = int(input("Menu: Press 1 to Play | Press 2 to See Directions | Press 3 to Quit: "))
    global player
    while idx != 3: 
        if idx == 1:
            play()
        elif idx == 2:
            print("When the game prompts you to choose a number between 1 and 1000, type in a number and press enter. The game will tell you whether the number you chose was higher or lower than the secret number. You start out with 100 points and each time you guess incorrectly, you lose 5 points. If you reach 0 points, you lose the game. Good luck! ")
        idx = int(input("Menu: Press 1 to Play | Press 2 to See Directions | Press 3 to Quit: "))
    print(f"See you next time, {player}!")


if __name__ == "__main__":
    main()