RULES = {}


def parse_containing_colours(line):
    contents = line.split('contain')[1]
    if 'no other bags' in contents:
        return []

    stripped_contents = (c.strip().split(' ') for c in contents.strip().split(','))
    return [(int(c[0]), ' '.join(c[1:3])) for c in stripped_contents]


with open('input.txt', 'r+') as f:
    for line in f:
        # Parse a rule
        bag_colour = ' '.join(line.split(' ')[0:2])
        print(bag_colour)

        contained_bag_colours = parse_containing_colours(line)
        print(contained_bag_colours)

        RULES[bag_colour] = contained_bag_colours


def contains_gold(bag, rules):
    if bag == 'shiny gold':
        return True

    return any(contains_gold(b[1], rules) for b in rules[bag])


count = 0
for bag in RULES:
    if bag == 'shiny gold':
        continue

    if contains_gold(bag, RULES):
        count += 1

print("count:", count)

# Part 2


def bag_count(bag, rules):
    if len(rules[bag]) == 0:
        print(f"bag count: {bag}, {rules[bag]}, 1")
        return 1

    subtotal = sum(b[0] * bag_count(b[1], rules) for b in rules[bag]) + 1
    print(f"bag count: {bag}, {rules[bag]}, {subtotal}")
    return subtotal


print("nested bags:", bag_count('shiny gold', RULES) - 1)
