# -*- coding: utf-8 -*-

#How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper
#fractions for d ≤ 12,000?
import fractions 

total = 0
for x in range(1, 12000):
    for y in range(x/3 + 1, x/2+1):
        if fractions.gcd(x, y) == 1:
            total += 1
print total
