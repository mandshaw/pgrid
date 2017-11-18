from collections import defaultdict
from pgrid.powerplant import ResourceType

class Space(object):
    """
    Object representation of of the Market spaces
    """
    LIMITS = {
        ResourceType.COAL : 3,
        ResourceType.OIL : 3,
        ResourceType.GARBAGE : 3,
        ResourceType.URANIUM : 1,
    }

    def __init__(self, cost, uranium_only=False):
        self.cost = cost
        self.resources = {}
        if not uranium_only:
            self.uranium_only = False
            self.resources[ResourceType.OIL] = 0
            self.resources[ResourceType.COAL] = 0
            self.resources[ResourceType.GARBAGE] = 0
        else:
            self.uranium_only = True
        self.resources[ResourceType.URANIUM] = 0

    def is_full(self, type):
        if self.resources[type] == self.LIMITS[type]:
            return True
        else:
            return False


class Market(object):
    """
    The Market on the board composed of a list of spaces
    """
    def __init__(self):
        self.spaces = []
        for i in range(1,9):
            self.spaces.append(Space(i))
        for i in range(10, 18, 2):
            self.spaces.append(Space(i, uranium_only=True))

        self.fill(ResourceType.COAL, 24)
        self.fill(ResourceType.OIL, 18)
        self.fill(ResourceType.GARBAGE, 6)
        self.fill(ResourceType.URANIUM, 2)

    def fill(self, type, quantity):
        """
        Adds resources to the Spaces on the board where there is free space
        :param type:
        :param quantity:
        :return:
        """
        self.spaces.reverse()
        while quantity > 0:
            for space in self.spaces:
                if type is not ResourceType.URANIUM and space.uranium_only:
                    continue
                if not space.is_full(type):
                    while space.resources[type] < space.LIMITS[type] and quantity > 0:
                        space.resources[type] += 1
                        quantity -= 1
        self.spaces.reverse()
