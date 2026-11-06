# List Comprehension:(Shortcut)
# new_list = [expression for item in iterable if condition]

# Example 1:
# Take Number from 1 to 20 :
# List of All Even Number - **2
# [2,4,6,8,10] = [4,16,36,64,100......]

# Option1 : Regular Way
list = []
for num in range(1,21):
    if num % 2 == 0:
        list.append(num**2)
print(list)

# Option2: With List Comprehension
#Syntax:
#new_list = [expression for item in iterable if condition]
list =[num**2 for num in range(1,21) if num % 2 == 0]
print(list)

# 1. With No Loops & Condition
num = 4
list = [num**2]
print(list)

# With Loops
# Print the  Power of Number till 4:
list = [num**2 for num in range(1,5)]
print(list)

# With Loops & Condition
# Print the  Power of Number till 10 except 3
list = [num**2 for num in range(1,11) if num != 3 ]
print(list)