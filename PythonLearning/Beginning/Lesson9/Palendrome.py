print("Word Palindrome Checker")

word= str(input("Enter a word: "))

if word == (word[::-1]):
    print("This word is a palindrome.")
else:
    print("This word is not a palindrome.")