
with open('input.txt', 'r') as f:
    content = f.readlines()
    instructions = []
    mask = ""

    for line in content:
        a, b = line.split(' = ')
        if a == "mask":
            mask = b.strip()
            instructions += [("mask", mask)]
        else:
            address = int(a[4:-1])
            value = int(b)
            instructions += [(address, value)]


def apply_mask(mask, value):
    m1 = int(mask.replace('X', '1'), 2)  # Make 0s pull values down
    m2 = int(mask.replace('X', '0'), 2)  # Make 1s pull values up

    return (value & m1) | m2


def part_one(mask, instructions):
    result = {}
    for k, v in instructions:
        if k == "mask":
            mask = v
            continue

        result[k] = apply_mask(mask, v)

    total = 0
    for v in result.values():
        total += v
    return total


def generate_combinations(value):
    if value == '0':
        return ['0']
    if value == '1':
        return ['1']
    if value == 'X':
        return ['1', '0']

    # recursive case
    if value[0] == '0':
        return ['0' + v for v in generate_combinations(value[1:])]
    if value[0] == '1':
        return ['1' + v for v in generate_combinations(value[1:])]
    if value[0] == 'X':
        return ['1' + v for v in generate_combinations(value[1:])] + ['0' + v for v in generate_combinations(value[1:])]


def apply_part_two_mask(mask, value):
    result = ""
    for a, b in zip(mask, '{0:b}'.format(value).zfill(36)):
        if a == '0':
            result += b
        if a == '1':
            result += '1'
        if a == 'X':
            result += 'X'

    return [int(v, 2) for v in generate_combinations(result)]


def part_two():
    result = {}
    for k, v in instructions:
        if k == "mask":
            mask = v
            continue

        for mv in apply_part_two_mask(mask, k):
            result[mv] = v

    total = 0
    for v in result.values():
        total += v
    return total


print("part one:", part_one(mask, instructions))
print("part two:", part_two())
