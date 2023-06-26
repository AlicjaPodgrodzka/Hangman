import random
from Player import Player


class Game:
    def __init__(self, list_of_words):
        self.player = Player()
        self.words = list_of_words
        self.letters_given = set()
        self.word_to_guess = ""
        self.underscores = ""

    def start(self):
        self.word_to_guess = random.choice(self.words)
        self.underscores = len(self.word_to_guess) * "_"
        print(f"Your word to guess: {self.underscores}")

    def reveal_a_letter(self, letter):
        start = 0
        while True:
            letter_index = self.word_to_guess.find(letter, start)
            if letter_index == -1:
                break
            self.underscores = self.underscores[: letter_index] + letter + self.underscores[letter_index + 1:]
            start = letter_index + 1
        print(self.underscores)
        print(f"Lives remaining: {self.player.lives}")

    def make_turn(self, letter):
        self.letters_given.add(letter)
        print(f"You've given the following letters: {self.letters_given}")
        if letter in self.word_to_guess:
            if letter in self.underscores:
                print("You've already given this letter. Give another one.")
            self.reveal_a_letter(letter)
        else:
            print(self.underscores)
            self.player.lives -= 1
            print(f"This letter is not in the word. Lives remaining: {self.player.lives}")
        print()

    def check_if_there_are_any_letters_to_guess(self):
        if "_" not in self.underscores:
            print("Well done! You guessed the word! ;)")
            return False
        else:
            return True