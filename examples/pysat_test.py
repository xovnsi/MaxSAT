from pysat.examples.rc2 import RC2
from pysat.formula import WCNF

unsatisfying_clauses = [[1, 2], [-1, 2], [1, -2], [-1, -2]]
satisfying_clauses = [[1, 2], [-1, 2]]


def solve_sat(clauses):
    wcnf = WCNF()
    for c in clauses:
        wcnf.append(c)

    with RC2(wcnf) as rc2:
        print(f"Solver result: {rc2.compute_()}")

        for m in rc2.enumerate():
            print(f"Found model: {m}")


def solve_max_sat(clauses):
    wcnf = WCNF()
    for c in clauses:
        wcnf.append(c, weight=1)

    with RC2(wcnf) as rc2:
        # rc2.compute()
        print(f"MaxSAT solver result: {rc2.compute()}")


if __name__ == '__main__':
    # solve_sat(unsatisfying_clauses)
    # solve_sat(satisfying_clauses)

    solve_max_sat(unsatisfying_clauses)
    solve_max_sat(satisfying_clauses)
