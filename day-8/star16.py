#!/usr/bin/env python

import fileinput
import numpy as np

inputs = [ line.rstrip() for line in fileinput.input() ]

heights = np.array([[ int(h) for h in input ] for input in inputs])
(h, w) = heights.shape

l = np.zeros_like(heights)
r = np.zeros_like(heights)
u = np.zeros_like(heights)
d = np.zeros_like(heights)

for y in range(h):
    for x in range(1, w):
        for x2 in reversed(range(x)):
            if heights[y][x2] >= heights[y][x]:
                l[y][x] = x - x2
                break
        else:
            l[y][x] = x

for y in range(h):
    for x in reversed(range(w - 1)):
        for x2 in range(x + 1, w):
            if heights[y][x2] >= heights[y][x]:
                r[y][x] = x2 - x
                break
        else:
            r[y][x] = w - x - 1

for x in range(w):
    for y in range(1, h):
        for y2 in reversed(range(y)):
            if heights[y2][x] >= heights[y][x]:
                u[y][x] = y - y2
                break
        else:
            u[y][x] = y

for x in range(w):
    for y in reversed(range(h - 1)):
        for y2 in range(y + 1, h):
            if heights[y2][x] >= heights[y][x]:
                d[y][x] = y2 - y
                break
        else:
            d[y][x] = h - y - 1

print(l)
print()
print(r)
print()
print(u)
print()
print(d)
print()

s = l * r *  u * d
c = max(np.nditer(s))

print(f"star 16: {c}")
