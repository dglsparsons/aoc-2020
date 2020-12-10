
with open('input.txt', 'r') as f:
    content = [int(l) for l in f.readlines()]
    joltages = sorted(content + [0, max(content) + 3])


def part_one():
    differences = [b - a for a, b in zip(joltages, joltages[1:])]
    return differences.count(1) * differences.count(3)


def calculate_combinations(n):
    # Think this dude is a tribonacci sequence, offset by 3...
    def tribonacci(n):
        if n == 0 or n == 1:
            return 0
        if n == 2:
            return 1

        return tribonacci(n - 3) + tribonacci(n - 2) + tribonacci(n - 1)

    return tribonacci(n + 3)


def part_two():
    off_by_ones = [b - a == 1 for a, b in zip(joltages, joltages[1:])]

    sequential_ones = 0
    combinations = 1
    for v in off_by_ones:
        if not v:
            combinations *= calculate_combinations(sequential_ones - 1)
            sequential_ones = 0
            continue

        sequential_ones += 1

    return combinations


print("part 1:", part_one())
print("part 2:", part_two())
