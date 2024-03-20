"""
    file: guess_game.py
    @brief: This is the guess game made in python. There are three difficulty Easy, Hard and Extreme.
            In Easy mode you have 5 life,
            In Hard mode you have 3 life,
            In hard mode you have 1 life.

    @author: Bhusan Shrestha
    @python version:3.12
"""
import random


def main(endgame):
    guess = random.randint(1, 10)
    guessed = 1
    for i in range(endgame):
        num = int(input("Guess a number between 1 to 10: "))
        if num == guess:
            print("number found is {} in {} guesses".format(num, guessed))
            break
    
        if guessed == endgame:
            print("Out of moves")
            print("The correct number is:", guess)
        else:
            guessed += 1
            print("wrong guess")


if __name__ == "__main__":
    difficulty = input("Which difficulty you want to choose: (Easy, Hard, Extreme)").lower()
    game = 3
    if difficulty == "easy":
        game = 5
        print("You have 5 chance.")
    elif difficulty == "hard":
        game = 3
        print("You have 3 chance.")
    elif difficulty == "extreme":
        game = 1
        print("You have 1 chance.")
    else:
        print("wrong input")
    main(game)
