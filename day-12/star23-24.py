#!/usr/bin/env python

import fileinput
import numpy as np
from textwrap import wrap

def calc_path_length(heights, end, start_pos=None, start_height=None):
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    distance = np.full_like(heights, -1)
    if start_pos is None:
        at_0 = np.where(heights == start_height)
        for i in range(len(at_0[0])):
            distance[at_0[0], at_0[1]] = 0
    else:
        distance[start_pos] = 0

    for step in range(heights.size):
#        print(distance)
        at_step = np.where(distance == step)
#        print(f"at_step {at_step}")
        for i in range(len(at_step[0])):
            c = (at_step[0][i], at_step[1][i])
            for d in directions:
                c2 = (c[0] + d[0], c[1] + d[1])
                if c2[0] >= 0 and c2[0] < heights.shape[0] and c2[1] >=0 and c2[1] < heights.shape[1]:
    #                print(f"{c2}: {distance[c2]}")
                    if distance[c2] == -1:
                        if (heights[c2] - heights[c] <= 1):
                            if c2 == end:
#                                print(f"reached [c2] in {step + 1} steps")
                                return step + 1
                            distance[c2] = step + 1


heights = np.array([
    [ ord(c) for c in line.rstrip() ]
    for line in fileinput.input()
])

start = np.where(heights == ord('S'))
start = (start[0][0], start[1][0])
end = np.where(heights == ord('E'))
end = (end[0][0], end[1][0])

heights[start] = ord('a')
heights[end] = ord('z')
heights -= ord('a')

star23 = calc_path_length(heights, end, start_pos=start)
print(f"star 23: {star23}")

star24 = calc_path_length(heights, end, start_height=0)
print(f"star 24: {star24}")
