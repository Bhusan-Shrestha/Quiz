"""
    file: rock_paper_scissor.py
    @brief: This is the rock paper and scissor game there is 2 players ie: player and computer.
            paper wins rock
            scissor wins paper
            rock wins scissor

    @author: Bhusan Shrestha
    @python version:3.12
"""

import random


def game(a, b, user1, computer, first, second, draw):
    if user1 == computer:
        print("Game is draw.")
        draw += 1

    else:
        if user1 == "rock":
            if computer == "paper":
                print(f"{b} player wins.")
                second += 1

            else:
                print(f"{a} player wins.")
                first += 1

        elif user1 == "paper":
            if computer == "scissor":
                print(f"{b} player wins.")
                second += 1

            else:
                print(f"{a} player wins.")
                first += 1

        elif user1 == "scissor":
            if computer == "rock":
                print(f"{b} player wins.")
                second += 1

            else:
                print(f"{a} player wins.")
                first += 1

    return first, second, draw


def main():
    a = input("Enter the name of the player:")
    b = "Computer"

    first = 0
    second = 0
    draw = 0

    choices = ["rock", "paper", "scissor"]

    ch = "y"

    while ch == "y":
        user1 = input(f"{a} Enter the choice (rock or paper or scissor):").lower()
        computer = random.choice(["rock", "paper", "scissor"])
        print(f"Computer choose : {computer}")

        if user1 in choices:

            first, second, draw = game(a, b, user1, computer, first, second, draw)

            ch = input("\nDo you guys want to play once more ( y / n ):")
            ch.lower()

        else:
            print("\nwrong choice Please choose from rock, paper and scissor\n")

    print(f"\nScore: \n{a} = {first} \n{b} = {second} \ndraw = {draw}")


if __name__ == "__main__":
    print("\nlets play Rock,Paper,Scissor\n")
    main()
