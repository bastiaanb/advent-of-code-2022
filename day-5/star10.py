#!/usr/bin/env python

import fileinput

inputs = [ line.rstrip() for line in fileinput.input() ]

split_index = inputs.index('')

stack_names = inputs[split_index-1].split()
stacks = { name:[] for name in stack_names }
for input in inputs[split_index-2::-1]:
    for i, name in enumerate(stack_names):
        j = 1 + 4 * i
        if j < len(input):
            crate = input[j]
            if crate != ' ':
                stacks[name].append(crate)

for move in inputs[split_index+1:]:
    (dummy1, c, dummy2, from_, dummy3, to) = move.split()
    count=int(c)
    stacks[to].extend(stacks[from_][-count:])
    del stacks[from_][-count:]

result = ''.join([stacks[n][-1] for n in stack_names])

print(f"star 10: {result}")
