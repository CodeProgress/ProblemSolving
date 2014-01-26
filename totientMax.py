def genPrimes():
    """Prime number generator.
    """
    primes = []
    q = 2  
    while True:
        isPrime = True
        upper = int(q**.5)
        for i in primes:
            if i > upper:
                isPrime = True
                break
            if q%i == 0:
                isPrime = False
                break
        if isPrime:
            yield q
            primes.append(q)
        
        q += 1
        
def findTotMax(limit = 1000000):
    primeGenerator = genPrimes()
    totMax = 1
    while totMax < limit:
        #print totMax
        prime = primeGenerator.next()
        temp = prime
        totMax *= prime
    
    return totMax/temp

print findTotMax()