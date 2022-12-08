#!/usr/bin/env python

import fileinput
import numpy as np

inputs = [ line.rstrip() for line in fileinput.input() ]

heights = np.array([[ int(h) for h in input ] for input in inputs])
(h, w) = heights.shape

l = np.empty(heights.shape, np.bool_)
r = np.empty(heights.shape, np.bool_)
u = np.empty(heights.shape, np.bool_)
d = np.empty(heights.shape, np.bool_)

for y in range(h):
    m = -1
    for x in range(w):
        l[y][x] = heights[y][x] > m
        m = max(heights[y][x], m)

for y in range(h):
    m = -1
    for x in reversed(range(w)):
        r[y][x] = heights[y][x] > m
        m = max(heights[y][x], m)

for x in range(w):
    m = -1
    for y in range(h):
        u[y][x] = heights[y][x] > m
        m = max(heights[y][x], m)

for x in range(w):
    m = -1
    for y in reversed(range(h)):
        d[y][x] = heights[y][x] > m
        m = max(heights[y][x], m)

v = l | r | u | d
c = sum([ 1 for x in np.nditer(v) if x ])

print(f"star 15: {c}")
