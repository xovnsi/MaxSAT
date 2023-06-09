import numpy as np


class ParkingLot:

    number: int
    free_lots: int
    paid: bool
    guarded: bool
    p_and_r: bool
    underground: bool
    disabled: bool
    area_num: int

    def __init__(self, number, free_lots, paid, guarded, p_and_r, underground, disabled):

        self.number = number
        self.free_lots = free_lots
        self.paid = paid
        self.guarded = guarded
        self.p_and_r = p_and_r
        self.underground = underground
        self.disabled = disabled

    def set_area(self, area_num: int):
        self.area_num = area_num

    def __str__(self):

        return f"number={self.number:3}, free_lots={self.free_lots:3}, paid={self.paid:1}, guarded={self.guarded:1}, " \
               f"p_and_r={self.p_and_r:1}, underground={self.underground:1}, disabled={self.disabled:1}"


