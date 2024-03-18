"""
    file: Tic_Tac_Toe.py
    @brief: This is the tic-tac-toe game made in python. There are two player : player 1 and player 2.
            First move of a player is random.

    @author: Bhusan Shrestha
    @python version:3.12
"""
import random
s = [0, 0, 0]


def board(a):  # for the board
    print(f"\t\t{a[0]} | {a[1]} | {a[2]}")
    print(f"\t-----------------")
    print(f"\t\t{a[3]} | {a[4]} | {a[5]}")
    print(f"\t-----------------")
    print(f"\t\t{a[6]} | {a[7]} | {a[8]}")


def score(s, p1, p2):   # For the score
    print(f"{p1} : {s[0]}\n{p2} : {s[1]}\nDraw: {s[2]}")


def play_again(s, p1, p2):    # for the play again
    again = input("Do you want to play again? (y / n):").lower()
    if again == "y":
        main(p1, p2)
    else:
        score(s, p1, p2)
        exit()


def play1(player1, player2, s, a, count, p1, p2, ch1, ch2):   # player 1
    player1 = int(input(f"Enter Your choice {p1} ({ch1}):"))
    if player1 < 9:
        if a[player1] == "X" or a[player1] == "O":
            print("The space is already occupied please choose another value")
            play1(player1, player2, s, a, count, p1, p2, ch1, ch2)
        else:
            a[player1] = ch1
            board(a)
            if a[0] == a[1] == a[2]:
                print(f"{p1} win")
                s[0] += 1
                play_again(s, p1, p2)
            elif a[0] == a[3] == a[6]:
                print(f"{p1} win")
                s[0] += 1
                play_again(s, p1, p2)
            elif a[2] == a[5] == a[8]:
                print(f"{p1} win")
                s[0] += 1
                play_again(s, p1, p2)
            elif a[6] == a[7] == a[8]:
                print(f"{p1} win")
                s[0] += 1
                play_again(s, p1, p2)
            elif a[0] == a[4] == a[8]:
                print(f"{p1} win")
                s[0] += 1
                play_again(s, p1, p2)
            elif a[2] == a[4] == a[6]:
                print(f"{p1} win")
                s[0] += 1
                play_again(s, p1, p2)
            elif a[3] == a[4] == a[5]:
                print(f"{p1} win")
                s[0] += 1
                play_again(s, p1, p2)
            else:
                for i in range(9):
                    if a[i] == "X" or a[i] == "O":
                        count += 1
                    else:
                        continue
                if count == 9:
                    print("Game is Draw")
                    s[2] += 1
                    play_again(s, p1, p2)
    else:
        print("The value is invalid please choose value between (0 to 8)")
        play1(player1, player2, s, a, count, p1, p2, ch1, ch2)

    return a


def play2(player1, player2, s, a, count, p1, p2, ch1, ch2):  # Player 2
    player2 = int(input(f"Enter your choice {p2} ({ch2}):"))
    if player2 < 9:
        if a[player2] == "X" or a[player2] == "O":
            print("The space is already occupied please choose another value")
            play2(player1, player2, s, a, count, p1, p2, ch1, ch2)
        else:
            a[player2] = ch2
            board(a)
            if a[0] == a[1] == a[2]:
                print(f"{p2} win")
                s[1] += 1
                play_again(s, p1, p2)
            elif a[0] == a[3] == a[6]:
                print(f"{p2} win")
                s[1] += 1
                play_again(s, p1, p2)
            elif a[2] == a[5] == a[8]:
                print(f"{p2} win")
                s[1] += 1
                play_again(s, p1, p2)
            elif a[6] == a[7] == a[8]:
                print(f"{p2} win")
                s[1] += 1
                play_again(s, p1, p2)
            elif a[0] == a[4] == a[8]:
                print(f"{p2} win")
                s[1] += 1
                play_again(s, p1, p2)
            elif a[2] == a[4] == a[6]:
                print(f"{p2} win")
                s[1] += 1
                play_again(s, p1, p2)
            elif a[3] == a[4] == a[5]:
                print(f"{p2} win")
                s[0] += 1
                play_again(s, p1, p2)
            else:
                for i in range(9):
                    if a[i] == "X" or a[i] == "O":
                        count += 1
                    else:
                        continue
                if count == 9:
                    print("Game is Draw")
                    s[2] += 1
                    play_again(s, p1, p2)
    else:
        print("The value is invalid please choose value between (0 to 8)")
        play2(player1, player2, s, a, count, p1, p2, ch1, ch2)

    return a


def main(p1, p2):   # main function
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    global s
    count = 0
    play = 0
    player1 = 0
    player2 = 0
    board(a)
    ch1 = random.randint(0, 1)  # for move ( X or O)
    ch2 = "hello"
    if ch1 == 0:
        ch1 = "X"
    elif ch1 == 1:
        ch1 = "O"

    if ch1 == "X":
        ch2 = "O"
    elif ch1 == "O":
        ch2 = "X"

    rand = random.randint(0, 1)  # for 1st move of a player
    if rand == 0:
        play = play1

    elif rand == 1:
        play = play2

    if play == play1:
        for i in range(9):
            a = play1(player1, player2, s, a, count, p1, p2, ch1, ch2)
            a = play2(player1, player2, s, a, count, p1, p2, ch1, ch2)
    elif play == play2:
        for i in range(9):
            a = play2(player1, player2, s, a, count, p1, p2, ch1, ch2)
            a = play1(player1, player2, s, a, count, p1, p2, ch1, ch2)


if __name__ == "__main__":
    print("Let's play Tic Tac Toe Game")
    p1 = input("Enter the name of 1st player: ")
    p2 = input("Enter the name of 2nd player: ")
    main(p1, p2)
else:
    pass
