import numpy as np


class ParkingLot:

    number: int
    free_lots: int
    paid: bool
    guarded: bool
    p_and_r: bool
    underground: bool

    def __init__(self, number, free_lots, paid, guarded, p_and_r, underground):

        self.number = number
        self.free_lots = free_lots
        self.paid = paid
        self.guarded = guarded
        self.p_and_r = p_and_r
        self.underground = underground

    def __str__(self):

        return f"{self.number = }, {self.free_lots = }, {self.paid = }, {self.guarded = }, {self.p_and_r = }, " \
               f"{self.underground = }"


