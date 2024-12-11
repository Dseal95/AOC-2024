"""AOC day 11."""

from functools import cache

import numpy as np


@np.vectorize
def blink(elem):
    """Apply blink rules to single arr elem."""
    if elem == "0":
        return "1"
    n = len(elem)
    if n % 2 == 0:
        lhs, rhs = int(elem[: n // 2]), int(elem[n // 2 :])
        return f"{lhs} {rhs}"
    return f"{int(elem)*2024}"


def expand_arr(arr):
    """expand out arr into individual strings."""
    return np.array(np.char.split(arr).sum())


NUM_BLINKS = 75
stones = "5688 62084 2 3248809 179 79 0 172169"

# arr = np.array(stones.split())
# for _ in range(NUM_BLINKS):
# arr = expand_arr(blink(arr))
# print(f"** part 1 = {len(arr.shape[0])} ** [time taken: {time.time() - t_start}s]")


# amazing explanation of @cache decorator: https://www.youtube.com/watch?v=pVfsmQSlVOQ&ab_channel=HyperNeutrino.
# able to use @cache over @lru_cache as we don't need to track usage order, just result.
@cache
def count(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return count(1, steps - 1)
    string = str(stone)
    n = len(string)
    if n % 2 == 0:
        return count(int(string[: n // 2]), steps - 1) + count(
            int(string[n // 2 :]), steps - 1
        )
    return count(stone * 2024, steps - 1)


# using a recursive tree.
arr = [int(x) for x in stones.split()]
print(f"** part 1/2 = {sum(count(stone, NUM_BLINKS) for stone in arr)}")
