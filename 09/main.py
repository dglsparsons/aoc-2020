

with open('input.txt', 'r+') as f:
    content = [int(line.strip()) for line in f.readlines()]

PREAMBLE_LENGTH = 25


def get_bad_value():
    for i, value in enumerate(content[PREAMBLE_LENGTH:]):
        # see if we can make the number from anything in the preamble
        index = i + PREAMBLE_LENGTH
        previous_numbers = content[index - PREAMBLE_LENGTH:index]

        def check_combo():
            for x in previous_numbers:
                for y in previous_numbers:
                    if x == y:
                        continue

                    if x + y == value:
                        return True
            return False

        if not check_combo():
            return value
    return None


# Part 1

bad_value = get_bad_value()
print(bad_value)


# Part 2

def check_contiguous_sum(thingies, bad_value):
    total = 0
    values = []
    for value in thingies:
        values = values + [value]
        total += value

        if total > bad_value:
            return None

        if total == bad_value:
            return values


# For each possible index, add value until bigger than the bad value.
# If exactly equal, return
for i in range(0, len(content)):
    result = check_contiguous_sum(content[i:], bad_value)
    if not result:
        continue

    print("Values found", result)

    smallest = min(result)
    biggest = max(result)
    print("weakness", smallest + biggest)
    break
