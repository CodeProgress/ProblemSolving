#Starting with 1 and spiralling anticlockwise in the following way, 
#a square spiral with side length 7 is formed.
#
#37 36 35 34 33 32 31
#38 17 16 15 14 13 30
#39 18  5  4  3 12 29
#40 19  6  1  2 11 28
#41 20  7  8  9 10 27
#42 21 22 23 24 25 26
#43 44 45 46 47 48 49
#
#It is interesting to note that the odd squares lie along
#the bottom right diagonal, but what is more interesting 
#is that 8 out of the 13 numbers lying along both diagonals are prime; 
#that is, a ratio of 8/13 is about 61.5%.
#
#If one complete new layer is wrapped around the spiral above, 
#a square spiral with side length 9 will be formed. 
#If this process is continued, what is the side length of the square spiral 
#for which the ratio of primes along both diagonals first falls below 10%?
#
#PEuler58

def sieve(limit):
    """returns a list of all primes <= limit
    limit: positive integer
    """
    sieve = [0 for x in xrange(limit + 1)]
    primes = []
    for posPrime in xrange(2, limit + 1):
        if sieve[posPrime] != 0:
            continue
        primes.append(posPrime)
        for multiple in xrange(posPrime*2, limit + 1, posPrime):
            sieve[multiple] = 1
    return primes

def isPrime(n, primes):
    """returns True if n is prime, False otherwise
    primes: list of prime numbers from sieve function
    """
    limit = int(n**.5)
    for i in primes:
        if i > limit:
            return True
        if n % i == 0:
            return False

def findSideLen(underPercentage = .1, upper = 100000):            
    """returns the side length of the spiral where the ratio of numbers
    along the diagonals (numPrimes/totalNums) is less than underPercentage
    underPercentage: 0.0 < num < 1.0
    upper: int > 2, handles corner vals up to upper**2
    """
    primes = sieve(upper)  
    
    sideLen = 1
    numToCheck = 1
    numPrimes = 0.0
    totalNums = 1.0
    
    while numPrimes/totalNums > underPercentage or sideLen <= 1:
        sideLen += 2
        incrSide = sideLen -1
        for i in xrange(3):
            numToCheck += incrSide
            if isPrime(numToCheck, primes):
                numPrimes += 1
        numToCheck += incrSide #to make up for not doing bottom right corner
        totalNums += 4
     
    return sideLen

print findSideLen()

