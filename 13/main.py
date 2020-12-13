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


def check_buses(start_time, buses):
    for i, bus in enumerate(buses):
        if bus == 'x':
            continue

        bus_id = int(bus)
        if (start_time + i) % bus_id != 0:
            print(f"start time {start_time} doesn't work for buses {buses}")
            return False

    return True


def get_frequency(start_time, current_frequency, index, bus):
    offset = None
    while True:
        if (start_time + index) % bus == 0:
            if not offset:
                offset = start_time
            else:
                print(index, start_time, start_time - offset, offset)
                return start_time, start_time - offset, offset

        start_time += current_frequency


def part_two(buses):
    frequency = int(buses[0])
    start_time = frequency
    t = 0
    for i, bus in enumerate(buses):
        if bus == 'x':
            continue
        # Find the frequency that works for the next bus added
        # So how often there's a time that works for bus one and two.
        # This becomes the start_time.
        start_time, frequency, t = get_frequency(start_time, frequency, i, int(bus))
    return t


print("part one:", part_one(earliest_timestamp, bus_ids))
print("part two:", part_two(all_buses))
