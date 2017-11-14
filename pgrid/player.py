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

    @property
    def balance(self):
        return self.wallet

    def debit(self, value):
        if value < self.wallet:
            self.wallet -= value
        else:
            raise InsufficientFundsException(self)

    def credit(self, value):
        self.wallet += value

    def add_city(self):
        self.cities += 1


