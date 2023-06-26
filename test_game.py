from Game import Game
import pytest


def test_if_given_letter_is_revealed_in_a_word():
    game = Game(["computer"])
    game.start()
    game.make_turn("u")
    assert game.underscores == "____u___"


def test_if_each_instance_of_a_given_letter_is_revealed():
    game = Game(["cookie"])
    game.start()
    game.make_turn("o")
    assert game.underscores == "_oo___"