with open('input.txt', 'r') as f:
    content = [(d[0], int(d[1:])) for d in f.read().splitlines()]


DIRECTIONS = {
    0: 'E',
    90: 'S',
    180: 'W',
    270: 'N'
}


def get_new_facing(starting, command, amount):
    if command == 'R':
        return (starting + amount) % 360
    return (starting - amount) % 360


def part_one(directions):
    position = (0, 0)
    facing = 0
    for (direction, amount) in directions:
        if direction in ['R', 'L']:
            facing = get_new_facing(facing, direction, amount)
            continue

        if direction == 'F':
            direction = DIRECTIONS[facing]

        if direction == 'N':
            position = position[0], position[1] + amount
        if direction == 'E':
            position = position[0] + amount, position[1]
        if direction == 'S':
            position = position[0], position[1] - amount
        if direction == 'W':
            position = position[0] - amount, position[1]

    return abs(position[0]) + abs(position[1])


def rotate_waypoint(pos, direction, angle):
    if direction == 'L':
        # Let's just always rotate rightyways
        angle = 360 - angle

    if angle == 90:
        return (pos[1], -pos[0])
    if angle == 180:
        return (-pos[0], -pos[1])
    if angle == 270:
        return (-pos[1], pos[0])

    raise ValueError("Bad angle", angle)


def part_two(directions):
    # Coords are (x, y)
    ship_position = (0, 0)
    waypoint_position = (10, 1)

    for (direction, amount) in directions:
        if direction in ['R', 'L']:
            waypoint_position = rotate_waypoint(waypoint_position, direction, amount)
            continue

        if direction == 'F':
            ship_position = (ship_position[0] + waypoint_position[0] * amount,
                             ship_position[1] + waypoint_position[1] * amount)

        if direction == 'N':
            waypoint_position = waypoint_position[0], waypoint_position[1] + amount
        if direction == 'E':
            waypoint_position = waypoint_position[0] + amount, waypoint_position[1]
        if direction == 'S':
            waypoint_position = waypoint_position[0], waypoint_position[1] - amount
        if direction == 'W':
            waypoint_position = waypoint_position[0] - amount, waypoint_position[1]

    return abs(ship_position[0]) + abs(ship_position[1])


print("part one:", part_one(content))
print("part two:", part_two(content))
