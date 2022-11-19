import numpy as np

from DataModel.ParkingLot import ParkingLot
from DataModel.Generator import Generator
# from UserInput.MainSolver import MainSolver
from pysat.examples.rc2 import RC2
from pysat.formula import WCNF


class Features:
    area: int
    free_lots: int
    paid: bool
    guarded: bool
    p_and_r: bool
    underground: bool
    disabled: bool

    def __init__(self, area,  free_lots, paid, guarded, p_and_r, underground, disabled):
        self.area = area
        self.free_lots = free_lots
        self.paid = paid
        self.guarded = guarded
        self.p_and_r = p_and_r
        self.underground = underground
        self.disabled = disabled

    @staticmethod
    def get_info():
        # free_lots = input("Do you want a parking with at least 10 free lots?")
        # paid = input("Do you want a paid parking?")
        # guarded = input("Do you want a guarded parking?")
        # p_and_r = input("Do you want a park&ride parking?")
        # underground = input("Do you want an underground parking?")
        # disabled = input("Do you want a disabled parking space?")
        area = 17
        paid = False
        guarded = True
        p_and_r = False
        underground = False
        free_lots = False
        disabled = True

        wanted_parking = Features(area, free_lots, paid, guarded, p_and_r, underground, disabled)
        # print(f"{wanted_parking.free_lots} {wanted_parking.paid} {wanted_parking.guarded} {wanted_parking.p_and_r}"
        #       f" {wanted_parking.underground}")

        return wanted_parking


class MainSolver:

    @staticmethod
    def solve(user_parking: Features, areas: np.array):
        max_weight = 0
        wcnf = WCNF()

        if user_parking.paid:
            wcnf.append([1], weight=30)
            wcnf.append([5], weight=10)
        else:
            wcnf.append([-1], weight=40)
            wcnf.append([-2], weight=10)

        if user_parking.guarded:
            wcnf.append([2], weight=40)
            wcnf.append([1], weight=40)
        else:
            wcnf.append([-1], weight=10)
            wcnf.append([-2], weight=20)

        if user_parking.p_and_r:
            wcnf.append([1], weight=10)
            wcnf.append([3], weight=40)
        else:
            wcnf.append([-3], weight=10)

        if user_parking.underground:
            wcnf.append([1, 2], weight=10)
            wcnf.append([4], weight=40)
        else:
            wcnf.append([-4], weight=35)

        if user_parking.free_lots:
            wcnf.append([5], weight=30)
            wcnf.append([1, 4], weight=30)
        else:
            wcnf.append([-5], weight=30)

        if user_parking.disabled:
            wcnf.append([5, 6], weight=45)
        else:
            wcnf.append([-6], weight=15)
            wcnf.append([-5], weight=15)

        area = areas[user_parking.area]
        area_weight = 1000 // (10 * area.in_need + 5 * area.attractiveness)
        wcnf.append([-7], weight=area_weight)

        all_areas = [7]
        for i, num in enumerate(area.neighbours):
            a = areas[num]
            all_areas.append(8 + i)
            area_weight = 1000 // (10 * a.in_need + 5 * a.attractiveness)
            wcnf.append([-(8 + i)], weight=area_weight)

        wcnf.append(all_areas)

        for i in range(len(wcnf.soft)):
            print(f"{wcnf.soft[i]}: {wcnf.wght[i]}")

        with RC2(wcnf) as rc2:
            print(rc2.compute())


if __name__ == '__main__':
    areas, parking_lots = Generator.generate_areas(5, 5, 5)
    for area in areas:
        print(area)
    MainSolver.solve(Features.get_info(), areas)

