#The smallest number expressible as the sum of a prime square, prime cube, and 
#prime fourth power is 28. In fact, there are exactly four numbers below fifty 
#that can be expressed in such a way:
#
#28 = 22 + 23 + 24
#33 = 32 + 23 + 24
#49 = 52 + 23 + 24
#47 = 22 + 33 + 24
#
#How many numbers below fifty million can be expressed as the sum of a 
#prime square, prime cube, and prime fourth power?

#PEuler 87

def sieve(limit):
    """returns a list of all primes less than or equal to limit
    limit: int
    """
    if limit < 2:
        return []
    primes = [2]
    for i in range(3, limit+1):
        flag = True
        for p in primes:
            if i%p == 0:
                flag = False
                break
        if flag:
            primes.append(i)
    return primes

def num_prime_power_triples(limit):
    """returns num of unique sums where prime**2 + prime**3 + prime**4 < limit
    """
    uniqueSums = set()

    #narrow search space
    sqBound = int(limit**.5)  +1
    thBound = int(limit**.34) +1
    foBound = int(limit**.25) +1
    
    sqPrimes = sieve(sqBound)
    thPrimes = [x for x in sqPrimes if x < thBound]
    foPrimes = [x for x in sqPrimes if x < foBound]
    
    #find unique sums < limit
    for sq in sqPrimes:
        for th in thPrimes:
            if sq**2 + th**3 > limit: continue
            for fo in foPrimes:
                primePowerTriple = sq**2 + th**3 + fo**4
                if primePowerTriple < limit:
                    uniqueSums.add(primePowerTriple)
    
    return len(uniqueSums)

print num_prime_power_triples(50000000)


