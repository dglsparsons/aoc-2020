from math import ceil

with open('input.txt', 'r') as f:
    content = f.read().splitlines()
    earliest_timestamp = int(content[0])
    all_buses = [x for x in content[1].split(',')]
    bus_ids = [int(t) for t in all_buses if t != 'x']


def part_one(timestamp, buses):
    best_bus_id = None
    nearest_time = None

    for bus in buses:
        best_time = ceil(timestamp / bus) * bus

        if nearest_time and best_time > nearest_time:
            continue

        best_bus_id = bus
        nearest_time = best_time

    return best_bus_id * (nearest_time - timestamp)


def part_two(buses):
    frequency = int(buses[0])
    start_time = frequency
    offset = 0
    for i, bus in enumerate(buses):
        if bus == 'x':
            continue

        # Find the offset that works with the next bus added
        # and how often there's a time that works for these busses.
        # This gives us a frequency to check for the next bus,
        # and the offset is the first time that works.
        # Do this for every bus, until we are good.
        offset = None
        while True:
            if (start_time + i) % int(bus) == 0:
                if not offset:
                    offset = start_time
                else:
                    frequency = start_time - offset
                    break

            start_time += frequency
    return offset


print("part one:", part_one(earliest_timestamp, bus_ids))
print("part two:", part_two(all_buses))
