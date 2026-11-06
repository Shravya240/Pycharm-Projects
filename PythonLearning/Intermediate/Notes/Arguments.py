# A. Set Default Argument in Function
def deposit(balance =0 , amount =0):
    balance = balance + amount
    print("Current Bal:" , balance)

deposit()

# B.Keywords Argument in Function

deposit(1000,300)
deposit(amount= 800, balance= 1000)

# C.Using Global variables in Function
balance = 7000
def deposit1(amount):
    global balance
    balance = balance + amount
    print("New Bal:", balance)

deposit1(500)
deposit1(600)
deposit1(900)


# D. Arbitrary Positional Arguments (*args)
balance1 = 7000
def deposit2(*amount): # Collection Data Types: List, Tuples, Set , Dictiona
    global balance1
    for num in amount:
        balance1 = balance1 + num
    print("New Bal1:", balance1)

deposit2(500, 600, 900,900,560)   # Deposit all three check at same time


# E. Arbitrary Keyword Argument (**args)
def detail_information(**details):   # key:value
    for key, value in details.items():
        print(key ,"- " , value)

detail_information(name="Sharvya", marks = 99)

# PRACTICE PROBLEMS
# Practice 1: Write Function to describe book with details like title, author, year.

# Hardcode Input
# Output:
#title: The Hobbit
#author: Tolkien
#year: 1989

def describe_book(**book):
    pass  # Future Code

describe_book(title= "The Hobbit", author= "Tolkein", year = 1989)

# Practice 2: Write Function Sum_all() that returns the sum of all numeric arguments passed to it.
# Hardcoded Input
# Output:
#Total Value: <Amount>

list = [67,45,35,6,9,8,80]

def sum_all(*num):
    pass #future code


sum_all(67,45,35,6,9,8,80)