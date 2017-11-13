import csv
import os
from collections import defaultdict

import yaml
from pgrid.engine import dijsktra

from pgrid.cities import City
from pgrid.components import component_path


class CityNotFound(BaseException):
    pass

class ConnectionNotFound(BaseException):
    pass

class Board(object):
    def __init__(self):
        self.cities = {}
        self.connections = defaultdict(list)
        self.connection_costs = {}

        with open(os.path.join(component_path, 'cities.yaml'), 'r') as cities_file:
            cities = yaml.load(stream=cities_file)
            for region, cities in cities.items():
                for city in cities:
                    self.register(City(city))
        with open(os.path.join(component_path, 'connections.csv'), 'r') as connections_file:
            connections = csv.reader(connections_file, delimiter=',')
            for connection in connections:
                from_city = connection[0]
                to_city = connection[1]
                cost = connection[2]
                self.add_connection(from_city, to_city, int(cost))

        self.optimal_connection_map = {city: dijsktra(self, city) for city in self.cities.keys()}

    def add_connection(self, from_city, to_city, cost):
        self.connections[from_city].append(to_city)
        self.connections[to_city].append(from_city)
        self.connection_costs[(from_city, to_city)] = cost
        self.connection_costs[(to_city, from_city)] = cost

    def register(self, city):
        self.cities[city.name] = city

    def find(self, name):
        if name in self.cities:
            return self.cities[name]
        else:
            raise CityNotFound('Could not find {city} on board'.format(city=name))

    def get_connection_cost(self, from_city, to_city):
        return self.optimal_connection_map[from_city][to_city]

