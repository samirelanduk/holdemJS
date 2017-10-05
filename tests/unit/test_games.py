from unittest import TestCase
from pokerbot.games import Game

class GameCreationTests(TestCase):

    def test_can_create_game(self):
        game = Game()
        self.assertEqual(game._players, [])
