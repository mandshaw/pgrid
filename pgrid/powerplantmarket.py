import os
import yaml
from pgrid.powerplant import PowerPlant, ResourceType
from pgrid.components import component_path
from random import shuffle
from collections import deque

class PowerPlantMarket(object):

    def __init__(self):
        self.power_plants= []
        with open(os.path.join(component_path, 'powerplants.yaml')) as power_plants_file:
            power_plants = yaml.load(stream=power_plants_file)
            for power_plant in power_plants['powerplants']:
                self.power_plants.append(
                    PowerPlant(power_plant['Type'], power_plant['Efficiency'], power_plant['Power'], power_plant['Cost']))

        self.shuffle_power_plants()
        self.current_market = [self.power_plants.pop(0) for i in range(0,4)]
        self.future_market = [self.power_plants.pop(0) for i in range(0,4)]

    def shuffle_power_plants(self):
        power_plants = self.power_plants
        core = [power_plants.pop(0) for i in range(8)]
        # find the Green Power Plant for cost 13. That should be the first card
        for i in range(len(power_plants)):
            if power_plants[i].type == ResourceType.GREEN and power_plants[i].cost == 13:
                first_card = power_plants[i]
                del power_plants[i]
                break
        shuffle(power_plants)
        self.power_plants = list(core) + [first_card] + list(power_plants) + [None]

    def remove_power_plant(self, index=None):
        if index == None:
            removed_power_plant = self.future_market.pop()
            self.power_plants.append(removed_power_plant)
            self.add_power_plant()
        else:
            removed_power_plant = self.current_market.pop(index)
            self.add_power_plant()
            return removed_power_plant

    def add_power_plant(self):
        sorted_markets = sorted(
            self.current_market + self.future_market + [self.power_plants.pop(0)],
            key=lambda x: x.cost,
            reverse=False)
        self.future_market = sorted_markets[4:8]
        self.current_market = sorted_markets[0:8]




