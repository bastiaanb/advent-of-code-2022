#!/usr/bin/env python

import fileinput

# A = X = 1 = Rock
# B = Y = 2 = Paper
# C = Z = 3 = Scissors

star3_scores = {
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


# A = 1 = Rock
# B = 2 = Paper
# C = 3 = Scissors

# X = lose
# Y = draw
# Z = win

star4_scores = {
    "A X": 3 + 0,
    "A Y": 1 + 3,
    "A Z": 2 + 6,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 2 + 0,
    "C Y": 3 + 3,
    "C Z": 1 + 6,
}

inputs = [ line.strip() for line in fileinput.input() ]

star3_score = sum([
    star3_scores[input] for input in inputs
])

print(f"star 3: {star3_score}")

star4_score = sum([
    star4_scores[input] for input in inputs
])

print(f"star 4: {star4_score}")
