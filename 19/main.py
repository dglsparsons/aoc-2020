import regex as re

with open('input.txt', 'r') as f:
    content = f.read().split('\n\n')
    raw_rules = [r.strip() for r in content[0].split('\n')]
    initial_rules = {}
    initial_values = [r.strip() for r in content[1].split('\n')]
    for r in raw_rules:
        key, value = r.split(': ')
        value = value.replace('"', '')
        initial_rules[int(key)] = value


def part_one(rules, values):
    rules[0] = ' ' + rules[0] + ' '
    while any(f' {n} ' in rules[0] for n in rules):
        for n in rules:
            rules[0] = rules[0].replace(f' {n} ', ' (?: ' + rules[n] + ' ) ')

    regex = re.compile(rules[0].replace(' ', ''))
    return sum(1 for v in values if regex.fullmatch(v))


def part_two(rules, values):
    rules[8] = '(?: 42 )+'
    rules[11] = ' (?P<g11> 42 (?&g11)? 31 ) '
    rules[0] = ' ' + rules[0] + ' '
    while any(f' {n} ' in rules[0] for n in rules):
        for n in rules:
            rules[0] = rules[0].replace(f' {n} ', ' (?: ' + rules[n] + ' ) ')

    regex = re.compile(rules[0].replace(' ', ''))
    return sum(1 for v in values if regex.fullmatch(v))


print("part_one", part_one({k: v for k, v in initial_rules.items()}, initial_values))
print("part_two", part_two({k: v for k, v in initial_rules.items()}, initial_values))
