from DataModel.ParkingLot import ParkingLot


class Features:

    @staticmethod
    def get_info():
        free_lots = input("How many free lots you want to be on a parking?")
        paid = input("Do you want a paid parking?")
        guarded = input("Do you want a guarded parking?")
        p_and_r = input("Do you want a park&ride parking?")
        underground = input("Do you want an underground parking?")

        wanted_parking = ParkingLot(0, free_lots, paid, guarded, p_and_r, underground)
        print(wanted_parking.free_lots + " " + wanted_parking.paid + " " + wanted_parking.guarded + ' '
              + wanted_parking.p_and_r + " " + wanted_parking.underground)


if __name__ == '__main__':
    Features.get_info()
