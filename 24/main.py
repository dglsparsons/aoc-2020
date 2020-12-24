def split(line):
    if not line:
        return []

    if line[0] in ['s', 'n']:
        return [line[:2]] + split(line[2:])

    return [line[:1]] + split(line[1:])


with open('input.txt', 'r') as f:
    start_instructions = [split(line.strip()) for line in f.readlines()]


def part_one(instructions):
    black = set()
    for ins in instructions:
        position = [0, 0]
        for step in ins:
            if step == 'e':
                position[0] += 1
            if step == 'se':
                position[0] += 1
                position[1] -= 1
            if step == 'sw':
                position[1] -= 1
            if step == 'w':
                position[0] -= 1
            if step == 'nw':
                position[0] -= 1
                position[1] += 1
            if step == 'ne':
                position[1] += 1
        tuple_pos = (position[0], position[1])
        if tuple_pos in black:
            black.remove(tuple_pos)
        else:
            black.add(tuple_pos)

    return black


def count_black_neighbours(x, y, black):
    count = 0
    for n in [
        (x+1, y),
        (x-1, y),
        (x, y+1),
        (x, y-1),
        (x-1, y+1),
        (x+1, y-1)
    ]:
        if n in black:
            count += 1

    return count


def part_two(start_instructions):
    initial = part_one(start_instructions)
    for day in range(100):
        copy = {t for t in initial}
        min_ew = min(t[0] for t in initial) - 1
        max_ew = max(t[0] for t in initial) + 1
        min_ns = min(t[1] for t in initial) - 1
        max_ns = max(t[1] for t in initial) + 1

        for x in range(min_ew, max_ew + 1):
            for y in range(min_ns, max_ns + 1):
                count = count_black_neighbours(x, y, initial)
                if (x, y) in initial and (count == 0 or count > 2):
                    copy.remove((x, y))
                if (x, y) not in initial and count == 2:
                    copy.add((x, y))

        initial = copy

    return len(initial)


print("part one:", len(part_one(start_instructions)))
print("part two:", part_two(start_instructions))
