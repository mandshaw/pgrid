from unittest import TestCase
from pgrid.player import Player, InsufficientFundsException


class TestPlayer(TestCase):

    def test_init(self):
        player = Player('Test')
        self.assertEqual(player.name, 'Test')
        self.assertEqual(player.wallet, 50)
        self.assertEqual(player.balance, 50)
        self.assertEqual(player.cities, 0)

    def test_player_debit(self):
        player = Player('Test')
        player.debit(35)
        self.assertEqual(player.balance, 15)

    def test_player_debit_insufficient_funds(self):
        player = Player('Test')
        with self.assertRaises(InsufficientFundsException) as exc:
            player.debit(55)
        self.assertEqual(exc.exception.message, 'Insufficient funds in account. Available funds are: 50')

    def test_player_credit(self):
        player = Player('Test')
        player.credit(100)
        self.assertEqual(player.balance, 150)

    def test_player_add_city(self):
        player = Player('Test')
        player.add_city()
        player.add_city()
        player.add_city()
        self.assertEqual(player.cities, 3)