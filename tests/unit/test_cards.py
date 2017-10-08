from unittest import TestCase
from unittest.mock import Mock, patch
from pokerbot.cards import Card

class CardCreationTests(TestCase):

    def test_can_create_card(self):
        card = Card(4, "♥")
        self.assertEqual(card._rank, 4)
        self.assertEqual(card._suit, "♥")


    def test_card_rank_must_be_int(self):
        with self.assertRaises(TypeError):
            Card("f", "♥")


    def test_card_rank_must_be_within_range(self):
        with self.assertRaises(ValueError):
            Card(1, "♥")
        with self.assertRaises(ValueError):
            Card(15, "♥")


    def test_card_face_must_be_str(self):
        with self.assertRaises(TypeError):
            Card(10, 2)


    def test_card_face_must_be_valid(self):
        with self.assertRaises(ValueError):
            Card(11, "4")



class CardReprTests(TestCase):

    @patch("pokerbot.cards.Card.name")
    def test_card_repr(self, mock_name):
        mock_name.return_value = "NAME"
        card = Card(4, "♥")
        self.assertEqual(str(card), "<Card (NAME)>")



class CardRankTests(TestCase):

    def test_card_rank(self):
        card = Card(4, "♥")
        self.assertIs(card._rank, card.rank())



class CardSuitTests(TestCase):

    def test_card_suit(self):
        card = Card(4, "♥")
        self.assertIs(card._suit, card.suit())



class CardNameTests(TestCase):

    def test_card_name(self):
        card = Card(4, "♥")
        self.assertEqual(card.name(), "4♥")


    def test_face_name(self):
        card = Card(11, "♥")
        self.assertEqual(card.name(), "J♥")
        card = Card(12, "♥")
        self.assertEqual(card.name(), "Q♥")
        card = Card(13, "♥")
        self.assertEqual(card.name(), "K♥")


    def test_ace_name(self):
        card = Card(14, "♥")
        self.assertEqual(card.name(), "A♥")
