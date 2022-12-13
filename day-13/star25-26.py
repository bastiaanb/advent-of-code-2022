#!/usr/bin/env python

import fileinput
import functools

# If both values are integers, the lower integer should come first.
# If the left integer is lower than the right integer, the inputs are in the right order.
# If the left integer is higher than the right integer, the inputs are not in the right order.
# Otherwise, the inputs are the same integer; continue checking the next part of the input.
# If both values are lists, compare the first value of each list, then the second value, and so on.
# If the left list runs out of items first, the inputs are in the right order.
# If the right list runs out of items first, the inputs are not in the right order.
# If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
# If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison.
# For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by instead comparing [0,0,0] and [2].

def compare(left, right):
    if isinstance(left, int):
        if isinstance(right, int):
            return (left > right) - (left < right)
        else:
            return compare([left], right)
    else:
        if isinstance(right, int):
            return compare(left, [right])
        else:
            if left == []:
                return 0 if right == [] else -1

            if right == []:
                return 1

            result = compare(left[0], right[0])
            return compare(left[1:], right[1:]) if result == 0 else result

inputs = [ line.rstrip() for line in fileinput.input() ]
pairs = [ (eval(inputs[i]), eval(inputs[i+1])) for i in range(0, len(inputs), 3) ]
star25 = sum([ i + 1 for i, p in enumerate(pairs) if compare(p[0], p[1]) < 1 ])
print(f"star 25: {star25}")

packets = [ eval(i) for i in inputs if i ] + [[[2]], [[6]]]
s = sorted(packets, key=functools.cmp_to_key(compare))
star26 = (s.index([[2]]) + 1) * (s.index([[6]]) + 1)
print(f"star 26: {star26}")
