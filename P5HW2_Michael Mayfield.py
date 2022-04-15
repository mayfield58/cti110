# Math Quiz
# 4/15/22
# CTI-110 P5HW2 - Math Quiz
# Michael Mayfield
#




import random
print("Welcome to Math Quiz")
print()


def main():
    menu()

def menu():
    repeat = 1
    choice = 0
    while repeat != 0:
        print("----MENU----")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")
        print()
        print("Please choose one of the menu options: ", end= '')


        choice = input()
        if choice == "1":
             addrandom()
        elif choice == "2":
             subrandom()
        elif choice == "3":
            print("Thank you for playing...")
            print("Bye!!")
            repeat = 0
        else:
            print("Not a valid entry")
            print("Try again")
            repeat = 1

def addrandom():
    keep_going = "yes"
    while keep_going == "yes":
        guess = 1
        num1 = random.randint(0,100)
        num2 = random.randint(0,100)
        correct_answer = num1 + num2
        print(" ",num1)
        print("+",num2)
        answer = int(input("Enter answer. "))
        while answer != correct_answer:
            if answer < correct_answer:
                print("answer too low")
                              
            else:
                print("answer too high")
            guess += 1
            answer = int(input("Try again: "))
        print("Congratulations!!! your answer correct...")
        print("number of guesses: ", guess)
        print()
        keep_going = "no"
                

        

def subrandom():
    keep_going = "yes"
    while keep_going == "yes":
        guess = 1
        num1 = random.randint(50,100)
        num2 = random.randint(1,50)
        correct_answer = num1 - num2
        print(" ",num1)
        print("-",num2)
        answer = int(input("Enter answer. "))
        while answer != correct_answer:
            if answer < correct_answer:
                print("answer too low")
                              
            else:
                print("answer too high")
            answer = int(input("Try again: "))
        print("Congratulations!!! your answer correct...")
        print("number of guesses: ", guess)
        print()
        keep_going = "no"
    
   
    

main()
