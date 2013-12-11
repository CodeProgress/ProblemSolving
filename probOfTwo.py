#If you know a family has two children,
#and at least one of them is a boy born on Tuesday,
#what is the probability that the other child is a boy?

#Adapted from Udacity - Design of Computer Programs

import itertools
import fractions

days = 'SMTWtFs'
mf = 'mf'

#enumerate possible outcomes for one child ('Sm', 'Sf', 'Mm', ..., 'sf')
oneChild =  [''.join(x) for x in itertools.product(days, mf)]

#enumerate for two children ('SmSm', 'SmSf', 'SmMm', ..., 'sfsf')
twoChildren = [''.join(x) for x in itertools.product(oneChild, oneChild)]

#limit outcomes to those that have at least one boy born on a Tuesday
oneBoyTues = [x for x in twoChildren if 'Tm' in x]

#of those in oneBoyTues, limit to those that have two boys
twoBoys = [x for x in oneBoyTues if x[1] == 'm' and x[3] == 'm']

#prepare to be surprised
print fractions.Fraction(len(twoBoys), len(oneBoyTues))
