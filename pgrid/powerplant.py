from enum import Enum

class UnrecognisedResourceException(BaseException):
    def __init__(self, resource):
        self.message = 'Resource type: \'{resource}\' is not one of the valid types: {types}'.format(resource=resource, types=', '.join(
            [resource_type.name for resource_type in ResourceType]
        ))
        super(UnrecognisedResourceException, self).__init__(self.message)

class ResourceType(Enum):
    COAL = 1
    OIL = 2
    COMBINED = 3
    GARBAGE = 4
    URANIUM = 5
    GREEN = 6

class PowerPlant(object):
    """
    PowerPlant object representing the Power Plant cards
    """
    def __init__(self, type, efficiency, power, cost):
        if type == 'Coal':
            self.type = ResourceType.COAL
        elif type == 'Oil':
            self.type = ResourceType.OIL
        elif type == 'Combined':
            self.type = ResourceType.COMBINED
        elif type == 'Garbage':
            self.type = ResourceType.GARBAGE
        elif type == 'Uranium':
            self.type = ResourceType.URANIUM
        elif type == 'Green':
            self.type = ResourceType.GREEN
        else:
            raise UnrecognisedResourceException(type)
        self.efficiency = efficiency
        self.power = power
        self.cost = cost