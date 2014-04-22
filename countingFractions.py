# -*- coding: utf-8 -*-

#How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper
#fractions for d <= 12,000?

import fractions

def count_fractions(lower, upper, n=12000):
    total = 0

    for x in xrange(1, n):
        for y in xrange(int(lower*x + 1), int(upper*x + 1)):
            if fractions.gcd(x, y) == 1:
                total += 1
    return total

lower = fractions.Fraction(1,3)
upper = fractions.Fraction(1,2)

print count_fractions(lower, upper)
