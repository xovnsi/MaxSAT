import numpy as np
import ParkingLot


class Area:
    number: int
    x: int
    y: int
    attractiveness: int
    in_need: int
    neighbours: np.array
    parking_lots: np.array

    ''' 
        in_need: range 0 - 10 
        attractiveness: range 0 - 10
    '''

    def __init__(self, number, x, y, attractiveness, in_need):
        self.number = number
        self.x = x
        self.y = y
        self.attractiveness = attractiveness
        self.in_need = in_need
        self.neighbours = np.empty(8, dtype=np.dtype(object))
        self.parking_lots = np.empty(0, dtype=np.dtype(object))

    # def add_neighbour(self, area):

    def add_parking_lot(self, parking_lot: ParkingLot):
        self.parking_lots = np.append(self.parking_lots, parking_lot)
