# python 3.6

import random

# Problem: in a number of length n, what is the probability that all digits are unique?


def exact_prob_all_dig_unique(num_digits):
    if num_digits > 10:
        return 0
    if num_digits <= 1:
        return 1
    prob = 1
    pos_values = 10.
    counter = 1
    while num_digits > 1:
        prob *= (pos_values-counter)/pos_values
        counter += 1
        num_digits -= 1
    return prob


def monte_carlo_estimate_of_all_dig_unique(num_digits, num_trials=10000):
    if num_digits <= 1:
        return 1
    nums_w_unique_digits = 0.
    lower_bound = 10**(num_digits-1)
    upper_bound = 10**num_digits-1
    rand_nums = [random.randint(lower_bound, upper_bound) for _ in range(num_trials)]
    for i in rand_nums:
        if len(set(str(i))) == num_digits:
            nums_w_unique_digits += 1
    return nums_w_unique_digits/num_trials

print("\nProbability that all digits are unique in a number with n digits:\n")
print("Num Digits \t Exact Prob \t Estimated Prob")
for num_digits in range(1, 12):
    exact = exact_prob_all_dig_unique(num_digits)
    estimate = monte_carlo_estimate_of_all_dig_unique(num_digits)
    print(f"{num_digits} \t \t \t {exact:.5f} \t \t {estimate:.5f}")
