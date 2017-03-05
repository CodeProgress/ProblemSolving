'''
Consider two sets of positive integers,  A and B. 
We say that a positive integer, x, is between sets A and B 
if the following conditions are satisfied:

    1) All elements in A are factors of x.
    2) x is a factor of all elements in B.

Given A and B, find and print the number of integers 
(i.e., possible 's) that are between the two sets.

Constraints:
    elements of a and b between 1 and 100
    a and b can have bewteen 1 and 10 elements
'''

def are_all_factors_of_x(x, nums):
    return all([i%x==0 for x in nums])

def is_x_factor_of_all(x, nums):
    return all([y%i==0 for y in nums])

a = [2, 4]
b = [16, 32, 96]

max_a = max(a)
min_b = min(b)

counter = 0
for i in range(max_a, min_b+1, max_a):
    if are_all_factors_of_x(i, a) and is_x_factor_of_all(i, b):
        counter += 1

print counter
