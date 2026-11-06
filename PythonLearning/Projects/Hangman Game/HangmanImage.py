HANGMAN_PICS = [
        '''
      +---+
      |   |
          |
          |
          |
          |
    =========''',
        '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''',
        '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''',
        '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''',
        '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========''',
        '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========''',
        '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ========='''
]


def show_Hangman(attempts):
    print(HANGMAN_PICS[attempts])

# Use this Function to Call on Main Hangman Game Logic
#show_Hangman(5)