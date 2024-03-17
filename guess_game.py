import random
guess = random.randint(1, 10)

guessed = 1
for i in range(1, 4):
    num = int(input("Guess a number between 1 to 10: "))
    if num == guess:
        print("number found is {} in {} guesses".format(num, guessed))
        break
    
    elif guessed == 3:
        print("Out of moves")
        print("The correct number is:", guess)
    
    else:
        guessed += 1
        print("wrong guess")
        
