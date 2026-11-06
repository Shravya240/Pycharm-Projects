print("Welcome to the ATM!")
option= int(input("Choose an option (1. Check Balance,  2. Withdraw Money): "))
balance= int("100000")
if option == "1":
        print("Your bank balance is $100,000")
else:
        withdraw= int(input("Enter the amount you want to withdraw: "))
        print("Your new bank balance is", balance - withdraw)
