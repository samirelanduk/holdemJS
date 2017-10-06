from unittest import TestCase
from unittest.mock import Mock, patch
from pokerbot.games import Game
from pokerbot.players import Player

class GameCreationTests(TestCase):

    def test_can_create_game(self):
        game = Game()
        self.assertEqual(game._players, [])



class GameReprTests(TestCase):

    def test_game_repr(self):
        game = Game()
        game._players = [1, 5, 2, 5]
        self.assertEqual(str(game), "<Game (4 players)>")



class GamePlayerAdditionTests(TestCase):

    def test_can_add_player(self):
        game = Game()
        player = Mock(Player)
        game.add_player(player)
        self.assertEqual(game._players, [player])


    def test_can_only_add_players(self):
        game = Game()
        with self.assertRaises(TypeError):
            game.add_player("player")
