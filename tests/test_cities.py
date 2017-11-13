from unittest import TestCase
from unittest.mock import MagicMock, PropertyMock

from pgrid.cities import City


class TestCities(TestCase):

    def test_phase_one_free_zone(self):
        test_city = City('Test')
        player = MagicMock()
        self.assertTrue(test_city.has_free_zone(1,player))

    def test_phase_one_no_free_zone(self):
        test_city = City('Test')
        test_city.zones[0].owner = "Test"
        player = MagicMock()
        self.assertFalse(test_city.has_free_zone(1,player))

    def test_phase_two_first_zone_free(self):
        test_city = City('Test')
        player = MagicMock()
        self.assertTrue(test_city.has_free_zone(2,player))

    def test_phase_two_second_zone_free(self):
        test_city = City('Test')
        test_city.zones[0].owner = "Test"
        player = MagicMock()
        self.assertTrue(test_city.has_free_zone(2,player))

    def test_phase_two_no_free_zone(self):
        test_city = City('Test')
        test_city.zones[0].owner = "Test"
        test_city.zones[1].owner = "Test"
        player = MagicMock()
        self.assertFalse(test_city.has_free_zone(2,player))

    def test_phase_three_first_zone_free(self):
        test_city = City('Test')
        player = MagicMock()
        self.assertTrue(test_city.has_free_zone(3,player))

    def test_phase_three_second_zone_free(self):
        test_city = City('Test')
        player = MagicMock()
        test_city.zones[0].owner = "Test"
        self.assertTrue(test_city.has_free_zone(3,player))

    def test_phase_three_thrid_zone_free(self):
        test_city = City('Test')
        player = MagicMock()
        test_city.zones[0].owner = "Test"
        test_city.zones[1].owner = "Test"
        self.assertTrue(test_city.has_free_zone(3,player))

    def test_phase_three_no_free_zone(self):
        test_city = City('Test')
        player = MagicMock()
        test_city.zones[0].owner = "Test"
        test_city.zones[1].owner = "Test"
        test_city.zones[2].owner = "Test"
        self.assertFalse(test_city.has_free_zone(3,player))

    def test_phase_two_player_already_in_city(self):
        test_city = City('Test')
        player = MagicMock()
        test_city.zones[0].owner = 'test'
        player_name = PropertyMock(return_value='test')
        type(player).name = player_name
        self.assertFalse(test_city.has_free_zone(2, player))

    def test_phase_three_player_already_in_city(self):
        test_city = City('Test')
        player = MagicMock()
        test_city.zones[0].owner = 'test'
        test_city.zones[1].owner = 'test2'
        player_name = PropertyMock(return_value='test')
        type(player).name = player_name
        self.assertFalse(test_city.has_free_zone(3, player))


