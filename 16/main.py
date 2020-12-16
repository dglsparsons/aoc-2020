from parse import parse


def parse_rules(raw_rules):
    separated = (parse('{}: {}-{} or {}-{}', r) for r in raw_rules.split('\n'))
    return {k: (int(l1), int(h1), int(l2), int(h2))
            for k, l1, h1, l2, h2 in separated}


def parse_tickets(raw_nearby_tickets):
    lines = raw_nearby_tickets.split('\n')
    return [[int(v) for v in line.strip().split(',') if v] for line in lines[1:] if line]


with open('input.txt', 'r') as f:
    raw_rules, raw_my_ticket, raw_nearby_tickets = f.read().split('\n\n')
    rules = parse_rules(raw_rules)
    nearby_tickets = parse_tickets(raw_nearby_tickets)
    my_ticket = parse_tickets(raw_my_ticket)[0]


def is_valid(v, args):
    (l1, h1, l2, h2) = args
    if ((l1 <= v <= h1) or (l2 <= v <= h2)):
        return True
    return False


def is_completely_invalid(v, rules):
    for r, vs in rules.items():
        if is_valid(v, vs):
            return False

    return True


def part_one(rules, tickets):
    invalid = [v for t in tickets for v in t if is_completely_invalid(v, rules)]
    return sum(invalid)


def get_valid_tickets(rules, tickets):
    valid_tickets = []
    for t in tickets:
        valid = all(not is_completely_invalid(v, rules) for v in t)
        if not valid:
            continue

        valid_tickets += [t]
    return valid_tickets


def part_two(rules, tickets, my_ticket):
    valid_tickets = get_valid_tickets(rules, tickets)
    candidate_fields = {i: set(rules.keys()) for i in range(0, len(tickets[0]))}

    for i in range(0, 2):  # Do 2 passes, because I need to trigger a second round of elimination
        for t in valid_tickets:
            for i, v in enumerate(t):
                candidate_fields[i] = {f for f in candidate_fields[i] if is_valid(v, rules[f])}
                if len(candidate_fields[i]) == 1:
                    candidate_fields = {idx: fields if i == idx
                                        else {c for c in fields if c not in candidate_fields[i]}
                                        for idx, fields in candidate_fields.items()}
    total = 1
    for i, v in candidate_fields.items():
        if list(v)[0].startswith('departure'):
            print(my_ticket)
            print(i, v, my_ticket[i])
            total *= my_ticket[i]

    return total


print(raw_rules)
print("part_one:", part_one(rules, nearby_tickets))
print("part_two:", part_two(rules, nearby_tickets, my_ticket))
