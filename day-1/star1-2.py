#!/usr/bin/env python

import fileinput

elves=[]
contents=[]

inputs = [ line.strip() for line in fileinput.input() ]

for input in inputs:
    if input:
        contents.append(int(input))
    else:
        elves.append(contents)
        contents=[]

if contents:
    elves.append(contents)

calories = [ sum(e) for e in elves ]
max_calories = max(calories)
print(f"star 1: {max_calories}")

sorted_calories = sorted(calories, reverse=True)
top3_calories = sum(sorted_calories[0:3])
print(f"star 2: {top3_calories}")
