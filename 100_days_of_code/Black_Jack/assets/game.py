import random
from typing import Iterable, List

from .constants import Game as Constants
from .errors import MethodNotImplemented
from .player import Player


class Game:
    """The black jack game engine."""

    _players: List[Player] = []
    VALID_CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    VALID_PLAYER_OPTIONS = [Constants.DRAW, Constants.STAND]
    game_cards = []

    def __init__(self, *args):
        """Things to initialize when making a game class"""
        for item in args:
            if isinstance(item, Player):
                self.add_player(item)

    def deal_game_cards(self):
        """Deal the games cards"""
        self.game_cards = [card for card_suit in [self.VALID_CARDS for _ in range(4)] for card in card_suit]
                

    def add_player(self, player: Player) -> bool:
        """Add a player to the game. """
        assert isinstance(player, Player)

    def add_players(self, players: Iterable[Player]) -> bool:
        """Add multiple players to a game at once."""
        success = False
        
        assert isinstance(players, Iterable)

        for player in players:
            assert isinstance(player, Player)
            self._players.append(player)

        success = True

        return success

    def get_players(self) -> None:
        """Prints the players in the game."""
        for player in self._players:
            print(player)

    def deal_cards(self) -> None:
        """Deal cards to each player in the game."""
        for player in self._players:
            for _ in range(2):
                player.add_card()

    def deal_card(self, player: Player) -> None:
        """Deal a card to a single player."""
        assert isinstance(player, Player)

        card = random.sample(self.VALID_CARDS)

        player.add_card(card)

    def print_game_state(self) -> None:
        """Prints the current game state of each player."""
        raise MethodNotImplemented()

    @staticmethod
    def introduction():
        """Print information about the Black Jack game"""
        print(Constants.LOGO)

    def play(self):
        """Play a game of Black Jack"""
        play = True
        while play:
            # Deal cards
            self.deal_cards()

            # Take non dealer actions
                # get non dealer players
                # Ask them to act until all are standing
            to_play = [player for player in self._players if not player.is_dealer]
            while to_play:
                for player in to_play:
                    result = input(f"Draw(d) or stand(s) {player.name}?")
                    valid = False
                    while not valid:
                        if not result:
                            print("Please use `d` or `s` to enter an option.")
                            result = input(f"Draw(d) or stand(s) {player.name}?")
                        
                        if result[0].lower() in self.VALID_PLAYER_OPTIONS:
                            valid = True
                            continue
                        
                    if result == Constants.DRAW:
                        self.deal_card(player)
                        if player.is_bust:
                            print(
                                f"{player.name} has gone bust\n"
                            )
                            # print hand
                            
                        self.print_game_state()
                        
                    elif result == Constants.STAND:
                        player.stand = True
                        to_play.remove(player)
                        break

            print("All players have acted. Dealers move")
            self.print_game_state()
            
            # Take dealer actions
            # deterine a winner
            # Ask for reset

            
            raise MethodNotImplemented()

    def restart(self):
        """Reset the game of Black Jack"""
        raise MethodNotImplemented()

    def _determine_winner(self) -> Player:
        """
        Internal method to determine who won the game.
        
        Returns the winning player.
        """
        raise MethodNotImplemented()

    def print_game_end_information(self) -> None:
        """
        Prints the winner of the game to the console.
        Might also print the sate of the game to the console.
        """
        raise MethodNotImplemented()
