with open('input.txt', 'r') as f:
    _content = [c.strip() for c in f.readlines()]
    # make coords as set of (x, y, z) tuples
    _coords = {(x, y, 0, 0) for y, line in enumerate(_content)
               for x, thing in enumerate(line) if thing == '#'}


def count_neighbours(x, y, z, w, coords):
    count = 0
    for _x in range(x-1, x+2):
        for _y in range(y-1, y+2):
            for _z in range(z - 1, z+2):
                for _w in range(w - 1, w+2):
                    if (_x, _y, _z, _w) in coords:
                        count += 1
    return count


def part_one(coords):
    for i in range(0, 6):
        start_x = min(c[0] for c in coords) - 1
        start_y = min(c[1] for c in coords) - 1
        start_z = min(c[2] for c in coords) - 1
        end_x = max(c[0] for c in coords) + 1
        end_y = max(c[1] for c in coords) + 1
        end_z = max(c[2] for c in coords) + 1

        next_iteration = {c for c in coords}
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                for z in range(start_z, end_z + 1):
                    count = count_neighbours(x, y, z, 0, coords)
                    if (x, y, z, 0) in coords:
                        # 2 or 3 neighbours means stay active, else go inactive
                        # but count also includes the cell itself
                        if count == 3 or count == 4:
                            continue
                        next_iteration.remove((x, y, z, 0))
                        continue
                    # 3 neighbours means go active, else stay inactive
                    if count != 3:
                        continue
                    next_iteration.add((x, y, z, 0))

        coords = next_iteration

    # finally, count them
    return len(list(coords))


def part_two(coords):
    for i in range(0, 6):
        start_x = min(c[0] for c in coords) - 1
        start_y = min(c[1] for c in coords) - 1
        start_z = min(c[2] for c in coords) - 1
        start_w = min(c[3] for c in coords) - 1
        end_x = max(c[0] for c in coords) + 1
        end_y = max(c[1] for c in coords) + 1
        end_z = max(c[2] for c in coords) + 1
        end_w = max(c[3] for c in coords) + 1

        next_iteration = {c for c in coords}
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                for z in range(start_z, end_z + 1):
                    for w in range(start_w, end_w + 1):
                        count = count_neighbours(x, y, z, w, coords)
                        if (x, y, z, w) in coords:
                            # 2 or 3 neighbours means stay active, else go inactive
                            # but count also includes the cell itself
                            if count == 3 or count == 4:
                                continue
                            next_iteration.remove((x, y, z, w))
                            continue
                        # 3 neighbours means go active, else stay inactive
                        if count != 3:
                            continue
                        next_iteration.add((x, y, z, w))

        coords = next_iteration

    # finally, count them
    return len(list(coords))


print("part_one:", part_one(_coords))
print("part_two:", part_two(_coords))
