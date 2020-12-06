from collections import Counter

with open('input.txt', 'r+') as f:
    groups = ((g.replace('\n', ''), len(g.split('\n'))) for g in f.read().strip().split('\n\n'))

    counts = ((Counter(g), l) for g, l in groups)

    everyone_answered = ([k for (k, v) in c.items() if v == l] for (c, l) in counts)
    print(sum(len(e) for e in everyone_answered))
