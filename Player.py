class Player:
    def __init__(self):
        self.lives = 10

    def check_if_player_has_lives(self):
        if self.lives > 0:
            return True
        else:
            print("You've lost all your lives. You lose :(")
            return False