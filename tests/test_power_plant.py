from unittest import TestCase
from pgrid.powerplant import PowerPlant, ResourceType, UnrecognisedResourceException


class TestPowerPlant(TestCase):

    def test_init(self):
        power_plant = PowerPlant('Oil', 3, 6, 32)
        self.assertEqual(power_plant.type, ResourceType.OIL)
        self.assertEqual(power_plant.efficiency, 3)
        self.assertEqual(power_plant.power, 6)
        self.assertEqual(power_plant.cost, 32)

    def test_unrecognised_resource(self):
        with self.assertRaises(UnrecognisedResourceException) as exc:
            power_plant = PowerPlant('Foo', 1, 1, 1)
        self.assertEqual(exc.exception.message, 'Resource type: \'Foo\' is not one of the valid types: COAL, OIL, COMBINED, GARBAGE, URANIUM, GREEN')