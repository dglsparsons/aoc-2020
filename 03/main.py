

# RIGHT_AMOUNT = 3
# DOWN_AMOUNT = 1


def get_count(right, down):
    with open('input.txt', 'r+') as f:
        x_position = 0
        tree_count = 0
        for i, line in enumerate(f):
            if (i % down != 0):
                continue
            if line[x_position] == '#':
                tree_count += 1
            x_position = (x_position + right) % (len(line) - 1)

        print("tree count:", tree_count)
        return tree_count


count = 1
for (right, down) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    count *= get_count(right, down)
print(f"total trees: {count}")
