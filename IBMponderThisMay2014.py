import itertools

def create_cart_prod(length):
    """returns a generator of the cartesian product of [0,1], repeat = length"""
    return itertools.product([0,1], repeat = length)

def are_all_gone(shots, numShots):
    if shots[-1] == 0: 
        return False                #Last can't be slowest
    if sum(shots) < numShots/2: 
        return False                #Need at least half ones for all to cancel
        
    stack = [0]
    index = 0
    while index < len(shots):
        if shots[index] == 0: stack.append(0)
        else:
            if len(stack) == 0: stack.append(0)
            else: stack.pop()
        index += 1
    return len(stack) == 0

def prob_all_gone(numShots):
    numAllGone = 0.
    for i in create_cart_prod(numShots-1):
        if are_all_gone(i, numShots):
            numAllGone += 1.
    print numAllGone
    return numAllGone/(2**(numShots-1))

print prob_all_gone(20)



#print sim_trials(100000, 20)     # Expected = 0.176197052002
#
#sim_trials(100000000, 20)
#NumShots   = 2
#NumTrials  = 100,000,000
#Expected   = 0.176197052002
#Simulation = 0.17618738
#Dif        = 9.672e-06
#
