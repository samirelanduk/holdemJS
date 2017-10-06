"""This module contains the Player class."""

class Player:
    """Represents a player in a game of Poker.

    :param str name: The player's name.
    :param int money: The money the player starts with.
    :raises TypeError: if name is not a string.
    :raises TypeError: if money is not an integer."""

    def __init__(self, name, money=0):
        if not isinstance(name, str):
            raise TypeError("name {} is not str".format(name))
        if not isinstance(money, int):
            raise TypeError("money {} is not int".format(money))
        self._name = name
        self._money = money
        self._cards = []


    def __repr__(self):
        return "<Player '{}' ({})>".format(self._name, self._money)


    def name(self, name=None):
        """Returns the name of the Player. If a value is given,
        the name will be updated to this (provided it is a string).

        :param str name: If given, this will be made the new name.
        :raises TypeError: if the name given is not a string."""

        if name is None:
            return self._name
        else:
            if not isinstance(name, str):
                raise TypeError("name '{}' is not a str".format(name))
            self._name = name
