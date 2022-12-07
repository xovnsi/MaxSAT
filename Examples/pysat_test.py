from pysat.examples.rc2 import RC2
from pysat.formula import WCNF
from DataModel.Generator import Generator
import numpy as np

unsatisfying_clauses = [[1, 2], [-1, 2], [1, -2], [-1, -2]]
satisfying_clauses = [[1, 2], [-1, 2]]
weights_1 = [5, 10, 2, 3]


def solve_sat(clauses):
    wcnf = WCNF()
    for c in clauses:
        wcnf.append(c)

    with RC2(wcnf) as rc2:
        print(f"Solver result: {rc2.compute_()}")

        for m in rc2.enumerate():
            print(f"Found model: {m}")


def solve_max_sat(clauses):
    nr_clauses = 0
    wcnf = WCNF()
    for c in clauses:
        wcnf.append(c, weight=1)
        nr_clauses += 1

    with RC2(wcnf) as rc2:
        rc2.compute()
        max_clauses = nr_clauses - rc2.cost

        for m in rc2.enumerate():
            if max_clauses == nr_clauses - rc2.cost:
                print(f"Found model: {m} Satisfied clauses {nr_clauses - rc2.cost}")
            else:
                break


def solve_weighted_max_sat(clauses, weights):
    if len(clauses) != len(weights):
        raise Exception("You must assign weight to all clauses!")

    max_weight = 0
    wcnf = WCNF()
    for i in range(len(clauses)):
        wcnf.append(clauses[i], weight=weights[i])
        max_weight += weights[i]

    with RC2(wcnf) as rc2:
        rc2.compute()
        max_cost = max_weight - rc2.cost
        for m in rc2.enumerate():
            if max_cost == max_weight - rc2.cost:
                print(f"Found model: {m} Maximised cost: {max_cost}")
            else:
                break


if __name__ == '__main__':

    # areas, parking_lots = Generator.generate_areas(7, 7, 9)

    areas, parking_lots = Generator.read_file("Krakow")

