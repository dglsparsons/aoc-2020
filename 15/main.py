with open('input.txt', 'r') as f:
    content = f.read()
    starting_numbers = [int(n) for n in content.split(',')]


def solution(starting_numbers, n):
    last_occurences = {}
    last_number_spoken = 0
    for turn in range(n):
        if turn < len(starting_numbers):
            last_number_spoken = starting_numbers[turn]
            last_occurences[last_number_spoken] = [turn]
            continue

        # look at the last number spoken
        last_turn = last_occurences.get(last_number_spoken)
        last_number_spoken = last_turn[-1] - last_turn[-2] if len(last_turn) > 1 else 0

        last_occurences[last_number_spoken] = last_occurences.get(
            last_number_spoken, [])[-1:] + [turn]

        if (turn % 1_000_000 == 0):
            print("turn", turn)

    return last_number_spoken


print("part one:", solution(starting_numbers, 2020))
print("part two:", solution(starting_numbers, 30_000_000))
