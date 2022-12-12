#!/usr/bin/env python

import fileinput
import numpy as np
from textwrap import wrap

def calc_path_length(heights, start, end):
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    distance = np.full_like(heights, -1)
    distance[start] = 0

    for step in range(heights.size):
        at_step = np.where(distance == step)
        for i in range(len(at_step[0])):
            c = (at_step[0][i], at_step[1][i])
            for d in directions:
                c2 = (c[0] + d[0], c[1] + d[1])
                if c2[0] >= 0 and c2[0] < heights.shape[0] and c2[1] >=0 and c2[1] < heights.shape[1]:
                    if distance[c2] == -1:
                        if (heights[c2] - heights[c] <= 1):
                            if c2 == end:
                                return step + 1
                            distance[c2] = step + 1


heights = np.array([
    [ ord(c) for c in line.rstrip() ]
    for line in fileinput.input()
])

start = np.where(heights == ord('S'))
end = np.where(heights == ord('E'))

heights[start] = ord('a')
heights[end] = ord('z')
heights -= ord('a')

star23 = calc_path_length(heights, start, end)
print(f"star 23: {star23}")

star24 = calc_path_length(heights, np.where(heights == 0), end)
print(f"star 24: {star24}")
