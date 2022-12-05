#!/usr/bin/env python

import fileinput

inputs = [ line.strip() for line in fileinput.input() ]

def to_range(s):
    r = s.split('-', 1)
    return (int(r[0]), int(r[1]))

def parse_input(s):
    elves = s.split(",", 1)
    return to_range(elves[0]), to_range(elves[1])

def is_part_of(range1, range2):
    return range1[0] >= range2[0] and range1[1] <= range2[1]

def overlaps_with(range1, range2):
    return (range1[0] <= range2[0] and range1[1] >= range2[0]) or (range2[0] <= range1[0] and range2[1] >= range1[0])


ranges = [ parse_input(input) for input in inputs]
contains=sum([ 1 for r in ranges if is_part_of(r[0], r[1]) or is_part_of(r[1], r[0]) ])
overlaps=sum([ 1 for r in ranges if overlaps_with(r[0], r[1]) ])

print(f"star 7: {contains}")
print(f"star 8: {overlaps}")
