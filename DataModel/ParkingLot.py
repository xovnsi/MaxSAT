import numpy as np


class ParkingLot:

    free_lots: int
    paid: bool
    guarded: bool
    p_and_r: bool
    underground: bool

    def __init__(self, free_lots, paid, guarded, p_and_r, underground):

        self.free_lots = free_lots
        self.paid = paid
        self.guarded = guarded
        self.p_and_r = p_and_r
        self.underground = underground


