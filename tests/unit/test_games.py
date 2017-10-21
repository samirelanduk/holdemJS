from unittest import TestCase
from unittest.mock import Mock, patch
from pokerbot.games import Game
from pokerbot.players import Player
from pokerbot.cards import Deck

class GameTest(TestCase):

    def setUp(self):
        self.deck = Mock(Deck)


class GameCreationTests(GameTest):

    def test_can_create_game(self):
        game = Game(self.deck)
        self.assertIs(game._deck, self.deck)
        self.assertEqual(game._players, [])
        self.assertIsNone(game._dealer)
        self.assertEqual(game._small_blind, 0)
        self.assertEqual(game._big_blind, 0)


    def test_deck_must_be_deck(self):
        with self.assertRaises(TypeError):
            Game("deck")



class GameReprTests(GameTest):

    def test_game_repr(self):
        game = Game(self.deck)
        game._players = [1, 5, 2, 5]
        self.assertEqual(str(game), "<Game (4 players)>")



class GameDeckTests(GameTest):

    def test_game_deck(self):
        game = Game(self.deck)
        self.assertIs(game.deck(), game._deck)



class GamePlayersTests(GameTest):

    def test_can_get_players(self):
        game = Game(self.deck)
        game._players = [1, 5, 2, 5]
        self.assertEqual(game.players(), (1, 5, 2, 5))



class GamePlayerAdditionTests(GameTest):

    def test_can_add_player(self):
        game = Game(self.deck)
        player = Mock(Player)
        game.add_player(player)
        self.assertEqual(game._players, [player])


    def test_can_only_add_players(self):
        game = Game(self.deck)
        with self.assertRaises(TypeError):
            game.add_player("player")



class GamePlayerRemovalTests(GameTest):

    def test_can_remove_players(self):
        player1, player2, player3 = Mock(), Mock(), Mock()
        game = Game(self.deck)
        game._players = [player1, player2, player3]
        game.remove_player(player2)
        self.assertEqual(game._players, [player1, player3])
        game.remove_player(player1)
        self.assertEqual(game._players, [player3])



class GameDealerTests(GameTest):

    def test_game_dealer(self):
        game = Game(self.deck)
        self.assertIs(game._dealer, game.dealer())



class GameDealerAssigningTests(GameTest):

    @patch("random.choice")
    def test_game_dealer_picking(self, mock_choice):
        game = Game(self.deck)
        player1, player2, player3 = Mock(), Mock(), Mock()
        game._players = [player1, player2, player3]
        mock_choice.return_value = player2
        self.assertIsNone(game._dealer)
        game.assign_dealer()
        mock_choice.assert_called_with([player1, player2, player3])
        self.assertIs(game._dealer, player2)



class GameSmallBlindTests(GameTest):

    def test_game_small_blind(self):
        game = Game(self.deck)
        game._small_blind = 9
        self.assertIs(game._small_blind, game.small_blind())



class GameBigBlindTests(GameTest):

    def test_game_small_blind(self):
        game = Game(self.deck)
        game._big_blind = 9
        self.assertIs(game._big_blind, game.big_blind())



class GameBlindsTests(GameTest):

    def test_can_set_blinds(self):
        game = Game(self.deck)
        game.set_blinds(60, 120)
        self.assertEqual(game._small_blind, 60)
        self.assertEqual(game._big_blind, 120)


