questions = [
    "What is the capital of France?",
    "Which planet is known as the 'Red Planet'?",
    " In which year did the Titanic sink?",
    "Who wrote 'Romeo and Juliet'?",
    "What is the largest mammal in the world?",
    "What is the chemical symbol for gold?",
    "Who painted the Mona Lisa?",
    "What is the powerhouse of the cell?",
    "Which country is known as the 'Land of the Rising Sun'?",
    "Who is the author of the Harry Potter series?",
    
]

answers = [
    "Paris",
    "Mars",
    "1912",
    "William Shakespeare",
    "Blue Whale",
    "Au",
    "Leonardo da Vinci",
    "Mitochondria",
    "Japan",
    "J.K. Rowling"
]

options = [
    "A. Berlin \nB. Paris \nC. Rome \nD. Madrid",
    "A. Venus \nB. Mars \nC. Jupiter \nD. Saturn",
    "A. 1905 \nB. 1912 \nC. 1920 \nD. 1931",
    "A. Charles Dickens \nB. William Shakespeare \nC. Jane Austen \nD. Mark Twain",
    "A. Elephant \nB. Blue Whale \nC. Giraffe \nD. Gorilla",
    "A. Au \nB. Ag \nC. Fe \nD. Cu",
    "A. Vincent van Gogh \nB. Leonardo da Vinci \nC. Pablo Picasso \nD. Michelangelo",
    "A. Nucleus \nB. Mitochondria \nC. Ribosome \nD. Endoplasmic reticulum",
    "A. China \nB. Japan \nC. South Korea \nD. Thailand",
    "A. J.K. Rowling \nB. George R.R. Martin \nC. Stephen King \nD. J.R.R. Tolkien",
]

# main function
def main():
    score: int = 0
    # length = questions.length()
    print("Welcome to quiz game!\n")
    input("Press Enter to start")

    # Loop over all questions
    for i in range(len(questions)):
        print(f"\nQuestion {i + 1}: {questions[i]}")
        print(f"\nOptions : \n{options[i]}")
        answer = input("\nYour answer: ").lower()

        if answer == answers[i].lower():
            print("\nYour answer was correct!")
            score += 1
            
        else:
            print("Your answer was incorrect!")
            print("Answer is "+answers[i])
            
    print("Game is over:")

    print(f"Your score is: {score}/{len(questions)}")
    print("Thanks for playing my quiz game")
# calling main function
main()
