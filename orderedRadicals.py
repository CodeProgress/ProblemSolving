
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

limit = 100000
place = 10000

radicalPairings = enumerate(sieve_with_rad(limit))
print sorted(radicalPairings, key = lambda x: x[1])[place][0]
    
