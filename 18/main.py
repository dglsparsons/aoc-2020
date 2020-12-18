with open('input.txt', 'r') as f:
    content = [li.strip() for li in f.readlines()]


def remove_brackets(s, solver):
    # Start by removing all the brackets
    close_bracket_idx = s.find(')')
    while close_bracket_idx != -1:
        open_bracket_idx = s[:close_bracket_idx].rfind('(')

        s = s[:open_bracket_idx] + \
            solver(s[open_bracket_idx+1:close_bracket_idx]) + s[close_bracket_idx+1:]

        close_bracket_idx = s.find(')')
    return s


def solve(s):
    s = remove_brackets(s, solve)
    # Now we've no brackets, lets take it one bit at a time, from the left and solve.
    chars = s.split(' ')

    lhs = 0
    op = ''
    for c in chars:
        if c in ['*', '+']:
            op = c
            continue
        if not lhs:
            lhs = int(c)
            continue

        if op == '*':
            lhs = lhs * int(c)
        else:  # op = '+'
            lhs = lhs + int(c)

    return str(lhs)


def part_one(sums):
    total = 0
    for s in sums:
        total += int(solve(s))

    return total


def solve_two(s):
    if len(s.split(' ')) == 3:
        return solve(s)

    s = remove_brackets(s, solve_two)
    chars = s.split(' ')
    try:
        idx = chars.index('+')
    except ValueError:
        idx = None
    while idx:
        chars = chars[:idx - 1] + \
            solve_two(' '.join(chars[idx-1:idx+2])).split(' ') + chars[idx+2:]
        try:
            idx = chars.index('+')
        except ValueError:
            idx = None

    # Now there's no plusses, just solve left to right
    return solve(' '.join(chars))


def part_two(sums):
    total = 0
    for s in sums:
        total += int(solve_two(s))

    return total


print("part one:", part_one(content))
print("part two:", part_two(content))
