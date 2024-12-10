"""AOC day 1."""

from collections import Counter

import numpy as np

with open("data/day1.txt") as f:
    l1, l2 = [], []
    for line in f.readlines():
        e1, e2 = line.split()
        l1.append(int(e1))
        l2.append(int(e2))
# part 1.
diff = np.abs(np.array(sorted(l1)) - np.array(sorted(l2)))
print(f"** part 1 = {np.sum(diff)} **")
# part 2.
cnts = Counter(l2)
sim_score = 0
for i in l1:
    sim_score += i * cnts.get(i, 0)
print(f"** part 2 = {sim_score} **")
