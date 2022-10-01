# The main game file we will use.

from assets.game import Game
from assets.player import Player


YES = "y"
NO = "n"


def main():
    """Run the game engine."""
    computer = Player(is_dealer=True, is_computer=True)
    player = Player(name="Sam")
    players = [computer, player]
    game = Game()
    game.add_players(players)
    game.introduction()
    game.play()

    
    while True:
        response = input("Play again (y/n)?\n")
        if not response or response[0].lower() not in [YES, NO]:
            continue

        if response == YES:
            game.restart()
        else:
            break

if __name__ == "__main__":
    main()