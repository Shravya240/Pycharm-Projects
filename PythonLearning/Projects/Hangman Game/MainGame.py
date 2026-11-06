import random
from HangmanImage import show_Hangman
from RandomWords import wordlist

word = random.choice(wordlist)
guessed_letters = []
attempts = 0
max_attempts = 6

print("Welcome to Hangman!")

while attempts < max_attempts:
    show_Hangman(attempts)
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word)
    if "_" not in display_word:
        print("You won! The word was:", word)
        break
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess not in word:
        attempts += 1
        print("Wrong guess!")

if attempts == max_attempts:
    show_Hangman(attempts)
    print("You lost... The word was:", word)
