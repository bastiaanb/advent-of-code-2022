#!/usr/bin/env python

import fileinput
import numpy as np


def print_cave(cave):
    print("\n".join([ "".join(r) for r in cave.tolist() ] ))

def simulate(paths, with_floor):
    xs = [ c[0] for path in paths for c in path ]
    ys = [ c[1] for path in paths for c in path ]

    ysize=1 + max(ys) + 2
    offsetx = ysize + 2
    minx = min(xs + [500 - offsetx])
    maxx = max(xs + [500 + offsetx])
    xsize=1 + maxx - minx
    cave = np.full((ysize, xsize), '.')

    if with_floor:
        cave[ysize -1:] = '#'

    for path in paths:
        for i in range(1, len(path)):
            (x1, y1) = path[i - 1]
            (x2, y2) = path[i]
            (dx, dy) = (x2 - x1, y2 - y1)
            match np.sign(dx), np.sign(dy):
                case 0, -1:
                    cave[y2:y1+1,x1-minx] = '#'
                case 0, 1:
                    cave[y1:y2+1,x1-minx] = '#'
                case -1, 0:
                    cave[y1,x2-minx:x1+1-minx] = '#'
                case 1, 0:
                    cave[y1,x1-minx:x2+1-minx] = '#'

    for piece in range(1000000):
        (sy, sx) = (0, 500 - minx)

        if cave[sy, sx] == 'O':
            # no more room => done
            return piece

        cave[sy, sx] = 'O'

        # print(f"piece {piece}")
        # if piece % 1000 == 0:
        #     print_cave(cave)
        for step in range(ysize):
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

paths = [ [ [ int(v) for v in c.split(",") ] for c in line.rstrip().split(" -> ") ] for line in fileinput.input() ]

print(f"star 27: {simulate(paths, False)}")
print(f"star 28: {simulate(paths, True)}")
