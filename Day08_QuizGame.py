#QUIZ GAME


def question_one():
        score = 0
        print("What does CPU stand for?")
        print("A. Central Processing Unit")
        print("B. Computer Processing Unit")
        print("C. Central Program Unit")
        print("D. Computer Power Unit")

        answer = input("Your answer: ")

        if answer.lower() == "a":
            print("Correct!")
            return 1
        else:
            print("Wrong!")
            return 0

def question_two():


        print("Which language are you currently learning?")
        print("A. Java")
        print("B. Python")
        print("C. C++")
        print("D. HTML")

        answer = input("Your answer: ")

        if answer.lower() == "b":
            print("Correct!")
            return 1
        else:
            print("Wrong!")
            return 0

def question_three():

        print("Which Python data type uses key-value pairs?")
        print("A. Dictionary")
        print("B. List")
        print("C. Strins")
        print("D. Turple")

        answer = input("Your answer: ")

        if answer.lower() == "a":
            print("Correct!")
            return 1
        else:
            print("Wrong!")
            return 0

def question_four():

        print("Which keyword creates a function in Python?")
        print("A. function")
        print("B. create")
        print("C. def")
        print("D. func")

        answer = input("Your answer: ")

        if answer.lower() == "c":
            print("Correct!")
            return 1
        else:
            print("Wrong!")
            return 0
        
def question_five():

        print("What is the capital of Nigeria?")
        print("A. Lagos")
        print("B. Abuja")
        print("C. Sokoto")
        print("D. Adisababa")

        answer = input("Your answer: ")

        if answer.lower() == "b":
            print("Correct!")
            return 1
        else:
            print("Wrong!")
            return 0

while True:
    score = 0

    score += question_one()
    score += question_two()
    score += question_three()
    score += question_four()
    score += question_five()

    percentage = (score / 5) * 100

    print("Score:", score, "/ 5")
    print(f"Percentage: {percentage:.0f}%")

    choice = input("Do you want to play again? (Y/N): ")

    if choice.lower() == "n":
        print("Thanks for playing!")
        break