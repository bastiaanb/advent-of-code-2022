#!/usr/bin/env python

import fileinput
import numpy as np
import re

def manhattan(ax, ay, bx, by):
    return abs(bx - ax) + abs(by - ay)

def sensors_to_ranges(sensors, y):
    ranges = []

    for s in sensors:
        d = manhattan(s[0], s[1], s[2], s[3])
        hw = d - abs(y - s[1])
        if hw >= 0:
            # range is excluding end
            ranges.append((s[0] - hw, s[0] + hw + 1))

    ranges.sort(key=lambda x: x[0])

    return ranges

def merge_ranges(ranges):
    merged = []
    (start, end) = ranges[0]

    for r in ranges[1:]:
        if r[0] <= end:
            end = max(r[1], end)
        else:
            merged.append((start, end))
            (start, end) = r

    merged.append((start, end))

    return merged

def calc_ranges_for_y(sensors, y):
    ranges = sensors_to_ranges(sensors, y)
    print(ranges)
    return merge_ranges(ranges)

inputs = [ line.rstrip() for line in fileinput.input() ]

sensors = []

for input in inputs:
    m = re.match("Sensor at x=(-?[0-9]+), y=(-?[0-9]+): closest beacon is at x=(-?[0-9]+), y=(-?[0-9]+)", input)
    sensors.append([int(m.group(i)) for i in range(1, 5)])

y=10
y=2000000
y=14
merged = calc_ranges_for_y(sensors, y)

positions = sum([r[1] - r[0] for r in merged])
beacons_in_row = len({s[2] for s in sensors if s[3] == y})
star29 = positions - beacons_in_row

print (f"star 29: {star29}")
