#!/usr/bin/env python

import fileinput
import numpy as np
import re
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations

def parse_input(inputs):
    g = nx.Graph()

    for input in inputs:
        m = re.match("Valve ([A-Z]+) has flow rate=([0-9]+); tunnels? leads? to valves? ([A-Z, ]+)", input)
        id = m.group(1)
        g.add_node(id, rate=int(m.group(2)))
        g.add_weighted_edges_from([(id, t, 1) for t in m.group(3).split(', ')])

    return g

def remove_broken_valves(g):
    broken_valves = [ v for v, d in g.nodes(data=True) if d['rate'] == 0 and v != 'AA']
    for v in broken_valves:
        for (from_, to_) in combinations(g[v], 2):
            w = g.edges[v, from_]['weight'] + g.edges[v, to_]['weight']
            if not to_ in g[from_] or g.edges[from_, to_]['weight'] > w:
                g.add_edge(from_, to_, weight=w)
        g.remove_node(v)

def max_flow_rate(g, position, to_visit, time_left):
    global distances
    best = (0, []);
    for i, v in enumerate(to_visit):
        d = distances[position][v] + 1
        if time_left > d:
            nv2 = to_visit[0:i] + to_visit[i+1:]
            rate = max_flow_rate(g, v, nv2, time_left - d)
            if rate[0] > best[0]:
                best = rate

    return (g.nodes.data()[position]['rate'] * time_left + best[0], [position] + best[1])

inputs = [ line.rstrip() for line in fileinput.input() ]
g = parse_input(inputs)
remove_broken_valves(g)

distances = dict(nx.shortest_path_length(g, weight="weight"))

to_visit = list(g.nodes)
to_visit.remove('AA')
(r, v) = max_flow_rate(g, 'AA', to_visit, 30)

print(f"{r} / {v}")
