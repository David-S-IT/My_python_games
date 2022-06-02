from settings import *

text_map = [
    '1111111111111111',
    '1..1..1........1',
    '1..1..1........1',
    '1..1..1........1',
    '1.....1...12...1',
    '1111..1...11...1',
    '1.....1........1',
    '1.....1........1',
    '1111111111111111',
]
world_map = {}
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            mini_map.add((i * map_tile, j * map_tile))
            if char == '1':
                world_map[(i * tile, j * tile)] = '1'
            elif char == '2':
                world_map[(i * tile, j * tile)] = '2'
