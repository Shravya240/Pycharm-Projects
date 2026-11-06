# 1. Indexing  : List, Set, Tuple, Dictionary(key)
# --------------------------------------------------

text = "Python"

print(text[0])  # start
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])  # end
# print(text[6])    # IndexError: string index out of range

for char in text:  # Each Character in the text
    print(char)

print("Length: ", len(text))  # 6

# or

i = 0
while i < len(text):
    print(text[i])
    i += 1  # i = i+1


