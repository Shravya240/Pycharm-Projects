
# Error : IndexError -- IndexError: string index out of range
# String indexing in Python allows access to individual characters within a string using their position, or index.
# A. Python strings are zero-indexed (0) , meaning the first character is at index 0, the second at index 1, and so on.
# B. Negative indexing can also be used, where -1 refers to the last character, -2 to the second last, and so forth.
# NOTE: To access a character at a specific index, use square brackets [] following the string or string variable.
my_string = "Hello"

print(my_string[0])  # Output: H
print(my_string[4])  # Output: o
print(my_string[-1]) # Output: o

# NOTE: Attempting to access an index outside the string's boundaries will result in an IndexError.

# 1. Indexing  : List, Set, Tuple, Dictionary(key)
# --------------------------------------------------

text = "Python"

print(text[0])  # start
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])  # end
#print(text[6])    # IndexError: string index out of range

# 2. String Indexing - start from 0   example:
print(text[0])              # First Character of String
print(text[5])              # 5th Character of String
print(text[-1])             # last Character of String

reverse_text =text[::-1]     # reverse the string
print(f"My ReverseString: {reverse_text}")