#!/usr/bin/env python

import fileinput
import itertools

inputs = [ line.rstrip() for line in fileinput.input() ]

def parse_inputs(inputs):
    root_dir = {
        'name': '/',
        'children': {}
    }

    current_dir = root_dir

    for input in inputs:
        parts = input.split()
        if parts[0] == '$':
            if parts[1] == 'ls':
                pass
            elif parts[1] == 'cd':
                name = parts[2]
                if name == '/':
                    current_dir = root_dir
                elif name == '..':
                    if 'parent' in current_dir:
                        current_dir = current_dir['parent']
                    else:
                        print(f"cd .. from dir {current_dir} without parent")
                        break
                else:
                    if name in current_dir['children']:
                        current_dir = current_dir['children'][name]
                    else:
                        print(f"cd from {current_dir} into not yet listed path '{name}'")
                        break
            else:
                print(f"unknown command {command}")
        else:
            name = parts[1]
            if name in current_dir['children']:
                print(f"listing already known file '{input}' while in dir '{current_dir}'")
                break
            if parts[0].startswith('dir'):
                current_dir['children'][name] = {
                    'name': name,
                    'parent': current_dir,
                    'children': {}
                }
            else:
                current_dir['children'][name] = {
                    'name': name,
                    'parent': current_dir,
                    'size': int(parts[0])
                }

    return root_dir

def get_size(node):
    if not 'size' in node:
         node['size'] = sum([ get_size(child) for child in node['children'].values() ])

    return node['size']

def get_all_dirs(node):
    if 'children' in node:
        return list(itertools.chain(*[ get_all_dirs(child) for child in node['children'].values() ])) + [ node ]
    else:
        return []

root_dir = parse_inputs(inputs)

total_size = 70000000
needed_size = 30000000

used_size = get_size(root_dir)
unused_size = total_size - used_size
to_free_size = needed_size - unused_size

all_dirs = get_all_dirs(root_dir)
star13 = sum([ dir['size'] for dir in all_dirs if dir['size'] <= 100000 ])
star14 = min([ dir['size'] for dir in all_dirs if dir['size'] >= to_free_size ])

print(f"star 13: {star13}")
print(f"star 14: {star14}")
