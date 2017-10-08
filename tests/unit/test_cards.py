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
