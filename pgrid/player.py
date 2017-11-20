class InsufficientFundsException(BaseException):
    def __init__(self, player):
        self.message = 'Insufficient funds in account. Available funds are: {funds}'.format(funds=player.balance)
        super(InsufficientFundsException, self).__init__(self.message)

class Player(object):
    """
    Player object.

    Players start off with 50 dollars each
    """
    def __init__(self, name):
        self.name = name
        self.cities = 0
        self.wallet = 50
        self.power_plants = []

    @property
    def balance(self):
        return self.wallet

    @property
    def highest_power_plant(self):
        if len(self.power_plants) > 0:
            return sorted(self.power_plants, key=lambda powerplant: powerplant.cost, reverse=True)[0].cost
        else:
            return 0

    def debit(self, value):
        if value < self.wallet:
            self.wallet -= value
        else:
            raise InsufficientFundsException(self)

    def credit(self, value):
        self.wallet += value

    def add_city(self):
        self.cities += 1

    def add_power_plant(self, power_plant):
        self.power_plants.append(power_plant)
