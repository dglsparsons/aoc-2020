with open('input.txt', 'r') as f:
    p1, p2 = [[int(n) for n in p.split('\n')[1:] if n] for p in f.read().split('\n\n')]


def take_turn(p1, p2):
    c1, c2 = p1[0], p2[0]
    if c1 > c2:
        return p1[1:] + [c1, c2], p2[1:]

    return p1[1:],  p2[1:] + [c2, c1]


def get_winning_score(hand):
    return sum((i+1) * n for i, n in enumerate(reversed(hand)))


def part_one(player1, player2):
    while len(player1) and len(player2):
        player1, player2 = take_turn(player1, player2)

    if player1:
        return get_winning_score(player1)

    return get_winning_score(player2)


def take_recursive_turn(p1, p2):
    c1, c2 = p1[0], p2[0]

    def copy(hand):
        return [c for c in hand]

    if len(p1[1:]) >= c1 and len(p2[1:]) >= c2:
        winner, e1, e2 = play_recursive_game(copy(p1[1:1+c1]), copy(p2[1:1+c2]))

        if winner == 'p1':
            return p1[1:] + [c1, c2], p2[1:]

        return p1[1:], p2[1:] + [c2, c1]

    if c1 > c2:
        return p1[1:] + [c1, c2], p2[1:]

    return p1[1:], p2[1:] + [c2, c1]


def hash(player1, player2):
    return ','.join(str(c) for c in player1) + ':' + ','.join(str(c) for c in player2)


def play_recursive_game(player1, player2):
    seen_hands = set()
    while len(player1) and len(player2):
        player1, player2 = take_recursive_turn(player1, player2)
        hashed = hash(player1, player2)
        if hashed in seen_hands:
            return 'p1', player1, player2
        seen_hands.add(hashed)

    if not player2:
        return 'p1', player1, player2

    return 'p2', player1, player2


def part_two(player1, player2):
    winner, p1, p2 = play_recursive_game(player1, player2)

    if winner == 'p1':
        return get_winning_score(p1)
    return get_winning_score(p2)


print("part one", part_one(p1, p2))
print("part two", part_two(p1, p2))
