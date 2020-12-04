import re


def validate_height(v):
    num_part = v[:-2]
    if not num_part:
        return False
    num = int(num_part)

    if v.endswith('cm'):
        return 150 <= num <= 193

    return 59 <= num <= 76


IS_VALID = {
    'byr': lambda v: 1920 <= int(v) <= 2002,
    'iyr': lambda v: 2010 <= int(v) <= 2020,
    'eyr': lambda v: 2020 <= int(v) <= 2030,
    'hgt': validate_height,
    'hcl': lambda v: re.match(r"#[0-9a-f]{6}$", v) is not None,
    'ecl': lambda v: v in 'amb blu brn gry grn hzl oth',
    'pid': lambda v: len(v) == 9
}


REQUIRED_FIELDS = set(IS_VALID.keys())

with open('input.txt', 'r+') as file:
    all_passports = file.read().split('\n\n')

normalised_passports = (p.replace('\n', ' ').strip().split(' ') for p in all_passports)

passports = ({f.split(':')[0]: f.split(':')[1] for f in p} for p in normalised_passports)

passports_with_only_useful_fields = (
    {k: v for (k, v) in p.items() if k in REQUIRED_FIELDS} for p in passports)

valid_passport_values = ({k for (k, v) in p.items() if IS_VALID[k](v)}
                         for p in passports_with_only_useful_fields)

intersects = (p for p in valid_passport_values if p.intersection(
    REQUIRED_FIELDS) == REQUIRED_FIELDS)
valid_count = sum(1 for p in intersects)

print(valid_count)
