from unittest import TestCase
import pokerbot

class PokerTests(TestCase):

    def test_can_play_poker(self):
        # Create players
        matt = pokerbot.Player("Matthew", 1000)
        mark = pokerbot.Player("Mark", 1000)
        luke = pokerbot.Player("Luke", 1000)
        john = pokerbot.Player("John", 1000)

        # Create deck and shuffle it
        deck = pokerbot.Deck()
        self.assertEqual(deck[0].name(), "2♠")
        self.assertEqual(deck[-1].name(), "A♣")
        deck.shuffle()
        # 1 in 2704 chance of this next line failing randomly
        self.assertTrue(deck[0].name() != "2♠" or deck[-1].name() != "A♣")

        # Game setup
        game = pokerbot.Game(deck)
        self.assertIs(game.deck(), deck)
        for player in [matt, mark, luke, john]:
            game.add_player(player)
        self.assertEqual(game.players(), (matt, mark, luke, john))
        game.set_blinds(50, 100)
        self.assertEqual(game.small_blind(), 50)
        self.assertEqual(game.big_blind(), 100)

        # Assign initial dealer
        self.assertIsNone(game.dealer())
        game.assign_dealer()
        self.assertIn(game.dealer(), [matt, mark, luke, john])

        '''# Deal
        game.dealer().deal_cards()
        for player in game.players():
            self.assertEqual(len(player.cards()), 2)'''
