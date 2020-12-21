from math import sqrt

sea_monster = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   '
]


def flip(tile):
    return list(reversed(tile))


def rotate(tile):
    out = []
    for i in range(0, len(tile[0])):
        out += ['']

    for y in reversed(tile):
        for i, x in enumerate(y):
            out[i] += x

    return [''.join(c) for c in out]


def get_possible_arrangements(tile):
    r1 = rotate(tile)
    r2 = rotate(r1)
    r3 = rotate(r2)

    # 8 directions for each tile
    return [tile, r1, r2, r3, flip(tile), flip(r1), flip(r2), flip(r3)]


with open('input.txt', 'r') as f:
    raw_tiles = [(int(r.strip().split('\n')[0][5:-1]), r.strip().split('\n')[1:])
                 for r in f.read().split('\n\n')]
    tile_permutations = [(t, get_possible_arrangements(tile)) for (t, tile) in raw_tiles]


def pretty_print(tile):
    for y in tile:
        print(y)

    print()


def get_rhs(tile):
    return [y[-1] for y in tile]


def get_lhs(tile):
    return [y[0] for y in tile]


def matching_arrangement(grid, y, x, arrangements):
    left = None if x == 0 else grid[y][x - 1]
    top = None if y == 0 else grid[y-1][x]

    for a in arrangements:
        top_matches = (not top) or a[0] == top[1][-1]
        left_matches = (not left) or get_rhs(left[1]) == get_lhs(a)

        if top_matches and left_matches:
            return a

    return None


def do_the_thing(tiles):
    grid_size = int(sqrt(len(tiles)))
    grid = [[None for i in range(0, grid_size)] for y in range(0, grid_size)]

    def possible(x, y, tile):
        left = None if x == 0 else grid[y][x - 1]
        top = None if y == 0 else grid[y-1][x]

        top_matches = (not top) or tile[0] == top[1][-1]
        left_matches = (not left) or get_rhs(left[1]) == get_lhs(tile)

        return top_matches and left_matches

    def solve(_tiles):
        for y in range(grid_size):
            for x in range(grid_size):
                if not grid[y][x]:
                    for tile in _tiles:
                        tile_id, arrangements = tile
                        for a in arrangements:
                            if possible(x, y, a):
                                grid[y][x] = (tile_id, a)
                                solve([t for t in _tiles if t[0] != tile_id])
                                grid[y][x] = None
                    return
        raise KeyError("completed")

    try:
        solve(tiles)
    except KeyError:
        pass

    print("part one", grid[0][0][0] * grid[0][grid_size-1][0] * grid[grid_size-1]
          [0][0] * grid[grid_size - 1][grid_size-1][0])

    # part 2
    no_borders_grid = [[None for i in range(0, grid_size)] for y in range(0, grid_size)]
    for y in range(grid_size):
        for x in range(grid_size):
            tile = grid[y][x][1]
            no_borders_tile = [line[1:-1] for line in tile[1:-1]]
            no_borders_grid[y][x] = no_borders_tile

    sea = [[] for i in range(0, 8*grid_size)]
    for y in range(grid_size):
        for x in range(grid_size):
            for _y, line in enumerate(no_borders_grid[y][x]):
                sea[y*8 + _y] += [c for c in line]

    def is_sea_monster(y, x, monster):
        for my, row in enumerate(monster):
            for mx, char in enumerate(row):
                if char != '#':
                    continue

                # need to check every character of the sea monster is a '#'
                # if it is, mark them all
                if sea[y+my][x+mx] not in ['#', '0']:
                    return False
        return True

    for monster in get_possible_arrangements(sea_monster):
        for y in range(0, len(sea) - len(monster)):
            for x in range(0, len(sea[0]) - len(monster[0])):
                if is_sea_monster(y, x, monster):
                    for my, row in enumerate(monster):
                        for mx, char in enumerate(row):
                            if char != '#':
                                continue

                            sea[y+my][x+mx] = '0'

    count = 0
    for line in sea:
        for c in line:
            if c == '#':
                count += 1
    print(count)

    return None


do_the_thing(tile_permutations)
