"""AOC day 3."""

import re

line = open("data/day3.txt").read()

_sum1, _sum2 = 0, 0
pattern1 = r"mul\((\d+),(\d+)\)"
pattern2 = r"(mul\(\d+,\d+\)|(?:do|don\'t)\(\))"
matches1 = re.finditer(pattern1, line)
matches2 = re.finditer(pattern2, line)

# part 1.
for op in matches1:
    _sum1 += eval(f"{op.group(1)} * {op.group(2)}")

# part 2.
mult = True
for op in matches2:
    if op[0] == "don't()":
        mult = False
    elif op[0] == "do()":
        mult = True
    else:
        if mult:
            _sum2 += eval(
                f'{op[0].replace("mul(", "").replace(")", "").replace(",", " * ")}'
            )
print(f"** part 1 = {_sum1} **")
print(f"** part 2 = {_sum2} **")
