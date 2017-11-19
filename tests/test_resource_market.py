from unittest import TestCase

from pgrid.resourcemarket import Space, ResourceMarket, ResourceType


class TestResourceMarket(TestCase):

    def test_space(self):
        space = Space(5)

        self.assertEqual(space.cost, 5)
        self.assertEqual(space.resources[ResourceType.COAL], 0)
        self.assertEqual(space.resources[ResourceType.OIL], 0)
        self.assertEqual(space.resources[ResourceType.GARBAGE], 0)
        self.assertEqual(space.resources[ResourceType.URANIUM], 0)
        self.assertEqual(space.LIMITS[ResourceType.COAL], 3)
        self.assertEqual(space.LIMITS[ResourceType.OIL], 3)
        self.assertEqual(space.LIMITS[ResourceType.GARBAGE], 3)
        self.assertEqual(space.LIMITS[ResourceType.URANIUM], 1)


    def test_space_uranium_only(self):
        space = Space(5, uranium_only=True)

        with self.assertRaises(KeyError):
            x = space.resources[ResourceType.COAL]
        with self.assertRaises(KeyError):
            x = space.resources[ResourceType.GARBAGE]
        with self.assertRaises(KeyError):
            x = space.resources[ResourceType.OIL]

        self.assertEqual(space.resources[ResourceType.URANIUM], 0)
        self.assertTrue(space.uranium_only)

    def test_market(self):
        market = ResourceMarket()
        for i in range (1, 9):
            self.assertEqual(market.spaces[i-1].cost, i)
        for i in range(16, 8, -2):
            test_space = market.spaces.pop()
            self.assertTrue(test_space.uranium_only)
            self.assertEqual(test_space.cost, i)

    def test_market_coal_on_init(self):
        market = ResourceMarket()
        for space in market.spaces:
            if not space.uranium_only:
                self.assertEqual(space.resources[ResourceType.COAL], space.LIMITS[ResourceType.COAL])

    def test_market_oil_on_init(self):
        market = ResourceMarket()
        for space in market.spaces:
            if space.cost < 3:
                self.assertEqual(space.resources[ResourceType.OIL], 0)
            elif not space.uranium_only:
                self.assertEqual(space.resources[ResourceType.OIL], space.LIMITS[ResourceType.OIL])

    def test_market_garbage_on_init(self):
        market = ResourceMarket()
        for space in market.spaces:
            if space.cost < 7:
                self.assertEqual(space.resources[ResourceType.GARBAGE], 0)
            elif not space.uranium_only:
                self.assertEqual(space.resources[ResourceType.GARBAGE], space.LIMITS[ResourceType.GARBAGE])

    def test_market_uranium_on_init(self):
        market = ResourceMarket()
        for space in market.spaces:
            if space.cost < 14:
                self.assertEqual(space.resources[ResourceType.URANIUM], 0)
            else:
                self.assertEqual(space.resources[ResourceType.URANIUM], space.LIMITS[ResourceType.URANIUM])


