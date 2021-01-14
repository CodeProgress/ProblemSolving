import matplotlib.pyplot as plt
import random

def sieve(limit):
    """return list of primes between 2 and limit, inclusive"""
    if limit <= 1:
        return []
    primes = []
    possible_primes = [None, None] + [x for x in range(2, limit + 1)]  # list(range(3, limit+1, 2))
    candidate_prime = 2
    while candidate_prime <= limit:
        primes.append(candidate_prime)
        multiple_of_candidate = candidate_prime*2
        while multiple_of_candidate <= limit:
            possible_primes[multiple_of_candidate] = None
            multiple_of_candidate += candidate_prime
        candidate_prime += 1
        while candidate_prime <= limit and possible_primes[candidate_prime] is None:
            candidate_prime += 1
    return possible_primes

def turn_right(direction):
    if direction == "n":
        return "e"
    if direction == "w":
        return "n"
    if direction == "s":
        return "w"
    if direction == "e":
        return "s"

def walk_step(current_location, direction):
    x, y = current_location
    dx, dy = direction_mapper[direction]
    return x + dx, y + dy


direction_mapper = {"n": (0, 1), "e": (1, 0), "s": (0, -1), "w": (-1, 0)}
limit = 100000
prime_list = sieve(limit)
random_walk = [(0, 0)]
direction = "w"
for num in prime_list:
    if num:
        curr_location = random_walk[-1]
        new_location = walk_step(curr_location, direction)
        random_walk.append(new_location)

    else:
        direction = turn_right(direction)
        #direction = random.choice("nesw")

seen = set()
random_walk_no_duplicate_locations = []
for loc in random_walk:
    if loc in seen:
        continue
    seen.add(loc)
    random_walk_no_duplicate_locations.append(loc)
print(len(random_walk), len(random_walk_no_duplicate_locations), len(random_walk)/len(random_walk_no_duplicate_locations))

x_list = [x[0] for x in random_walk_no_duplicate_locations]
y_list = [y[1] for y in random_walk_no_duplicate_locations]

plt.plot(x_list, y_list)
plt.scatter(x_list, y_list, c=range(len(random_walk_no_duplicate_locations)))    # c=range(len(random_walk)
plt.colorbar()
plt.show()