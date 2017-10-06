from unittest import TestCase
from pokerbot.games import Game

class GameCreationTests(TestCase):

    def test_can_create_game(self):
        game = Game()
        self.assertEqual(game._players, [])



class GameReprTests(TestCase):

    def test_game_repr(self):
        game = Game()
        game._players = [1, 5, 2, 5]
        self.assertEqual(str(game), "<Game (4 players)>")
