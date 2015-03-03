
# What are the last 10 digits of 2^(3^(4^(5^(6^(7^(8^9)))))) ?

def keep_last_ten(num):
    return num % 10**10

def fast_exp(base, exp):
    assert exp >= 0
    # base case
    if exp == 0: return 1
    if exp == 1: return base
    # recursive steps
    if exp % 2 == 0: return keep_last_ten(fast_exp(base, exp/2)**2)
    return keep_last_ten(base * fast_exp(base, exp - 1))


# each step written out to gain intuition
a = 9
b = fast_exp(8, a)
c = fast_exp(7, b)
d = fast_exp(6, c)
e = fast_exp(5, d)
f = fast_exp(4, e)
g = fast_exp(3, f)
h = fast_exp(2, g)
print h


# using while loop
def solve_with_while_loop(startingNum):
    assert startingNum > 0
    if startingNum == 1: return 0
    if startingNum == 2: return 1
    ans = startingNum
    while startingNum > 2:
        ans = fast_exp(startingNum - 1, ans)
        startingNum -= 1
    return ans

assert solve_with_while_loop(1) == 0
assert solve_with_while_loop(2) == 1
assert solve_with_while_loop(3) == 8
assert solve_with_while_loop(4) == (2**(3**4))%(10**10)

print solve_with_while_loop(9)
   

# recursive
def solve_with_recursion(startingNum):
    return rec_helper(startingNum, startingNum)

def rec_helper(a, ans):
    assert a > 0
    # base cases
    if a <= 3: return fast_exp(a-1, ans)
    # recursive step
    return rec_helper(a-1, fast_exp(a-1, ans))

assert solve_with_recursion(1) == 0
assert solve_with_recursion(2) == 1
assert solve_with_recursion(3) == 8
assert solve_with_recursion(4) == (2**(3**4))%(10**10)

print solve_with_recursion(9)


