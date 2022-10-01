import random
from typing import List

from .constants import Game as GameConstants, Player as PlayerConstants
from .errors import MethodNotImplemented


class Player:
    """A black jack player"""
    # Private attributes about a player. Expose them using properties
    _hand:List[int] = []
    _stand: bool = False
    _is_computer: bool = False
    _is_dealer:bool = False
    _name:str = None
    _score: int = 0

    def __init__(self, name=PlayerConstants.COMPUTER_NAME, is_computer = False, is_dealer = False):
        """Initialize a player."""
        self._name = name
        self._is_dealer = is_dealer
        self._is_computer = is_computer

    def __str__(self) -> str:
        """String representation of a player."""
        return f"Player({self._name}, is_computer={self._is_computer}, is_dealer={self._is_dealer})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def stand(self) -> bool:
        """
        Getter for the stand property. 

        This will be used to determine if a player has stood up from the hand.
        They will not be dealt more cards if this is true.
        
        Use this pattern to expose attributes about the class.

        Example:
            if not Player.stand:
                draw_card()
        """
        return self._stand

    @stand.setter
    def stand(self, state_to_set: bool):
        """Setter for the stand property"""
        assert isinstance(state_to_set, bool)
        self._stand = state_to_set

        if state_to_set:
            print(f"{self} is standing")

    @property
    def is_bust(self) -> bool:
        """Used to check if a player has gone bust"""
        return self.score > GameConstants.PERFECT_SCORE

    @property
    def _should_draw(self) -> bool:
        """Logic used by the computer to determine if they should draw."""
        raise MethodNotImplemented()

    @property
    def score(self) -> int:
        """Returns the score of the players hand."""
        return self._score

    @property
    def is_dealer(self) -> bool:
        """Check if the player is a dealer."""
        return self._is_dealer

    def add_card(self, card: int):
        """Draw a card."""
        if self.stand:
            print(f"Player is standing and cannot be dealt a card.")

        elif not self.is_bust():
            self._hand.append(card)
            self._score = sum(self._hand)

        if self.is_bust and self.has_ace:
            index = self._hand.index(GameConstants.ACE)
            self._hand[index] = GameConstants.ACE_1
            print(f"Ace downgraded to 1")

        elif self.is_bust:
            print(f"{self} is bust with a score of: {self.score}")

        self.print_state()
            
    @property
    def has_ace(self):
        return GameConstants.ACE in self._hand


    def print_state(self) -> None:
        """Print the players current important game stats"""
        print(
            f"Player: {self}\n"
            f"Score: {self.score}\n"
            f"Hand: {self._hand}"
        )


    