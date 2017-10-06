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


class GamePlayersTests(TestCase):

    def test_can_get_players(self):
        game = Game()
        game._players = [1, 5, 2, 5]
        self.assertEqual(game.players(), (1, 5, 2, 5))



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



class GamePlayerRemovalTests(TestCase):

    def test_can_remove_players(self):
        player1, player2, player3 = Mock(), Mock(), Mock()
        game = Game()
        game._players = [player1, player2, player3]
        game.remove_player(player2)
        self.assertEqual(game._players, [player1, player3])
        game.remove_player(player1)
        self.assertEqual(game._players, [player3])
