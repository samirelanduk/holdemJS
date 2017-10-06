from unittest import TestCase
from pokerbot.players import Player

class PlayerCreationTests(TestCase):

    def test_can_create_player(self):
        player = Player("Jo")
        self.assertEqual(player._name, "Jo")
        self.assertEqual(player._money, 0)
        self.assertEqual(player._cards, [])


    def test_player_name_must_be_str(self):
        with self.assertRaises(TypeError):
            Player(100)


    def test_can_create_player_with_money(self):
        player = Player("Jo", money=200)
        self.assertEqual(player._name, "Jo")
        self.assertEqual(player._money, 200)
        self.assertEqual(player._cards, [])


    def test_player_money_must_be_int(self):
        with self.assertRaises(TypeError):
            Player("Jo", money="grand")



class PlayerReprTests(TestCase):

    def test_player_repr(self):
        player = Player("Jo", money=200)
        self.assertEqual(str(player), "<Player 'Jo' (200)>")



class VariableNameTests(TestCase):

    def test_can_get_player_name(self):
        player = Player("Jo")
        self.assertIs(player._name, player.name())


    def test_can_update_name(self):
        player = Player("Jo")
        player.name("new name")
        self.assertEqual(player._name, "new name")


    def test_new_name_must_be_str(self):
        player = Player("Jo")
        with self.assertRaises(TypeError):
            player.name(100)
