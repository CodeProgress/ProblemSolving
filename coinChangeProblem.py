
# depth first search

seen_set = set()
solutions = set()

def num_ways_to_make_change(total, coins, change=()):
    for coin in sorted(coins):
        possible_change = tuple(sorted(change + (coin,)))
        if sum(possible_change) > total:
            break
        if possible_change not in seen_set:
            seen_set.add(possible_change)
            if sum(possible_change) == total:
                solutions.add(possible_change)
            else:
                num_ways_to_make_change(total, coins, possible_change)
    return solutions

print len(num_ways_to_make_change(100, (1, 5, 10, 25)))

