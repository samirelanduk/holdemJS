from unittest import TestCase
from unittest.mock import Mock, patch
from pokerbot.cards import Deck, Card

class DeckCreationTests(TestCase):

    @patch("pokerbot.cards.Card")
    def test_can_create_deck(self, mock_card):
        mock_card.side_effect = range(52)
        deck = Deck()
        for rank in range(2, 15):
            for suit in ["♣", "♦", "♥", "♠"]:
                mock_card.assert_any_call(rank, suit)
        self.assertEqual(deck._cards, list(range(52)))



class DeckReprTests(TestCase):

    def test_deck_repr(self):
        deck = Deck()
        self.assertEqual(str(deck), "<Deck (52 cards)>")
