from unittest import TestCase
import pokerbot

class PokerTests(TestCase):

    def test_can_play_poker(self):
        matt = pokerbot.Player("Matthew")
        mark = pokerbot.Player("Mark")
        luke = pokerbot.Player("Luke")
        john = pokerbot.Player("John")

        game = pokerbot.Game()
        for player in [matt, mark, luke, john]:
            game.add_player(player)
        self.assertEqual(game.players(), (matt, mark, luke, john))
