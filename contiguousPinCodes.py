import cProfile
import pylab

# Problem to solve:  How many pin code combinations are there if the combination
# only uses contiguous numbers?

# typical phone configuration

# 1 2 3
# 4 5 6
# 7 8 9
#   0

# contiguous is defined here as diagonal or orthogonal to a given number:

contiguous = {1: [2, 4, 5], 
              2: [1, 3, 4, 5, 6],
              3: [2, 5, 6],
              4: [1, 2, 5, 7, 8],
              5: [1, 2, 3, 4, 6, 7, 8, 9],
              6: [2, 3, 5, 8, 9],
              7: [4, 5, 8, 0],
              8: [4, 5, 6, 7, 9, 0],
              9: [5, 6, 8, 0],
              0: [7, 8, 9]
              }

def get_num_combos_recursive(pinLength):
    if pinLength <= 0:
        return 0
    if pinLength == 1:
        return 1
    total = 0
    for i in range(10):
        total += get_num_combos_recursive_helper_with_memo(pinLength, i)
    return total

def get_num_combos_recursive_helper(pinLength, startingNum):
    if pinLength <= 1:
        return 1
    total = 0
    for i in contiguous[startingNum]:
        total += get_num_combos_recursive_helper(pinLength-1, i)
    return total

memo = {}
def get_num_combos_recursive_helper_with_memo(pinLength, startingNum):
    if pinLength <= 1:
        return 1
    if (pinLength, startingNum) in memo:
        return memo[(pinLength, startingNum)]
    else:
        total = 0
        for i in contiguous[startingNum]:
            total += get_num_combos_recursive_helper_with_memo(pinLength-1, i)
        memo[(pinLength, startingNum)] = total
        return total

def get_num_combos_iterative_pin_length_nine():
    '''written in this ridiculous nested loop for educational purposes'''
    numCombos = 0
    for i in range(10):
        for j in contiguous[i]:
            for k in contiguous[j]:
                for m in contiguous[k]:
                    for n in contiguous[m]:
                        for p in contiguous[n]:
                            for q in contiguous[p]:
                                for r in contiguous[q]:
                                    for s in contiguous[r]:
                                        numCombos += 1
    return numCombos

def get_num_combos_estimate(pinLength):
    if pinLength < 1:
        return 0
    return 10 * 5**(pinLength-1)

def estimated_ratio_of_search_space_contiguous_vs_random(pinLength):
    return float(get_num_combos_estimate(pinLength))/(10**pinLength)

print get_num_combos_recursive(9)
print get_num_combos_iterative_pin_length_nine()


#cProfile.run('get_num_combos_recursive(9)')
#cProfile.run('get_num_combos_iterative_pin_length_nine()')
#cProfile.run('get_num_combos_estimate(9)')

actuals = []
estimates = []

for i in range(9):
    actuals.append(get_num_combos_recursive(i))
    estimates.append(get_num_combos_estimate(i))

pylab.plot(actuals)
pylab.plot(estimates)
pylab.title("Actual vs. Estimate")
pylab.show()

# Contiguous pin code combinations grow at roughly 10 * 5**(pinLength-1)
# Random pin codes grow at 10**pinLength
