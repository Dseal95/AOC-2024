"""AOC day 7."""

from itertools import product

part1 = False

if part1:
    operators = ["+", "*"]
else:
    operators = ["+", "*", "||"]

with open("data/day7.txt") as f:
    possibly_true_eqs = []
    for e, line in enumerate(f.readlines()):
        test_score, eq = line.strip().split(": ")
        eq = eq.split()
        num_places = len(eq) - 1
        for ops in product(operators, repeat=num_places):
            s = str(eq[0])
            result = 0
            for i, op in enumerate(ops):
                # left-to-right operation.
                if op == "||":
                    result = eval(f"{s}{eq[i + 1]}")
                else:
                    result = eval(f"{s}{op}{eq[i + 1]}")
                s = result
            s = str(eq[0])
            if result == int(test_score):
                possibly_true_eqs.append((e, result))
                break

    # part 1 and 2.
    print(
        f"** part {1 if part1 else 2} answer = {sum([i[1] for i in possibly_true_eqs])} **"
    )
