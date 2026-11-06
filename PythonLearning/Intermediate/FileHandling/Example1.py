f = open ("sampleABC.txt", "r")
print (f. read())


# Read whole Document
f.read()

# Read - Certain Characters
f.read(5)

# Read line by Line
f.readline()

#Read: Whole File or Line by Line

f = open("sampleABC.txt", "r")     # 1. Open the file in "read" mode  (use - "r") - By default read modes and text files
data = f.read()                    # 2. Read the File  - Whole the document

data = f.read(10)                 # 2. Read Only Parts of the File

print(f.readline())               # 2. Read the File - Line by Line
print(f.readline())

print(type(data))                 # Print the Type of data retrieve from File.

print(data)

f.close()                           # Close the File


with open("sampleABC.txt") as file:       # Alias or second name
    data = file.read()
    print(data)


file = open("sampleABC.txt")
for i in file:
    print(i, end = '')

with open ("sampleABC.txt" , "r") as file:          # Alias or second name
    data = file.read()
print(data)

with open("Demo1.txt" , "w") as file:       # Alias or second name
    file.write("I Love Music and Singing")

