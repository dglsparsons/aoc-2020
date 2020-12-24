LABELING = '318946572'
start_order = [int(c) for c in LABELING]


def take_turn(cups, current):
    # Pick up
    picked_up = []
    pickup = cups[current]  # next cup
    for _ in range(3):
        picked_up += [pickup]
        pickup = cups[pickup]
    cups[current] = pickup

    # Find the destination
    destination = current
    while destination == current or destination in picked_up:
        destination -= 1
        if destination == 0:
            destination += len(cups) - 1

    # Reinsert the picked up ones
    cups[picked_up[-1]] = cups[destination]
    cups[destination] = picked_up[0]

    return cups[current]


def play_game(cups, current, rounds):
    for n in range(1, rounds+1):
        if n % 1_000_000 == 0:
            print("Turn:", n)
        current = take_turn(cups, current)

    return cups


def flesh_out_cups(start_order, amount):
    cups = [0] + list(range(2, amount + 2))
    cups[-1] = start_order[0]
    for ix, (s, s1) in enumerate(zip(start_order, start_order[1:])):
        cups[s] = s1
        if ix + 1 == len(start_order[1:]) and amount > ix + 2:
            cups[s1] = len(start_order) + 1
        if ix + 2 == amount:
            cups[s1] = start_order[0]
    return cups


def part_one(start_order):
    cups = flesh_out_cups(start_order, 9)
    # now we have a circle of cups, where the cup's number is the index, and the
    # value is the next index in the circle
    start = start_order[0]
    cups = play_game(cups, start, rounds=100)

    current = cups[1]
    result = ''
    for _ in range(8):
        result += str(current)
        current = cups[current]

    return result


def part_two(start_order):
    cups = flesh_out_cups(start_order, 1_000_000)
    start = start_order[0]
    cups = play_game(cups, start, rounds=10_000_000)

    current = cups[1]
    result = 1
    for _ in range(2):
        result *= current
        current = cups[current]

    return result


print("part one (52864379)", part_one(start_order))
print("part two", part_two(start_order))
