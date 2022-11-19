from DataModel.ParkingLot import ParkingLot
from DataModel.Generator import Generator


class Features:
    free_lots: int
    paid: bool
    guarded: bool
    p_and_r: bool
    underground: bool
    disabled: bool

    def __init__(self, free_lots, paid, guarded, p_and_r, underground, disabled):
        self.free_lots = free_lots
        self.paid = paid
        self.guarded = guarded
        self.p_and_r = p_and_r
        self.underground = underground
        self.disabled = disabled

    @staticmethod
    def get_info():
        free_lots = input("How many free lots you want to be on a parking?")
        paid = input("Do you want a paid parking?")
        guarded = input("Do you want a guarded parking?")
        p_and_r = input("Do you want a park&ride parking?")
        underground = input("Do you want an underground parking?")
        disabled = input("Do you want an disabled parking space?")

        wanted_parking = Features(free_lots, paid, guarded, p_and_r, underground, disabled)
        # print(f"{wanted_parking.free_lots} {wanted_parking.paid} {wanted_parking.guarded} {wanted_parking.p_and_r}"
        #       f" {wanted_parking.underground}")


if __name__ == '__main__':
    Features.get_info()
    Generator.generate_areas(9, 8, 100)

