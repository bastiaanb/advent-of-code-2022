#!/usr/bin/env python

import fileinput

inputs = [ line.strip() for line in fileinput.input() ]

def to_range(s):
    r = s.split('-', 1)
    return (int(r[0]), int(r[1]))

def is_part_of(range1, range2):
    return range1[0] >= range2[0] and range1[1] <= range2[1]

def overlaps_with(range1, range2):
    return (range1[0] <= range2[0] and range1[1] >= range2[0]) or (range2[0] <= range1[0] and range2[1] >= range1[0])

contains=0
overlaps=0

for input in inputs:
    elves = input.split(",", 1)
    range1 = to_range(elves[0])
    range2 = to_range(elves[1])
    if is_part_of(range1, range2) or is_part_of(range2, range1):
        contains+=1

    if overlaps_with(range1, range2):
        overlaps+=1

print(f"star 7: {contains}")
print(f"star 8: {overlaps}")
