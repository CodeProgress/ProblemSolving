"""
For an integer N, find the least positive integer X made up of only 9's and 0's, such that X is a multiple of N

X contains one ore more 9s and zero or more 0s

Input
The first line contains an integer T, the number of test cases
Next T lines contain integer N

Output
Print the answer X corresponding to each test case (no leading zeroes in X)

Constraints
1 <= T <= 1000
1 <= X <= 500
"""

import itertools

def get_nine_zero_combinations(num_repeat):
    return map(int, [''.join(x) for x in itertools.product('09', repeat=num_repeat)])

def get_special_num(n, list_of_nine_zero_combs):
    assert n >= 1 and n <= 500  # per the problem constraints
    zero_nine_numbers = list_of_nine_zero_combs
    for i in zero_nine_numbers:
        if i % n == 0:
            return i

nine_zero_combs = get_nine_zero_combinations(13)[1:]

num_tests = int(input())

for test in range(num_tests):
    print get_special_num(int(input()), nine_zero_combs)
    