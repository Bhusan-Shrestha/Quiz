"""
    file: Tic_Tac_Toe.py
    @brief: This is the tic-tac-toe game made in python. There are two player : player 1 and player 2.
            player 1 is (X)
            player 2 is (O)

    @author: Bhusan Shrestha
    @python version:3.12
"""
s = [0, 0, 0]


def board(a):
    print(f"\t\t{a[0]} | {a[1]} | {a[2]}")
    print(f"\t-----------------")
    print(f"\t\t{a[3]} | {a[4]} | {a[5]}")
    print(f"\t-----------------")
    print(f"\t\t{a[6]} | {a[7]} | {a[8]}")


def score(s):
    print(f"Player1 : {s[0]}\nPlayer2 : {s[1]}\nDraw: {s[2]}")


def play_again(s):
    again = input("Do you want to play again? (y / n):").lower()
    if again == "y":
        main()
    else:
        score(s)
        exit()


def play1(player1, player2, s, a, count):
    player1 = int(input("Enter the choice player 1 (X):"))
    if player1 < 9:
        if a[player1] == "X" or a[player1] == "O":
            print("The space is already occupied please choose another value")
            play1(player1, player2, s, a, count)
        else:
            a[player1] = "X"
            board(a)
            if a[0] == a[1] == a[2]:
                print("Player 1 wins")
                s[0] += 1
                play_again(s)
            elif a[0] == a[3] == a[6]:
                print("Player 1 wins")
                s[0] += 1
                play_again(s)
            elif a[2] == a[5] == a[8]:
                print("Player 1 wins")
                s[0] += 1
                play_again(s)
            elif a[6] == a[7] == a[8]:
                print("Player 1 wins")
                s[0] += 1
                play_again(s)
            elif a[0] == a[4] == a[8]:
                print("Player 1 wins")
                s[0] += 1
                play_again(s)
            elif a[2] == a[4] == a[6]:
                print("Player 1 wins")
                s[0] += 1
                play_again(s)
            elif a[3] == a[4] == a[5]:
                print("Player 1 wins")
                s[0] += 1
                play_again(s)
            elif a[6] == a[7] == a[8]:
                print("Player 1 wins")
                s[0] += 1
                play_again(s)
            else:
                for i in range(9):
                    if a[i] == "X" or a[i] == "O":
                        count += 1
                    else:
                        continue
                if count == 9:
                    print("Game is Draw")
                    s[2] += 1
                    play_again(s)
    else:
        print("The value is invalid please choose value between (0 to 8)")
        play1(player1, player2, s, a, count)


    return a


def play2(player1, player2, s, a, count):
    player2 = int(input("Enter the choice player 2 (O):"))
    if player2 < 9:
        if a[player2] == "X" or a[player2] == "O":
            print("The space is already occupied please choose another value")
            play2(player1, player2, s, a, count)
        else:
            a[player2] = "O"
            board(a)
            if a[0] == a[1] == a[2]:
                print("Player 2 wins")
                s[1] += 1
                play_again(s)
            elif a[0] == a[3] == a[6]:
                print("Player 2 wins")
                s[1] += 1
                play_again(s)
            elif a[2] == a[5] == a[8]:
                print("Player 2 wins")
                s[1] += 1
                play_again(s)
            elif a[6] == a[7] == a[8]:
                print("Player 2 wins")
                s[1] += 1
                play_again(s)
            elif a[0] == a[4] == a[8]:
                print("Player 2 wins")
                s[1] += 1
                play_again(s)
            elif a[2] == a[4] == a[6]:
                print("Player 2 wins")
                s[1] += 1
                play_again(s)
            elif a[3] == a[4] == a[5]:
                print("Player 1 wins")
                s[0] += 1
                play_again(s)
            elif a[6] == a[7] == a[8]:
                print("Player 1 wins")
                s[0] += 1
                play_again(s)
            else:
                for i in range(9):
                    if a[i] == "X" or a[i] == "O":
                        count += 1
                    else:
                        continue
                if count == 9:
                    print("Game is Draw")
                    s[2] += 1
                    play_again(s)
    else:
        print("The value is invalid please choose value between (0 to 8)")
        play2(player1, player2, s, a, count)

    return a


def main():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    global s
    count = 0
    board(a)
    player1 = 0
    player2 = 0
    for i in range(9):
        a = play1(player1, player2, s, a, count)
        a = play2(player1, player2, s, a, count)


if __name__ == "__main__":
    print("Let's play Tic Tac Toe Game")
    main()
else:
    pass
