
with open('input.txt', 'r') as f:
    content = [[c for c in l.strip()] for l in f.readlines()]


def count_neighbours(x, y, grid):
    count = 0
    if x - 1 >= 0 and grid[y][x-1] == '#':
        count += 1
    if x + 1 < len(grid[y]) and grid[y][x+1] == '#':
        count += 1
    if y + 1 < len(grid) and grid[y+1][x] == '#':
        count += 1
    if y - 1 >= 0 and grid[y-1][x] == '#':
        count += 1
    if y - 1 >= 0 and x-1 >= 0 and grid[y-1][x-1] == '#':
        count += 1
    if y + 1 < len(grid) and x - 1 >= 0 and grid[y+1][x-1] == '#':
        count += 1
    if y - 1 >= 0 and x + 1 < len(grid[y-1]) and grid[y-1][x+1] == '#':
        count += 1
    if y + 1 < len(grid) and x + 1 < len(grid[y+1]) and grid[y+1][x+1] == '#':
        count += 1

    return count


def part_one(stuff):
    initial = [[c for c in l] for l in stuff]
    while True:
        copy = [[c for c in l] for l in initial]
        for y, row in enumerate(initial):
            for x, cell in enumerate(row):
                neighbour_count = count_neighbours(x, y, initial)
                if cell == 'L' and neighbour_count == 0:
                    copy[y][x] = '#'
                if cell == '#' and neighbour_count >= 4:
                    copy[y][x] = 'L'

        if copy == initial:
            break

        initial = copy

    occupied = [1 for c in initial for r in c if r == '#']
    return sum(occupied)


def count_visible_occupied_seats(x, y, grid):
    def find_next_seat(start_x, start_y, gradient):
        next_x = gradient[0](start_x)
        next_y = gradient[1](start_y)
        while 0 <= next_x < len(grid[y]) and 0 <= next_y < len(grid):
            cell = grid[next_y][next_x]
            if cell == 'L':
                return 0
            if cell == '#':
                return 1
            next_x = gradient[0](next_x)
            next_y = gradient[1](next_y)

        return 0

    gradients = [
        (lambda x: x, lambda y: y+1),
        (lambda x: x, lambda y: y-1),
        (lambda x: x+1, lambda y: y),
        (lambda x: x-1, lambda y: y),
        (lambda x: x+1, lambda y: y+1),
        (lambda x: x-1, lambda y: y-1),
        (lambda x: x+1, lambda y: y-1),
        (lambda x: x-1, lambda y: y+1)
    ]

    return sum(find_next_seat(x, y, g) for g in gradients)


def part_two(stuff):
    initial = [[c for c in l] for l in stuff]
    while True:
        copy = [[c for c in l] for l in initial]
        for y, row in enumerate(initial):
            for x, cell in enumerate(row):
                if cell == '.':
                    continue

                occupied_count = count_visible_occupied_seats(x, y, initial)
                if cell == 'L' and occupied_count == 0:
                    copy[y][x] = '#'
                if cell == '#' and occupied_count >= 5:
                    copy[y][x] = 'L'

        if copy == initial:
            break

        initial = copy

    occupied = [1 for c in initial for r in c if r == '#']
    return sum(occupied)


print("part one:", part_one(content))
print("part two:", part_two(content))
