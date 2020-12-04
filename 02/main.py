from parse import parse


def count_letter(raw_input, letter):
    count = 0
    for c in raw_input:
        if c == letter:
            count += 1
    return count


def is_valid(raw_input, letter, first_pos, second_pos):
    x = raw_input[first_pos - 1]
    y = raw_input[second_pos - 1]

    return (x == letter or y == letter) and x != y


with open('input.txt', 'r+') as f:
    valid_count = 0

    for line in f:
        first_pos, second_pos, letter, raw_input = parse('{}-{} {}: {}', line)
        valid = is_valid(raw_input, letter, int(first_pos), int(second_pos))
        if valid:
            valid_count += 1

    print("valid count:", valid_count)
