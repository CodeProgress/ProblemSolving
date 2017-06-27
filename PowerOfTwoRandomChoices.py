"""
Monte Carlo simulation of "The Power of Two Random Choices"

http://www.eecs.harvard.edu/~michaelm/postscripts/handbook2001.pdf

Summary:
"To motivate this survey, we begin with a simple problem that demonstrates a
powerful fundamental idea. Suppose that n balls are thrown into n bins, with
each ball choosing a bin independently and uniformly at random. Then the
maximum load, or the largest number of balls in any bin, is approximately
(log n)/(log log n) with high probability. Now suppose instead that the balls
are placed sequentially, and each ball is placed in the least loaded of d=2
bins chosen independently and uniformly at random. Azar, Broder, Karlin,
and Upfal showed that in this case, the maximum load is (log log n)/log d +
O(1) with high probability.
The important implication of this result is that even a small amount of
choice can lead to drastically different results in load balancing. Indeed,
having just two random choices (i.e., d = 2) yields a large reduction in
the maximum load over having one choice, while each additional choice
beyond two decreases the maximum load by just a constant factor."
-Mitzenmacher, Richa, Sitaraman


Sample output for n = 100,000, d=2

Outcome #1:
    n balls are thrown into n bins, with each ball choosing a bin independently and uniformly at random:
    {0: 36723, 1: 36948, 2: 18314, 3: 6103, 4: 1527, 5: 315, 6: 59, 7: 10, 8: 1}

Outcome #2:
    each ball is placed in the least loaded of d=2 bins chosen independently and uniformly at random:
    {0: 23951, 1: 52998, 2: 22151, 3: 900}

"""

import random
import collections
import pylab


def add_to_random_bucket(hash_table):
    # choose a random bucket and add to the value
    rand_bucket = random.randint(0, len(hash_table)-1)
    hash_table[rand_bucket] += 1


def add_via_pow_two_rand_choice(hash_table):
    # choose two random buckets, add to the one with the min load
    rand_bucket_1 = random.randint(0, len(hash_table)-1)
    rand_bucket_2 = random.randint(0, len(hash_table)-1)
    while rand_bucket_1 == rand_bucket_2:
        rand_bucket_2 = random.randint(0, len(hash_table) - 1)

    if hash_table[rand_bucket_1] < hash_table[rand_bucket_2]:
        hash_table[rand_bucket_1] += 1
    else:
        hash_table[rand_bucket_2] += 1


n = 100000
num_buckets = n
num_values = n

# Initialize all buckets' load to zero
hash_table = {x: 0 for x in range(num_buckets)}
hash_table_two = {y: 0 for y in range(num_buckets)}

for _ in range(num_values):
    add_to_random_bucket(hash_table)
    add_via_pow_two_rand_choice(hash_table_two)

# print(max(hash_table.values()), max(hash_table_two.values()))

hash_collection = collections.Counter(hash_table.values())
hash_two_collection = collections.Counter(hash_table_two.values())
print({x: hash_collection[x] for x in sorted(hash_collection)})
print({x: hash_two_collection[x] for x in sorted(hash_two_collection)})


# plotting
highest_val = max(max(hash_table.values()), max(hash_table_two.values()))
pylab.hist(list(hash_table.values()),
           range(highest_val+2),
           alpha=.5,
           label="Assign to One Random Bucket")
pylab.hist(list(hash_table_two.values()),
           range(highest_val+2),
           alpha=.5,
           label="Two Random Buckets, \nAssign to Bucket with Min Load")
pylab.legend()
pylab.xlabel("Load Factor")
pylab.ylabel("Number of Buckets with a Given Load Factor")
pylab.show()
