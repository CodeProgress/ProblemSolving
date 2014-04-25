# -*- coding: utf-8 -*-

#The radical of n, rad(n), is the product of the distinct prime factors of n
#
#For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42
#
#Let e(k) be the kth element in the sorted n column; 
#for example, e(4) = 8 and e(6) = 9
#
#If rad(n) is sorted for 1 <= n <= 100000, find e(10000)
#
#PEuler 124

def sieve_with_rad(limit):
    '''returns a list of all primes <= limit
    limit: positive integer
    modified sieve that keeps track of rad instead of only 0, 1 for isPrime
    '''
    sieve = [1 for x in xrange(limit + 1)]

    for posPrime in xrange(2, limit + 1):
        if sieve[posPrime] != 1:
            continue
        
        #multiply value being stored in sieve by the primes it's a multiple of
        for multiple in xrange(posPrime, limit + 1, posPrime):
            sieve[multiple] *= posPrime

    return sieve

def e(limit = 100000, place = 10000):
    radicalPairings = enumerate(sieve_with_rad(limit))
    return sorted(radicalPairings, key = lambda x: x[1])[place][0]

print e()
    
