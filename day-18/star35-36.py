#!/usr/bin/env python

import fileinput
import numpy as np

def surface_area(a):
    neighbours = (
        np.roll(a, 1, 0) + np.roll(a, 1, 1) + np.roll(a, 1, 2) +
        np.roll(a, -1, 0) + np.roll(a, -1, 1) + np.roll(a, -1, 2)
    )

    return np.sum(a * (6 - neighbours))

# -1 == !value
# 1 == filled
# 0 == not filled
def flood_fill(a, start, value):
    f = np.where(a == value, 0, -1)
    f[start] = 1
    for i in range(1, 1000000000):
        c = f == i
        if not np.max(c):
            break
        neighbours = (f == 0) & (
            np.roll(c, 1, 0) | np.roll(c, 1, 1) | np.roll(c, 1, 2) |
            np.roll(c, -1, 0) | np.roll(c, -1, 1) | np.roll(c, -1, 2)
        )
        f[neighbours] = i + 1
    return np.sign(f)

def print_fill(a):
    print(np.array2string(a, separator='', max_line_width=200, threshold=999999,
        formatter={'int': lambda a: {-1: '*', 0: '.', 1: ' '}[a] }))

inputs = [ line.rstrip() for line in fileinput.input() ]

droplet = np.zeros((23,23,23), dtype=int)
for input in inputs:
    droplet[tuple([int(x) for x in input.split(",")])] = 1

surface = surface_area(droplet)
print(f"star 35: {surface}")

f = flood_fill(droplet, (0,0,0), 0)
print_fill(f)

inside = surface_area(np.where(f == 0, 1, 0))

print(f"star 36: {surface - inside}")
