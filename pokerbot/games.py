"""This module contains the Game class."""

import random
from .players import Player
from .cards import Deck

class Game:
    """Represents a game of Poker, and tracks its state.

    :param Deck deck: The deck of cards to use."""

    def __init__(self, deck):
        if not isinstance(deck, Deck):
            raise TypeError(f"{deck} is not a Deck")
        self._deck = deck
        self._players = []
        self._dealer = None
        self._small_blind, self._big_blind = 0, 0


    def __repr__(self):
        return "<Game ({} players)>".format(len(self._players))


    def deck(self):
        """Returns the Game's :py:class:`.Deck` of cards.

        :rtype: ``Deck``"""

        return self._deck


    def players(self):
        """Returns the :py:class:`.Player` objects in this game.

        :rtype: ``tuple``"""

        return tuple(self._players)


    def add_player(self, player):
        """Adds a :py:class:`.Player` to the game.

        :param Player player: the player to add.
        :raises TypeError: if the player is not a :py:class:`.Player`."""

        if not isinstance(player, Player):
            raise TypeError("{} is not a Player".format(player))
        self._players.append(player)


    def remove_player(self, player):
        """Removes a :py:class:`.Player` from the game.

        :param Player player: the player to add."""

        self._players.remove(player)


    def dealer(self):
        """Returns the :py:class:`.Player` who is currently the dealer.

        :rtype: ``Player``"""
        
        return self._dealer


    def assign_dealer(self):
        """Picks a random :py:class:`.Player` to be the dealer."""

        self._dealer = random.choice(self._players)


    def small_blind(self):
        """Returns the current small blind amount.

        :rtype: ``int``"""

        return self._small_blind


    def big_blind(self):
        """Returns the current big blind amount.

        :rtype: ``int``"""

        return self._big_blind


    def set_blinds(self, small_blind, big_blind):
        """Sets the small and big blinds.

        :param int small_blind: The small blind.
        :param int big_blind: The big blind."""

        self._small_blind = small_blind
        self._big_blind = big_blind
