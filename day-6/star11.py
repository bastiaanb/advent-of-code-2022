#!/usr/bin/env python

import fileinput

inputs = [ line.rstrip() for line in fileinput.input() ]

def print_marker_offsets(inputs, marker_length):
    for input in inputs:
        chunks = [ input[i:i+marker_length] for i in range(0, len(input)) ]
        only_unique_chars = [ len(set(chunk)) == len(chunk) for chunk in chunks ]
        print(only_unique_chars.index(True) + marker_length)

print("star 11:")
print_marker_offsets(inputs, 4)

print("star 12:")
print_marker_offsets(inputs, 14)
