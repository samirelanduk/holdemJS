"""This module contains the Game class."""

class Game:
    """Represents a game of Poker, and tracks its state."""

    def __init__(self):
        self._players = []


    def __repr__(self):
        return "<Game ({} players)>".format(len(self._players))
