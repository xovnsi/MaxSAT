import numpy as np
from DataModel.Area import Area
from DataModel.ParkingLot import ParkingLot


class Generator:

    @staticmethod
    def generate_areas(x: int, y: int, parking_num: int) -> np.array:

        num = 0
        areas = np.empty((x, y), dtype=np.dtype(Area))
        attr = np.random.randint(10, size=(x, y))
        in_need = np.random.randint(10, size=(x, y))

        for i in range(x):
            for j in range(y):
                area = Area(num, i, j, attr[i][j], in_need[i][j])
                areas[i][j] = area
                num += 1

        for i in range(x):
            for j in range(y):
                if i < x - 1:
                    areas[i][j].add_neighbour(areas[i + 1][j])
                if i > 0:
                    areas[i][j].add_neighbour(areas[i - 1][j])
                if j < y - 1:
                    areas[i][j].add_neighbour(areas[i][j + 1])
                if j > 0:
                    areas[i][j].add_neighbour(areas[i][j - 1])
                if i < x - 1 and j < y - 1:
                    areas[i][j].add_neighbour(areas[i + 1][j + 1])
                if i > 0 and j < y - 1:
                    areas[i][j].add_neighbour(areas[i - 1][j + 1])
                if i < x - 1 and j > 0:
                    areas[i][j].add_neighbour(areas[i + 1][j - 1])
                if i > 0 and j > 0:
                    areas[i][j].add_neighbour(areas[i - 1][j - 1])

        parking_lots = Generator.generate_parking_lots(parking_num)
        areas = areas.flatten()

        for parking_lot in parking_lots:
            random_area = np.random.randint(0, x*y, dtype=np.int16)
            areas[random_area].parking_lots = np.append(areas[random_area].parking_lots, parking_lot)

        # Generator.save_to_file(parking_lots, areas)

        return areas, parking_lots

    @staticmethod
    def generate_parking_lots(num: int) -> np.array:

        free_lots = np.random.randint(50, size=(num,))
        paid = np.random.randint(2, size=(num,), dtype=np.bool)
        guarded = np.random.randint(2, size=(num,), dtype=np.bool)
        p_and_r = np.random.randint(2, size=(num,), dtype=np.bool)
        underground = np.random.randint(2, size=(num,), dtype=np.bool)
        parking_lots = np.empty((num,), dtype=np.dtype(ParkingLot))

        for i in range(num):
            parking_lot = ParkingLot(i, free_lots[i], paid[i], guarded[i], p_and_r[i], underground[i])
            parking_lots[i] = parking_lot

        return parking_lots

    @staticmethod
    def save_to_file(lots_: np.array, areas_: np.array):
        f = open("../Data/Lots.txt", "w")
        for lot in lots_:
            f.write(str(lot) + '\n')
        f.close()

        f = open("../Data/Areas.txt", "w")
        for a in areas_:
            f.write(str(a) + '\n')
        f.close()

