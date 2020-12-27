with open('input.txt', 'r') as f:
    card_key, door_key = [int(k.strip()) for k in f.readlines()]


def calculate_key(loop_size, subject_number):
    value = 1
    for _ in range(loop_size):
        value = (value * subject_number) % 20201227

    return value


def brute_force_loop_size(public_key):
    loop_size = 1
    value = 1
    loop_size = 1
    while True:
        value = (value * 7) % 20201227
        if value == public_key:
            return loop_size
        loop_size += 1


def part_one(card_key, door_key):
    loop_size = brute_force_loop_size(card_key)

    return calculate_key(loop_size, door_key)


print("part one", part_one(card_key, door_key))
