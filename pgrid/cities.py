class Zone(object):
    """
    Class representing a Zone in a citu
    """
    def __init__(self, price):
        self.price = price
        self.owned = False
        self.owner = None

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        if owner:
            self.__owner = owner
            self.owned = True
        else:
            self.__owner = owner

class City(object):
    """
    Class representing a city on the board
    """
    def __init__(self, name):
        self.name = name
        # self.connections = {}
        self.zones = [
            Zone(10),
            Zone(15),
            Zone(20)
        ]

    # def get_connections(self):
    #     return self.connections
    #
    # def get_connection(self, city):
    #     if city in self.connections:
    #         return self.connections[city]
    #     else:
    #         raise ConnectionNotFound('{city} not connected to {me}'.format(city=city.name, me=self.name))
    #
    # def set_connection(self, city, cost):
    #     self.connections[city] = int(cost)

    def has_free_zone(self, phase, player):
        """
        Gets free zones for the current phase and current player in a City
        :param player:
        :return: True/False
        """
        zones = self.zones[:phase]
        player_zones = [zone for zone in zones if zone.owner == player.name]
        for zone in zones:
            if not zone.owned and not player_zones:
                return True
            else:
                continue
        return False

    def __repr__(self):
        return '<City:{name}>'.format(name=self.name)
