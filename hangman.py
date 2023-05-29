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