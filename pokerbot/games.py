"""This module contains the Game class."""

from .players import Player

class Game:
    """Represents a game of Poker, and tracks its state."""

    def __init__(self):
        self._players = []


    def __repr__(self):
        return "<Game ({} players)>".format(len(self._players))


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
