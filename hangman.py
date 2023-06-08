'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''

import random

class Hangman:
    def __init__(self, words):
        self.words = words
        self.word = random.choice(self.words)
        self.tries = 6
        self.used_letters = set()
        self.guessed_word = ["_"] * len(self.word)

    def guess(self, letter):
        if letter in self.used_letters:
            print(f"You have already used this letter: {letter}")
            return

        self.used_letters.add(letter)
        
        if letter in self.word:
            for i, l in enumerate(self.word):
                if l == letter:
                    self.guessed_word[i] = letter
                    print(f"Yes! {letter} is in your word")
        else:
            self.tries -= 1
            
    def is_word_guessed(self):
        return ''.join(self.guessed_word) == self.word

    def print_status(self):
        print(f"\nYou have {self.tries} tries left.")
        print(f"Used letters: {' '.join(self.used_letters)}")
        print(f"Word: {' '.join(self.guessed_word)}")


def main():
    words = ["hello", "water", "pencil", "rope", "supercalifragilistico"]
    game = Hangman(words)

    while game.tries > 0 and not game.is_word_guessed():
        game.print_status()

        letter_input = input("Guess a letter: ").lower()

        while not letter_input.isalpha() or len(letter_input) != 1:
            print("Invalid input. Please enter a single English letter.")
            letter_input = input("Guess a letter: ").lower()

        game.guess(letter_input)

        if game.is_word_guessed():
            print(f"You guessed the word {game.word} !")
            break
            
    if game.tries == 0:
        print(f"You've run out of tries. The word was: {game.word}")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == 'y':
        main()

main()

'''
This Python script implements a simple version of the classic game Hangman. Here's a breakdown of its different components:

1. The Hangman class: This is the main class that embodies the game itself. It has several attributes and methods:

Attributes:
self.words: A list of possible words for the game.
self.word: The randomly chosen word from the list that the player needs to guess.
self.tries: The number of attempts a player has to guess the word.
self.used_letters: A set to store the letters that the player has already guessed.
self.guessed_word: A list representation of the word to guess, with underscores for each unknown letter.
Methods:
__init__: Initializes a Hangman game with a word list and sets up the initial state of the game.
guess: This method takes a letter as input, checks if the letter has already been used, and if not, it updates self.used_letters and self.guessed_word or decreases the number of tries depending on whether the guessed letter is in the word.
is_word_guessed: Checks if the player has guessed the word correctly.
print_status: Prints the current status of the game, including the number of tries left, used letters, and the current guessed word.
2. The main function: This function handles the game flow. It does the following:

Initializes the game with a list of words.
Keeps asking for user inputs until either the word is guessed or the tries run out.
Validates the input to ensure it's a single English alphabet letter.
Handles the case of winning (the word is guessed) or losing (the tries run out) the game.
Asks the player if they want to replay the game, and if yes, restarts the game.
3. Execution: The script ends with a call to the main function, starting the game when the script is run.
'''