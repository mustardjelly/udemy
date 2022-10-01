import random
from typing import Iterable, List

from assets.constants import Game as Constants
from assets.player import Player


class Game:
    """The black jack game engine."""

    _players: List[Player] = []
    VALID_CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    VALID_PLAYER_OPTIONS = [Constants.DRAW, Constants.STAND]
    game_cards = []

    def __init__(self, *args):
        """Things to initialize when making a game class"""
        pass

    def deal_game_cards(self):
        """Deal the games cards"""
        self.game_cards = [card for card_suit in [self.VALID_CARDS for _ in range(4)] for card in card_suit]

    def add_players(self, players: Iterable[Player]) -> bool:
        """Add multiple players to a game at once."""
        success = False

        for player in players:
            # assert isinstance(player, Player)
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
                self.deal_card(player)

    def deal_card(self, player: Player) -> None:
        """Deal a card to a single player."""

        card = random.sample(self.VALID_CARDS, 1)[0]

        player.add_card(card)

    def print_game_state(self) -> None:
        """Prints the current game state of each player."""
        for player in self._players:
            player.print_state()

    @staticmethod
    def introduction():
        """Print information about the Black Jack game"""
        print(Constants.LOGO)

    def play(self):
        """Play a game of Black Jack"""
        
        for player in self._players:
            if player.is_dealer:
                dealer = player
                break

        # Deal cards
        self.deal_cards()

        # Take non dealer actions
            # get non dealer players
            # Ask them to act until all are standing
        to_play = [player for player in self._players if not player.is_dealer]
        while to_play:
            for player in to_play:
                result = input(f"Draw(d) or stand(s) {player.name}?\n")
                valid = False
                while not valid:
                    if not result:
                        print("Please use `d` or `s` to enter an option.")
                        result = input(f"Draw(d) or stand(s) {player.name}?\n")
                    
                    if result[0].lower() in self.VALID_PLAYER_OPTIONS:
                        valid = True
                        continue
                    
                if result == Constants.DRAW:
                    self.deal_card(player)
                    if player.is_bust:
                        to_play.remove(player)

                    self.print_game_state()
                    
                elif result == Constants.STAND:
                    player.stand = True
                    to_play.remove(player)

        self.print_game_state()

        # Check if players have lost
        if all([player.is_bust for player in self._players]):
            print("Players have lost")
            return
        
        # Take dealer actions

        print("All players have acted. Dealers move")

        while not dealer.is_bust:
            self.deal_card(dealer)

            if not dealer.should_draw:
                dealer.stand = True
                break

        self.print_game_end_information()

    def restart(self):
        """Reset the game of Black Jack"""
        self.deal_game_cards()
        self.play()

    def _determine_winner(self) -> List[Player]:
        """
        Internal method to determine who won the game.
        
        Returns the winning players.
        """
        score_array = [player.score for player in self._players if player.score <= Constants.PERFECT_SCORE]
        if not score_array:
            return []

        highest_score = max(score_array)

        return [player for player in self._players if player.score == highest_score]

    def print_game_end_information(self) -> None:
        """
        Prints the winner of the game to the console.
        Might also print the sate of the game to the console.
        """
        winners = self._determine_winner()
        
        
        if winners:
            print(f"Congratulations to:")
            if len(winners) == 1:
                winners[0].print_state()
            else:
                for player in winners:
                    player.print_state()
                    print("========")
        else:
            print("No winners!")
