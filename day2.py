"""AOC day 2."""

import numpy as np


def is_safe(arr):
    diff = np.diff(arr)
    return (np.all(diff <= -1) or np.all(diff >= 1)) and np.all(np.abs(diff) <= 3)


with open("data/day2.txt") as f:
    cnt1, cnt2 = 0, 0
    for e, line in enumerate(f.readlines()):
        arr = np.array(line.split(), dtype=int)
        # part 1.
        if is_safe(arr):
            cnt1 += 1
        # part 2.
        else:
            for lvl in range(len(arr)):
                if is_safe(arr=np.concatenate([arr[:lvl], arr[lvl + 1 :]])):
                    cnt2 += 1
                    break
    print(f"** part 1 = {cnt1} **")
    print(f"** part 2 = {cnt1 + cnt2} **")
