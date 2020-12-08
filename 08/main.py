

with open('input.txt', 'r+') as f:
    stuff = (l.strip() for l in f.readlines())
    commands = [(l.split(' ')[0], int(l.split(' ')[1])) for l in stuff]


def process_boot(instructions):
    visited = set()

    def _process_boot(index, acc):
        if index >= len(instructions):
            return acc

        if index in visited:
            raise ValueError(f"Infinite loop found at index {index}, acc {acc}")
        visited.add(index)

        if instructions[index][0] == 'jmp':
            return _process_boot(index + instructions[index][1], acc)
        if instructions[index][0] == 'acc':
            return _process_boot(index + 1, acc + instructions[index][1])

        # else it's a noop
        return _process_boot(index + 1, acc)

    return _process_boot(0, 0)


# Part 1
try:
    process_boot(commands)
except ValueError as e:
    print(e)


# Part 2
jmp_indexes = [i for (i, j) in enumerate(commands) if j[0] == 'jmp']

for i in jmp_indexes:
    commands[i] = ('nop', commands[i][1])
    try:
        print(process_boot(commands))
    except ValueError as e:
        pass
    commands[i] = ('jmp', commands[i][1])
