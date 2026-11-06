with open("Practice.txt" , "w") as file:
    file.write(''' Hi Everyone
 We are learning file I/O
 Using Python
 I like programming in Python.''')

with open("Practice.txt" , "a") as file:
    file.write('''
 Python is fun''')

with open ("Practice.txt" , "r") as file:
    data = file.read()
print(data)