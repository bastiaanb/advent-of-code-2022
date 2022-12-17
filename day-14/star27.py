#!/usr/bin/env python

import fileinput
import numpy as np


def print_cave(cave):
    print("\n".join([ "".join(r) for r in cave.tolist() ] ))

paths = [ [ [ int(v) for v in c.split(",") ] for c in line.rstrip().split(" -> ") ] for line in fileinput.input() ]

print(paths)
xs = [ c[0] for path in paths for c in path ]
ys = [ c[1] for path in paths for c in path ]

minx=min(xs)
maxx=max(xs)
maxy=max(ys)
miny= 0
xsize=1 + maxx - minx
ysize=1 + maxy - miny

cave = np.full((ysize, xsize), '.')

for path in paths:
    for i in range(1, len(path)):
        (x1, y1) = path[i - 1]
        (x2, y2) = path[i]
        (dx, dy) = (x2 - x1, y2 - y1)
        match np.sign(dx), np.sign(dy):
            case 0, -1:
                cave[y2-miny:y1+1-miny,x1-minx] = '#'
            case 0, 1:
                cave[y1-miny:y2+1-miny,x1-minx] = '#'
            case -1, 0:
                cave[y1-miny,x2-minx:x1+1-minx] = '#'
            case 1, 0:
                cave[y1-miny,x1-minx:x2+1-minx] = '#'

def simulate():
    for piece in range(10000):
        (sy, sx) = (0, 500 - minx)

        cave[sy, sx] = 'O'

        print(f"piece {piece}")
        print_cave(cave)
        for step in range(ysize):
#            print(f"piece {piece}, {step}")
#            print_cave(cave)
            for (ny, nx) in [ (sy + 1, sx), (sy + 1, sx - 1), (sy + 1, sx + 1) ]:
                if ny >= ysize or nx < 0 or nx >=xsize:
                    # free fall => done
                    return piece
                if cave[ny, nx] == '.':
                    # free spot => move
                    cave[sy, sx] = '.'
                    cave[ny, nx] = 'O'
                    (sy, sx) = (ny, nx)
                    break
            else:
                # no free spots => done with this piece
                break

pieces = simulate()
print(f"star 27: {pieces}")
