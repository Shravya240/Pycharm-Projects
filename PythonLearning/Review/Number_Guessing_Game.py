# Question 1 — Guess the Number
# Create a Python program that stores a secret number:

# secret = 7

# Ask the user to guess the number.

# If the guess is correct, print "Correct!"
# If the guess is too high, print "Too high!"
# If the guess is too low, print "Too low!"

# Bonus challenge: Keep asking until the user guesses correctly.

secret = 7
guess = int(input("Guess the number: "))
while guess != secret:
    if guess > secret:
        print("Too high!")
    else:
        print("Too low!")

    guess = int(input("Guess again: "))

print("Correct!")

