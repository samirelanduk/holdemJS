"""This module contains the Deck and Card classes."""

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



class Deck:
    """Represents a deck of cards. Deck will be unshuffled initially."""

    def __init__(self):
        self._cards = []
        for rank in range(2, 15):
            for suit in ["♠", "♥", "♦", "♣"]:
                self._cards.append(Card(rank, suit))


    def __repr__(self):
        return "<Deck ({} cards)>".format(len(self._cards))
