#!/usr/bin/env python

import fileinput
import numpy as np
import re

def manhattan(ax, ay, bx, by):
    return abs(bx - ax) + abs(by - ay)

def sensors_to_ranges(sensors, y, minx, maxx):
    ranges = []

    for s in sensors:
#        d = manhattan(s[0], s[1], s[2], s[3])
        hw = s[2] - abs(y - s[1])
        if hw >= 0:
            # range is excluding end
            start = s[0] - hw
            end = s[0] + hw + 1
            if end > minx and start < maxx:
                ranges.append((max(minx, start), min(maxx, end)))

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

def calc_ranges_for_y(sensors, y, minx, maxx):
    ranges = sensors_to_ranges(sensors, y, minx, maxx)
    return merge_ranges(ranges)

inputs = [ line.rstrip() for line in fileinput.input() ]

sensors = []

for input in inputs:
    m = re.match("Sensor at x=(-?[0-9]+), y=(-?[0-9]+): closest beacon is at x=(-?[0-9]+), y=(-?[0-9]+)", input)
    s = [int(m.group(i)) for i in range(1, 5)]
    d = abs(s[2] - s[0]) + abs(s[3] - s[1])
    sensors.append((s[0], s[1], d))

(minx, miny) = 0, 0
(maxx, maxy) = (4000001,4000001)

for y in range(maxy - 1, miny - 1, -1):
#for y in range(miny, maxy):
    merged = calc_ranges_for_y(sensors, y, minx, maxx)
    if merged != [(minx, maxx)]:
        print (f"{y}: {merged}")
        x = merged[0][1]
        print(f"star 30: {x*4000000+y}")
        break
