from itertools import product

from engine import get_cheapest_connection

from pgrid.board import Board

if __name__ == '__main__':
        board = Board()
        combos = product(board.cities.keys(), board.cities.keys())
        for combo in combos:
                print(get_cheapest_connection(board, combo[0], combo[1]))