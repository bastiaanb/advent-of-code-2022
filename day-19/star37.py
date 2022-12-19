#!/usr/bin/env python

import fileinput
import numpy as np
import re
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations
from math import ceil

def parse_input(inputs):
    blueprints={}
    for input in inputs:
        m = re.match("Blueprint ([0-9]+): Each ore robot costs ([0-9]+) ore. Each clay robot costs ([0-9]+) ore. Each obsidian robot costs ([0-9]+) ore and ([0-9]+) clay. Each geode robot costs ([0-9]+) ore and ([0-9]+) obsidian.", input)
        blueprints[m.group(1)] = np.array([
            [ m.group(2),          0,          0, 0 ], # ore
            [ m.group(3),          0,          0, 0 ], # clay
            [ m.group(4), m.group(5),          0, 0 ], # obsidian
            [ m.group(6),          0, m.group(7), 0 ], # geode
        ], dtype=int)
    return blueprints

count = 0
def most_geodes(robots, inventory, time_left):
    global items, count
    count +=1
    if time_left > 1:
        # ore_robot
        options = []
        wait = 1 + max(ceil((cost[0][0] - inventory[0]) / robots[0]), 0)
        if wait < time_left:
            options.append(most_geodes(robots + items[0], inventory + robots * wait - cost[0], time_left - wait))

        # clay_robot
        wait = 1 + max(ceil((cost[1][0] - inventory[0]) / robots[0]), 0)
        if wait < time_left:
            options.append(most_geodes(robots + items[1], inventory + robots * wait - cost[1], time_left - wait))

        # obsidian_robot
        if (robots[1] > 0):
            wait = 1 + max(ceil((cost[2][0] - inventory[0]) / robots[0]), ceil((cost[2][1] - inventory[1]) / robots[1]), 0)
            if wait < time_left:
                options.append(most_geodes(robots + items[2], inventory + robots * wait - cost[2], time_left - wait))

        # geode_robot
        if (robots[2] > 0):
            wait = 1 + max(ceil((cost[3][0] - inventory[0]) / robots[0]), ceil((cost[3][2] - inventory[2]) / robots[2]), 0)
            if wait < time_left:
                options.append(most_geodes(robots + items[3], inventory + robots * wait - cost[3], time_left - wait))

        if options != []:
            return max(options)

    inventory += robots * int(time_left)
    return inventory[3]

inputs = [ line.rstrip() for line in fileinput.input() ]
blueprints = parse_input(inputs)

#print(blueprints)

cost = blueprints['2']
robots = np.array([1, 0, 0, 0], dtype=int)
inventory = np.array([0, 0, 0, 0], dtype=int)

items=np.eye(4, dtype=int)
names= ['ore', 'clay', 'obisidian', 'geode', 'nothing' ]

m = most_geodes(robots, inventory, 24)
print(f"geodes={m}")
# for v in m[1]:
#     print(v)
print(count)
