#!/usr/bin/env python

import fileinput
import numpy as np

inputs = [ line.rstrip() for line in fileinput.input() ]

def calculate_x(inputs):
    x = 1
    for input in inputs:
        parts = input.split()
        if parts[0] == 'noop':
            yield x
        elif parts[0] == 'addx':
            yield x
            yield x
            x += int(parts[1])
        else:
            print(f"unknown opcode {input}")
            break

x_values = list(calculate_x(inputs))

strengths = [ (i + 1) * x for (i, x) in enumerate(x_values) if i % 40 == 19 ]
print(f"star 19: {sum(strengths[0:6])}")

pixels = [
    '#' if abs((i % 40) - x) < 2 else '.'
    for (i, x) in enumerate(x_values)
]

print("star 20:")
p = ''.join(pixels)
for y in range(6):
    print(p[y*40:(y+1)*40])

# dict panels contains all painted panels...
from PIL import Image
img = Image.new('RGB', (40, 6), 'black')
p2 = img.load()

for (i, x) in enumerate(x_values):
    (xc, yc) = (i % 40, int(i / 40))
    if abs(xc - x) < 2:
        p2[xc, yc] = (255, 255, 255)

img.save("star20.png")
