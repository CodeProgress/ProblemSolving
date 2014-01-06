#  A jar has 1000 coins.  999 are fair and 1 is double headed.
#  Pick a coin at random, and toss it 10 times.
#  Given that you see 10 heads, what is the probability that the next toss of 
#  that coin will also be heads?

#  Monte Carlo simulation to approximate solution:

#  (simFinalTossProb() simulates around one million trials per second
#   benchmark: 100,000,000 trials returns around 0.752115379758)

import random

def simFinalTossProb(numDoubleHeaded = 1,
                      numFlips        = 10, 
                      numCoins        = 1000, 
                      numTrials       = 1000000
                     ):
    """
    returns the approximate probability as a float
    numDoubleHeaded, numFlips, numCoins, numTrials: integers

    #  A jar has numCoins coins, of which numDoubleHeaded are double headed.
    #  Pick a coin at random, and toss it numFlips times.
    #  Given that you see numFlips heads, 
    #  what is the probability that the next toss of that coin 
    #  will also be heads?
    #  This probability is approximated by running numTrials trials.
    """

    count = 0
    heads = 0
    condition = 1 - (float(numDoubleHeaded)/numCoins)
    
    for i in xrange(numTrials):
    
        x = random.random()
        
        if x < condition:
            flag = True
            for i in range(numFlips):
                outcome = int(random.random() + .5)
                if outcome == 0:
                    flag = False
                    break      
            if flag:
                count += 1
                heads += int(random.random() + .5)
    
        else:
            count += 1
            heads += 1
        
    return heads/float(count)

print simFinalTossProb()

