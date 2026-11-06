print("Project #1")

# 1. Check the Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit

def balance():   # create Function for balance
    print("MyBalance")
    pass

def deposit(bal):   # create Function for deposit
    print("Enter the amount you want to deposit: ")
    amount = int(input())
    if(amount < 0):
        print("Invalid Amount")
    else:
        bal = bal + amount  #balance += amount

    return bal

def withdraw(bal):    # create Function for withdraw
    print("Enter the amount you want to withdraw: ")
    take = int(input())
    if (take > balance):
        print("Invalid Amount")
    else:
        bal = bal - take

    return bal



print("Bank App Program")
print("-----------------------")
print("Welcome to Bank of America")

isrunning = True
balance = 0  # startValue
while isrunning:
    print("Enter the option you want to proceed:")
    print("1. Check Balance")
    print("2. Deposit ")
    print("3. Withdraw ")
    print("4. Exit ")
    option = int(input())

    if (option == 1):
        print("Your Balance: $", balance)
    elif (option == 2):
        balance = deposit(balance)  # call the functions
        print("Your New Balance: $", balance)
    elif (option == 3):
        balance = withdraw(balance)
        print("Your New Balance: $", balance)
    elif (option == 4):
        isrunning = False
        print("Invalid Option, Try Again!!")
    else:
        print("Invalid Option, Try Again!!")