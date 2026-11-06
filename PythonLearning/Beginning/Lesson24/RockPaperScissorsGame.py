import random as r

isrunning = True
rps = ["Rock", "Paper", "Scissors"]
print('''Rules of Rock Paper Scissors:
1. You will choose either rock, paper or scissors and computer will choose another
2. Rock will beat scissors, Paper will beat rock and scissors will beat paper
3. If the same things are chosen, then it will be a tie
Have fun!!!''')
def play():
    compChoice = r.choice(rps)
    playerChoice = input("Enter Rock, Paper, or Scissors: ").lower().capitalize()
    print("You chose: {playerChoice}")
    print("Computer chose: {compChoice}")
    if playerChoice == compChoice:
        print("It's a tie!!")
    elif (playerChoice == "Rock" and compChoice == "Scissors"):
     print("You win!!")
    elif (playerChoice == "Paper" and compChoice == "Rock"):
        print("You win!!")
    elif (playerChoice == "Scissors" and compChoice == "Paper"):
        print("You win!!!")
    elif playerChoice in rps:
        print("You lose:(")
    else:
        print("Invalid input! Try Again.")

def main():
    while isrunning:
        print("Do you want to play? (Y/N)")
        choice = input()
        if choice == 'Y':
            print("Let's play!")
            play()
        elif choice == 'N':
            print("Thank you for playing")
            break
        else:
            print("Inavlid Option, Try Again!")

main()