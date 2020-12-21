with open('input.txt', 'r') as f:
    content = [(line.split(' (')[0], line.strip().split(' (')[1][:-1]) for line in f.readlines()]

_foods = [(i.split(' '), a[8:][1:].split(', ')) for i, a in content]


def part_one(foods):
    allergens = {}

    for ingredients, alls in foods:
        for a in alls:
            if a not in allergens:
                allergens[a] = set(ingredients)
                continue

            allergens[a] = {i for i in ingredients if i in allergens[a]}

    def is_allergen(i):
        for v in allergens.values():
            if i in v:
                return True
        return False

    non_allergen_count = 0
    for ingredients, _ in foods:
        for i in ingredients:
            if is_allergen(i):
                continue
            non_allergen_count += 1

    return non_allergen_count


def part_two(foods):
    allergens = {}

    for ingredients, alls in foods:
        for a in alls:
            if a not in allergens:
                allergens[a] = set(ingredients)
                continue

            allergens[a] = {i for i in ingredients if i in allergens[a]}

    # Now remove ingredients from allergens until they are all length 1
    while any(len(list(v)) > 1 for v in allergens.values()):
        copy = {k: v for k, v in allergens.items()}
        for k, v in copy.items():
            if len(list(v)) == 1:
                for k2, v2 in allergens.items():
                    if k2 == k:
                        continue
                    items = {item for item in v2 if item not in v}
                    copy[k2] = items

            allergens = copy

    stuff = sorted([f"{k},{list(v)[0]}" for k, v in allergens.items()])
    things = [s.split(',')[1] for s in stuff]
    return ','.join(things)


print("part one", part_one(_foods))
print("part two", part_two(_foods))
