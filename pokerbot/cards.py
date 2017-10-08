"""This module contains the Deck and Card classes."""

import random

class Card:
    """Represents a card.

    :param int rank: The number of the card, from 2 to 14.
    :param str face: The face of the card, as a unicode symbol."""

    def __init__(self, rank, suit):
        if not isinstance(rank, int):
            raise TypeError(f"rank {rank} is not int")
        if rank < 2 or rank > 14:
            raise ValueError("rank {rank} is not within 2 - 14")
        if not isinstance(suit, str):
            raise TypeError(f"suit {suit} is not str")
        if suit not in ["♣", "♦", "♥", "♠"]:
            raise ValueError("{suit} is not a valid suit")
        self._rank = rank
        self._suit = suit


    def __repr__(self):
        return "<Card ({})>".format(self.name())


    def rank(self):
        """Returns the card's rank as a number (2 being 2, Jack being 12, Ace
        being 14).

        :rtype: ``int``"""

        return self._rank


    def suit(self):
        """Returns the card's suit as a unicode character.

        :rtype: ``str``"""

        return self._suit


    def name(self):
        """Returns the card's name.

        :rtype: ``str``"""

        rank = self._rank
        rank = str(rank) if 2 <= rank <= 10 else ["J", "Q", "K", "A"][rank - 11]
        return rank + self._suit



class Deck:
    """Represents a deck of cards. Deck will be unshuffled initially."""

    def __init__(self):
        self._cards = []
        for rank in range(2, 15):
            for suit in ["♠", "♥", "♦", "♣"]:
                self._cards.append(Card(rank, suit))


    def __repr__(self):
        return "<Deck ({} cards)>".format(len(self._cards))


    def __getitem__(self, index):
        return self._cards[index]


    def shuffle(self):
        """Randomises the order of cards in the deck."""

        random.shuffle(self._cards)
