#!/usr/bin/env python

import fileinput
import numpy as np
from textwrap import wrap

def calc_path_length(heights, start, end):
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    distance = np.full_like(heights, -1)
    distance[start] = 0

    for step in range(1, heights.size):
        for i in np.argwhere(distance == step - 1):
            for d in directions:
                c = tuple(i + d)
                if c >= (0, 0) and c[0] < heights.shape[0] and c[1] < heights.shape[1]:
                    if distance[c] == -1:
                        if (heights[c] - heights[tuple(i)] <= 1):
                            if c == end:
                                return step
                            distance[c] = step

heights = np.array([
    [ ord(c) for c in line.rstrip() ]
    for line in fileinput.input()
])

start = np.where(heights == ord('S'))
end = np.where(heights == ord('E'))

heights[start] = ord('a')
heights[end] = ord('z')

star23 = calc_path_length(heights, start, end)
print(f"star 23: {star23}")

star24 = calc_path_length(heights, np.where(heights == ord('a')), end)
print(f"star 24: {star24}")
