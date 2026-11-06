def greet(user):
    return "Hello, " + user + ", Welcome to Akku's Website"

name = input("Enter your name: ")
print(greet(name))

'''
# 2. 1.
What is the primary benefit of using a 'function' in your code?


A.
It allows you to reuse a block of code without typing it again.


B.
It automatically fixes bugs in your script.


C.
It converts your code into a different language.


D.
It makes the computer run faster.

# 3. If you have a list called fruits = ['apple', 'banana', 'cherry'], what command would you use to add 'orange' to the end?


A.
fruits.append('orange')


B.
fruits.add('orange')


C.
fruits + 'orange'


D.
fruits.push_back('orange')

# 4. 
What is a 'parameter' in a function?


A.
A secret password to run the code.


B.
The total number of lines in the function.


C.
The name of the function itself.


D.
An input variable that allows you to pass information into the function.'''

# 5.  List Comprehension:  ShortCut to create List
# Complete the code to create a list of squares
#Expected Output:  [1,4,9,16,25]

numbers = [1,2,3,4,5]                # Create a List
squares = [ n**2 for n in numbers ]  # Traverse through the List : New List
print("ShortCut using List Comprehension:" , squares)      # List with Squares

# Long Way to same things:
numbers = [1,2,3,4,5]
squares = []
for n in numbers:
    ans = n**2
    squares.append(ans)
print("Longway:" , squares)

#6. String Uppercase: Fill the blank to convert a string to uppercase.
#Output:PYTHON PROGRAMMING

text = "python programming"
print(text.upper())

# 7. Length of List: Fill the blank to print the length of the list.
items = ["apple","banana","mango"]
print(len(items))   # len function used to find the length of list/String

#8.  Add Element to List: Complete the code to add an item to the list.
student = ["Yashvi","Shagun"]
student.append("Shravya")
print(student)

#9. Loop Through List: Fill the blank to loop through the list.
numbers = [10,20,30]
for n in numbers:
    print(n, end= ",")

#10.Dictionary Access: Fill the blank to access the value "John".
person = {"name":"John",
          "age":30}
           # Create new Line or use "\n" inside the print
print("\n",person["name"])     # Access the value through Dictionaries Key

# 11.   Create Below Same Function Using Lambda  also:
def sum2(x,y):
    return x + y

print(sum2(56,4))

#Creating the function above using lambda

sum3 = lambda x,y : x+y

print(sum3(6,9))

#12. Import Math Module: Fill the blank to import the math module.
import math
print(math.sqrt(25))

#13. Exception/Errorin the code : You Handle using Try / Except
#Complete the exception handling.

try:
    x = 10 / 2
    print(x)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally :
    print("Clean Job")

#14. Range Function: Fill the blank to print numbers 1–5.
for i in range(1,6):
     print(i)

#15. List Sorting: Fill the blank to sort the list.

numbers = [5,2,9,1]
numbers.sort()
print(numbers)