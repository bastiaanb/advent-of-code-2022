#!/usr/bin/env python

import fileinput

inputs = [ line.strip() for line in fileinput.input() ]

def to_prority(c):
    i = ord(c)
    if i >= 97:
        return i - 96
    else:
        return i - 64 + 26

prios=[]

for input in inputs:
    half = int(len(input)/2)
    in_both = list(set(input[:half]) & set(input[half:]))
    prios.append(to_prority(in_both[0]))

print(f"star 5: {sum(prios)}")

prios=[]

for i in range(0, len(inputs), 3):
    in_all = list(set(inputs[i]) & set(inputs[i+1]) & set(inputs[i+2]))
    prios.append(to_prority(in_all[0]))

print(f"star 6: {sum(prios)}")
