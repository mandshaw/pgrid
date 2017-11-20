from unittest import TestCase
from pgrid.player import Player, InsufficientFundsException
from pgrid.powerplant import PowerPlant


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

    def test_add_power_plant(self):
        player = Player('Test')
        power_plant = PowerPlant('Oil', 3, 6, 32)
        player.add_power_plant(power_plant)
        self.assertEqual(len(player.power_plants), 1)
        self.assertEqual(player.power_plants[0], power_plant)

    def test_get_highest_power_plant(self):
        player = Player('Test')
        player.power_plants = [PowerPlant('Oil', 3, 6, 4),PowerPlant('Coal', 3, 6, 34),PowerPlant('Green', 3, 6, 5),PowerPlant('Combined', 3, 6, 7)]
        self.assertEqual(player.highest_power_plant, 34)