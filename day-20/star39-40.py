#!/usr/bin/env python

import fileinput
from dataclasses import dataclass

@dataclass
class Number:
    v: int
    p: "Number" = None
    n: "Number" = None
    def __str__(self):
        return f"Number(v={self.v},p={self.p.v},n={self.n.v})"

def calc_coordinate(input, key, times):
    numbers = [ Number(i * key) for i in inputs]
    l = len(numbers)

    for i, n in enumerate(numbers):
        n.p = numbers[(i-1) % l]
        n.n = numbers[(i+1) % l]

    for t in range(times):
        for number in numbers:
            j = number.v % (l - 1)
            if j != 0:
                number.p.n = number.n
                number.n.p = number.p
                c = number
                for r in range(j):
                    c = c.n
                number.n = c.n
                number.n.p = number
                number.p = c
                number.p.n = number

    s = [ n for n in numbers if n.v == 0 ][0]
    coordinate = 0
    for i in range(3001):
        if i in [1000, 2000, 3000]:
            coordinate += s.v
        s = s.n

    return coordinate

inputs = [ int(line.rstrip()) for line in fileinput.input() ]

star39 = calc_coordinate(inputs, 1, 1)
print(f"star 39: {star39}")

star40 = calc_coordinate(inputs, 811589153, 10)
print(f"star 40: {star40}")
