def recursive_search(column_input, options, upper_half_char):
    if len(column_input) == 1:
        return options[1] if column_input[0] == upper_half_char else options[0]

    middle = int(len(options) / 2)

    new_options = options[middle:] if column_input[0] == upper_half_char else options[:middle]
    return recursive_search(column_input[1:], new_options, upper_half_char)


with open('input.txt', 'r+') as f:
    max_id = 0
    seats = set()
    for line in f:
        row = recursive_search(
            line[0:7],
            list(range(0, 128)),
            'B',
        )
        column = recursive_search(
            line[7:],
            list(range(0, 8)),
            'R'
        )

        seat_id = row * 8 + column
        seats.add(seat_id)

        if seat_id > max_id:
            max_id = seat_id

    # Part 1
    print(f"Max ID found is {max_id}")

    # Part 2
    for seat in sorted(list(seats)):
        if (seat + 1) not in seats:
            print(f"EMPTY SEAT: {seat + 1}")
            break
