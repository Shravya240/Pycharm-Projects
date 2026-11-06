print("Project #5")
import random

print("Guess A Number Game")
print('''Rules:
1. You will guess an number 1-10
2. The computer will guess another number 1-10
3. If your number matches with the somputer, then you win! If not, then you lose :(
''')

isrunning = True

def choosenum():
    print("Choose a number from 1-10")
    number = input()
    computer = random.randint(1, 10)

    print(computer, ":", number)
    if number == computer:
        print("You won!!!")
    else:
        print("You lost :(")

def main():
    while isrunning:
        print("Do you want to play? (Y/N)")
        choice = input()
        if choice == 'Y':
            print("Let's play!")
            choosenum()
        elif choice == 'N':
            print("Thank you for playing")
            break
        else:
            print("Inavlid Option, Try Again!")

main()