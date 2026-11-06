import random

wordlist = ["Road","Chocolate","Hare","Main", "Meter", "Sun", "Dragon"]
def choose():
    word = random.choice(wordlist)
    length = len(word)
    print(length)

def play():
    playerChoice = input("Guess a letter: ").lower().capitalize()
