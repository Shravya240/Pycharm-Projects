print ('hello')
# 1: To Print in the  editor:
print("#1: To Print statement using ")
print("Hello, Friends!")
print('Hello, Friends!')

# 2: To print more than one Objects:
print("#2: To print more than one Objects:")
print("Hello", "how are you?")

# 3: Python “sep” parameter in print()
#The print() function can accept any number of positional arguments. To separate these positional arguments, the keyword argument “sep” is used.
#Note: As sep, end, flush, and file are keyword arguments their position does not change the result of the code.
#This code is showing how we can use the sep argument for multiple variables.

print("#3: Python “sep” parameter in print(): ")
a=12
b=12
c=2022
print(a,b,c,sep="-")

print("#4: Python “end” parameter in print() with and without")
# This line will automatically add a new line before the
# next print statement
print ("Python is the high level language")

# This print() function ends with "**" as set in the end argument.
print ("Python is the high level language", end= "**")
print("Welcome to PyCharm")

print ("namaste")

# 8: How to print "" in Output Statement:
print("# 8: How to print "" in Output Statement:")
print(" \"Namaste\" is \"Hello \" in Hindi ")

print("\" Shravya Gupta\"")
print ('I\'m so happy')

# 9:  Print the statement exactly as written use “””
print("# 9:  Print the statement exactly as written use inside the print function")
print("""
I Love Python 
I Love Programming
I Love People
""")

#10:Python program to print Emojis
print("# 10:Python program to print Emojis")
# There are multiple ways we can print the Emojis in Python. Let’s see how to print Emojis with Unicodes, CLDR names and emoji module.
# Using Unicodes:
# Every emoji has a Unicode associated with it. Emojis also have a CLDR short name, which can also be used.
# From the list of unicodes, replace “+” with “000”. For example – “U+1F600” will become “U0001F600” and prefix the unicode with “\” and print it.

# grinning
print("\U0001f600")
# grinning squinting face
print("\U0001F606")
# rolling on the floor laughing
print("\U0001F923")
# Print emojis in Python
print("\U0001F60D", "\U0001F680", "\U0001F44D")
