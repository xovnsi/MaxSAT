import numpy as np
from DataModel.ParkingLot import ParkingLot


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
        self.neighbours = np.ones(6, dtype=np.int16) * -1
        self.parking_lots = np.empty(0, dtype=np.int16)

    def add_neighbour(self, area):
        x = area.x - self.x
        y = area.y - self.y

        if np.abs(x) > 1 or np.abs(y) > 1:
            return

        if x == 0 and y == 1:
            self.neighbours[0] = area.number
        elif x == 1 and y == 1:
            self.neighbours[1] = area.number
        elif x == 1 and y == 0:
            self.neighbours[2] = area.number
        elif x == 0 and y == -1:
            self.neighbours[3] = area.number
        elif x == -1 and y == 0:
            self.neighbours[4] = area.number
        elif x == -1 and y == 1:
            self.neighbours[5] = area.number

    def __str__(self):
        neighbours = ""
        for n in self.neighbours:
            if n != -1:
                neighbours += " "
                neighbours += str(n)

        parking_lots = ""
        for p in self.parking_lots:
            parking_lots += str(p)
            parking_lots += " "

        return f"{self.number = }, {self.x = }, {self.y = }, {self.attractiveness = }, {self.in_need = }, " \
               f"neighbours ={neighbours}, parking lots = {parking_lots}"

    def get_weight(self, is_chosen=False):
        weight = self.in_need * 10 + self.attractiveness * 5
        return weight
