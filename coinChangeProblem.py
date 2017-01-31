
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


# Dynamic programming.  Runtime = len(coins) * amount
def make_change(coins, amount):
    # make a row each coin including zero coins
    # make a col for each amount including zero
    solution_matrix = [[0]*(amount+1) for _ in range((len(coins)+1))]

    # There is one way to make change if the amount is zero
    for x in range(len(coins)+1):
        solution_matrix[x][0] = 1

    # There are zero ways to make change for amounts >= 1 if num coins is zero
    for y in range(1, amount+1):
        solution_matrix[0][y] = 0

    # incrementally fill in solution_matrix for all coins and all amounts
    # successive rows/cols build upon answers from previous rows/cols (overlapping sub problems)
    for coin_index in range(1, len(coins)+1):
        for amt in range(1, amount + 1):
            value_of_current_coin = coins[coin_index-1]
            num_ways_without_coin = solution_matrix[coin_index-1][amt]
            if value_of_current_coin <= amt:
                num_ways_with_coin = solution_matrix[coin_index][amt - value_of_current_coin]
                solution_matrix[coin_index][amt] = num_ways_without_coin + num_ways_with_coin
            else:
                solution_matrix[coin_index][amt] = num_ways_without_coin

    return solution_matrix[len(coins)][amount]

print make_change((1,5, 10, 25), 100)
