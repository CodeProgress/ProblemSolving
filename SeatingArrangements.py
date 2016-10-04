import itertools
import random

"""
IBM "Ponder This" Challenge, September 2016

It is impossible to seat three people (Alice, Bob, and Charlie) in three places
for six hours, while changing places each hour in such a way that each hour has
a different seating permutation and no one stays in his or her chair during two
consecutive hours. Here is an "almost" solution: 
A B C A B C
B C A C A B
C A B B C A

The only violation is the "B B" in the middle of the third line. 
Our challenge for this month is to design a seating plan for four people for
24 hours in such a way that they don't repeat the same seating arrangement, and
the number of violations is minimal, where violations refer to the same person
sitting in the same place he sat in during one of the two preceding hours.
Update (29/8): We count each person sitting violation separately, so ABCD-ABDC
counts as two violations; and having the same person sit on the same seat for
three consecutive hours count as three violations (t vs t+1; t+1 vs t+2 
and t vs t+2) etc.
"""

def count_violations(x, y, z):
    violations = 0
    for i in range(len(x)):
        if x[i] == y[i]:
            violations += 1
        if y[i] == z[i]:
            violations += 1
        if x[i] == z[i]:
            violations += 1
    return violations

def count_pair_violations(x, y):
    violations = 0
    for i in range(len(x)):
        if x[i] == y[i]:
            violations += 1
    return violations
    
num_trials = 10000
lowest = 1000
best_arrangement = []
for _ in range(num_trials): 
    seating_arrangements = [''.join(x) for x in itertools.permutations('abcd', 4)]
    random.shuffle(seating_arrangements)
    
    new_arrangement = [seating_arrangements.pop()]
    
    for i in seating_arrangements:
        if count_pair_violations(new_arrangement[0], i) == 0:
            new_arrangement.append(i)
            break
    
    seating_arrangements.remove(new_arrangement[-1])
    
    assert len(seating_arrangements) + len(new_arrangement) == 24
    
    while len(seating_arrangements) > 0:
        target_low_violations = 0
        while target_low_violations < 10:
            for i in seating_arrangements:
                if count_violations(new_arrangement[-2], new_arrangement[-1], i) == target_low_violations:
                    new_arrangement.append(i)
                    break
            if len(seating_arrangements) + len(new_arrangement) == 25:
                seating_arrangements.remove(new_arrangement[-1])
                assert len(seating_arrangements) + len(new_arrangement) == 24
                break
            target_low_violations += 1

    total = 0
    for i in range(2, len(new_arrangement)):
        num_violations = count_violations(
            new_arrangement[i], 
            new_arrangement[i-1],
            new_arrangement[i-2])
        total += num_violations
    
    if total < lowest:
        best_arrangement = new_arrangement[:]
        lowest = total
        print lowest, best_arrangement
        
assert set(best_arrangement) == set([''.join(x) for x in itertools.permutations('abcd', 4)])

for seating in map(list, zip(*best_arrangement)):
    print ''.join(seating)
