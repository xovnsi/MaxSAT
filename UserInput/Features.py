import numpy as np

from DataModel.Generator import Generator
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
    the_best_area: int

    def __init__(self, area, free_lots, paid, guarded, p_and_r, underground, disabled):
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
        wcnf = WCNF()

        # feature numbers 1 - 6
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

        # area chosen by user
        area = areas[user_parking.area]
        area_weight = 1000 // (10 * area.in_need + 5 * area.attractiveness)
        wcnf.append([-7], weight=area_weight)

        # area numbers: 7 - 13
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
            result = np.array(rc2.compute())
            # print(rc2.compute())
            print(f"result {result}")

        return MainSolver.choose_area(areas, result, user_parking)

    @staticmethod
    def choose_area(areas: np.array, solver_result: np.array, user_parking: Features):
        user_area = user_parking.area
        areas_ = [int(areas[user_area].number)]
        lots_areas = {}
        lots_weights = {}

        for p in areas[user_area].parking_lots:
            lots_areas[p] = int(areas[user_area].number)
            lots_weights[p] = 20

        # actual areas' numbers
        for n in areas[user_area].neighbours:
            areas_.append(n)
            for p in areas[n].parking_lots:
                lots_areas[p] = n
                lots_weights[p] = 0

        # indexes for areas in solver: 7 - 13
        for i in range(6, 13):
            if solver_result[i] > 0:
                # best_area = solver_result[i]
                best_area = areas_[i - 6]  # corresponding areas_ number

        print(f"best: {best_area}\n areas: {areas_}")
        print(f"items {lots_areas.items()}")
        print(f"weights {lots_weights.items()}")

        return areas_

    # @staticmethod
    # def choose_parking(best_area: int, neighbours: np.array, lots: np.array):



if __name__ == '__main__':
    areas, parking_lots = Generator.generate_areas(5, 5, 5)
    # for area in areas:
    #     print(area)
    curr_areas = MainSolver.solve(Features.get_info(), areas)
    # MainSolver.choose_parking(res_area, area_neighb, parking_lots)

