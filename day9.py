"""AOC day 9."""

import copy
import time
from collections import defaultdict

line = open("data/day9.txt").read()
map = defaultdict(lambda: (0, 0))
c = 0
for i in range(0, len(line), 2):
    blk, mem = line[i : i + 2] + "0" if len(line[i : i + 2]) == 1 else line[i : i + 2]
    map[c] = [int(blk), int(mem)]
    c += 1

# part 1.
t_start = time.time()
s = 0
map1 = copy.deepcopy(map)
for k, v in {k: v for k, v in sorted(map1.items(), reverse=True)}.items():
    if s >= k:  # break when you meet in the middle.
        break
    remainder = v[0]
    mem_left = 0
    while remainder != 0:
        # if there is no space at s, move to next s.
        if map[s][1] == 0:
            s += 1
            continue

        # calculate the remainder.
        remainder = remainder - map1[s][1]
        if remainder < 0:
            # overshot.
            # there will still be some space left in s position.
            mem_left = abs(remainder)
            swapped = map1[s][1] - mem_left
            v[0] -= swapped
            map1[s].append([k] * swapped)
            map1[s][1] = mem_left
            remainder = 0
            # don't want to increase s if there is still memory.

        else:
            # filled available space, move to next s.
            swapped = v[0] - remainder
            v[0] = remainder
            map1[s].append([k] * swapped)
            map1[s][1] = mem_left
            s += 1  # move to next spot of memory.

# create the filesystem + compute checked sum.
files = []
for k, v in map1.items():
    for i in [k for _ in range(v[0])] + [item for sublist in v[2:] for item in sublist]:
        files.append(i)
chk_sum = 0
for e, i in enumerate(files):
    chk_sum += e * i

print(f"** part 1 = {chk_sum} ** [time taken: {time.time() - t_start}s]")

# part 2.
t_start = time.time()
map2 = copy.deepcopy(map)
for k, v in {k: v for k, v in sorted(map2.items(), reverse=True)}.items():
    s = 0  # reset pointer for each value.
    mem_to_move = v[0]
    while mem_to_move != 0:
        space_left = map2[s][-1] - mem_to_move
        if space_left >= 0:
            # move works.
            swapped = map2[s][-1] - space_left
            v[0] -= swapped
            map2[s][-1] -= swapped
            map2[s].insert(-1, [k] * swapped)
            mem_to_move = 0  # false update to break while.
            v.insert(1, ["."] * swapped)
            s += 1
        else:
            # try next space.
            s += 1
        if s > (k - 1):
            # can't move, move to next file.
            mem_to_move = 0

# create the filesystem + compute checked sum.
files = []
for k, v in map2.items():
    for e in [k for _ in range(v[0])] + v[1:-1] + [v[-1] * ["."]]:
        if isinstance(e, list):
            for sub_e in e:
                files.append(sub_e)
        else:
            files.append(e)
chk_sum = 0
for e, i in enumerate(files):
    if i != ".":
        chk_sum += e * i

print(f"** part 2 = {chk_sum} ** [time taken: {time.time() - t_start}s]")
