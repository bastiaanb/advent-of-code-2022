#!/usr/bin/env python

import fileinput
import numpy as np

inputs = [ line.rstrip() for line in fileinput.input() ]

def count_visited_by_tail(inputs, l):
    knots = np.zeros([l, 2], int)
    visited = {}

    for input in inputs:
        (direction, steps) = input.split(' ')

        for step in range(int(steps)):
            knots[0] += { 'R': [0, 1], 'L': [0, -1], 'U': [1, 0], 'D': [-1, 0]}[direction]

            for i in range(1, l):
                dist = knots[i - 1] - knots[i]
                if max(abs(dist)) > 1:
                    knots[i] += np.sign(dist)

            visited[str(knots[l - 1])] = True

    return len(visited)

print(f"star 17: {count_visited_by_tail(inputs, 2)}")
print(f"star 18: {count_visited_by_tail(inputs, 10)}")
