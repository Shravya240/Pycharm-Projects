def print_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_info(name="Charlie", city="New York")

#6. Functions with Arbitrary Keyword Arguments (**kwargs):
#The **kwargs syntax allows a function to accept an arbitrary number of keyword arguments. These arguments are collected into a dictionary within the function.
#Python

def print_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_info(name="Charlie", city="New York")
#5. Functions with Arbitrary Positional Arguments (*args):
#The *args syntax allows a function to accept an arbitrary number of positional arguments. These arguments are collected into a tuple within the function.
#Python

def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3)) # Output: 6
print(sum_all(10, 20, 30, 40)) # Output: 100
