# File handling
# Create the file same folder : Python is great language to build App. Python is also can create web and Game App

# 1. Open the file - open()
# 2. Read the File - Read()  or loops
# 4. Replace the Python Word with Java.
# 5. Close the File - close()


file = open("Review.txt", "x")     #x - create, r - read, w - write a - append
file.write("Python is great language to build App. Python is also can create web and Game App")
file.close
file = open("Review.txt", "r")
content = file.read()
print(content)
content = content.replace("Python", "Java")
file.close()

file = open("Review.txt", "w")
file.write(content)
print(content)
file.close()
