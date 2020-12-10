from copy import copy
from functools import reduce


def do_thing():
    with open('input.txt', 'r') as f:
        so_far = {}
        for line in f:
            if not line:
                continue

            val = int(line)
            so_far[val] = [val]
            for k, v in copy(so_far).items():
                if len(v) > 2:
                    continue

                combined = [*v, val]
                total = sum(combined)
                if total == 2020:
                    print(combined)
                    print("total: ", reduce(lambda x, acc: x * acc, combined))
                so_far[total] = combined


do_thing()
