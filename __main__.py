from Game import Game
from Words_reader import WordsReader

game = Game(WordsReader().get())
game.start()
while game.player.check_if_player_has_lives() and game.check_if_there_are_any_letters_to_guess():
    letter = input("Give a letter")
    game.make_turn(letter)