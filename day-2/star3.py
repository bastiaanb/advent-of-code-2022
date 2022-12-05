#!/usr/bin/env python

import fileinput

# A = X = 1 = Rock
# B = Y = 2 = Paper
# C = Z = 3 = Scissors

scores = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3 + 0,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3,
}

score = 0
for line in fileinput.input():
    line = line.strip()
    score += scores[line]

print(score)
