from unittest import TestCase
from pgrid.powerplantmarket import PowerPlantMarket
from pgrid.powerplant import PowerPlant, ResourceType

class TestPowerPlantMarket(TestCase):

    def test_board_power_plants(self):
        power_plant_market = PowerPlantMarket()

        self.assertEqual(len(power_plant_market.current_market), 4)
        self.assertEqual(power_plant_market.current_market[0].cost, 3)
        self.assertEqual(power_plant_market.current_market[1].cost, 4)
        self.assertEqual(power_plant_market.current_market[2].cost, 5)
        self.assertEqual(power_plant_market.current_market[3].cost, 6)

        self.assertEqual(len(power_plant_market.future_market), 4)
        self.assertEqual(power_plant_market.future_market[0].cost, 7)
        self.assertEqual(power_plant_market.future_market[1].cost, 8)
        self.assertEqual(power_plant_market.future_market[2].cost, 9)
        self.assertEqual(power_plant_market.future_market[3].cost, 10)

        self.assertEqual(len(power_plant_market.power_plants), 35)

        self.assertEqual(power_plant_market.power_plants[0].cost, 13)
        self.assertFalse(
            power_plant_market.power_plants[1].cost == 11 and
            power_plant_market.power_plants[2].cost == 12 and
            power_plant_market.power_plants[3].cost == 14 and
            power_plant_market.power_plants[4].cost == 15 and
            power_plant_market.power_plants[5].cost == 16
        )
        self.assertEqual(power_plant_market.power_plants[-1], None)

    def test_remove_last_power_plant(self):
        power_plant_market = PowerPlantMarket()
        power_plant_market.remove_power_plant()
        self.assertEqual(power_plant_market.power_plants[-1].type, ResourceType.COAL)
        self.assertEqual(power_plant_market.power_plants[-1].cost, 10)
        self.assertEqual(len(power_plant_market.future_market), 4)

    def test_remove_indexed_power_plant(self):
        power_plant_market = PowerPlantMarket()
        removed_power_plant = power_plant_market.remove_power_plant(1)
        self.assertEqual(removed_power_plant.cost, 4)
        self.assertEqual(power_plant_market.current_market[1].cost, 5)
        self.assertEqual(power_plant_market.future_market[3].cost, 13)