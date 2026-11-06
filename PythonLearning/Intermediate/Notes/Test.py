# ********************************************
# TEST 1 - PYTHON FUNDAMENTAL
# ********************************************

# 1. How to Convert Any Number into String
number = 5
# print: 51
# Ans : use Python -IbBuilt Function: str() to convert number to String

number =  5
print(f"\n1. Convert Int to String add 1 to it: , {str(number) + str(1)}")

# 2. How to print length (size ) of the List
# Print : How many element in the list
list = [45,34,23,42,78,94]
print(f"\n2. Total Size of the List : {len(list)}")


# 3. Create a list of three fruits and print each fruit on a new line using a loop
fruits_list = ["Apple", "Banana", "Cherry"]
print("\n3. List of Fruits:  ")
for fruit in fruits_list:
    print(fruit)

# 4. How to Add new number in the list
# Ans use List Methods - append()

print("\n4. Add New Number into the List until you hit 'X' " )
list = []
while True:
    number = input("Enter a number: ")
    if number.lower() == "x":
        print("Thank you. Bye")
        break
    else:
        number = int(number)   # convert to integer
        list.append(number)
        print(f"Current List : {list}" )

# 5. Find Largest Number in the List
print("\n 5. Find Largest Number in the List")
numbers = [45,34,23,89,56]

print("Largest Value(Using max Func) :", max(numbers))
 # Using Loops
largest = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > largest:
        largest = numbers[i]
print("Largest Value(Using loops- range()) :", largest)
# or
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest Value(Using loops - directly list) :", largest)

# 6. Solve the Equation (A+B) * (C+D) using Function  ( need more than more times )
print("\n 6. Solve the Equation (A+B) * (C+D) using Function ")
def sum(x,y):
    return x + y

A = int(input("Enter the A Values: "))
B = int(input("Enter the B Values: "))
C = int(input("Enter the C Values: "))
D = int(input("Enter the D Values: "))

result =  sum(A,B)  * sum(C,D)
print(f"Equation Result:  {result} ")


# 7. Solve the Equation : ((A*B) + (C*D))  + C^2
print("\n 7. Solve the Equation : ((A*B) + (C*D))  + C^2")

def sum(x,y):
    return x + y
def product(x,y):
    return x * y

A = int(input("Enter the A Values: "))
B = int(input("Enter the B Values: "))
C = int(input("Enter the C Values: "))
D = int(input("Enter the D Values: "))

result1  = sum(x= A*B  , y= C * D ) +  C ** 2
result2 =  sum(product(A,B), product(C,D))  +  C**2
result3  = sum(x= product(A,B)  , y= product(C,D) ) +  C ** 2

print(f"Equation Result:  {result1} ")
print(f"Equation Result:  {result2} ")
print(f"Equation Result:  {result3} ")


# 8. Say Hello To User (if name is mentioned Otherwise Say Hello to the User)
print("\n 8. Say Hello To User (if name is mentioned Otherwise Say Hello to the User)")
# Do this by using one Function    (Default Arguments)
#>> Rakhee
#Hello, Rakhee
#>>
#Hello, User

def greet(name = "User"):     # DEfault Arguments
    print(f"Hello, {name}")

greet()
greet("Rakhee")