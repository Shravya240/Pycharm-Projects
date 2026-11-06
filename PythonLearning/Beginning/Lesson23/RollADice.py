print("Project #3")
import random

def rolladice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print(dice1, ":", dice2)
    if (dice1 == dice2):
        print("You Won!!")
    else:
        print("You Lost!!!")

def main():
    print("Roll a Dice Game")
    isrunning = True

    while isrunning:
        print("Do you want to play? (Y/N)")
        choice = input()

        if choice == 'Y':
            print("Lets play the Game")
            rolladice()
        elif choice == 'N':
            print("Thank you for playing")
isrunning = False

main()