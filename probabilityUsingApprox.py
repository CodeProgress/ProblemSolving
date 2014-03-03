# -*- coding: utf-8 -*-
#If a box contains twenty-one coloured discs, 
#composed of fifteen blue discs and six red discs, 
#and two discs were taken at random, 
#it can be seen that the probability of taking two blue discs, 
#P(BB) = (15/21)×(14/20) = 1/2.
#
#The next such arrangement, 
#for which there is exactly 50% chance of taking two blue discs at random,
#is a box containing eighty-five blue discs and thirty-five red discs.
#
#By finding the first arrangement 
#to contain over 10^12 = 1,000,000,000,000 discs in total, 
#determine the number of blue discs that the box would contain.
#
#PEuler100



import fractions
import time

def calcProb(numBlue, numRed):

    total = numBlue + numRed
    
    prob1 = fractions.Fraction(numBlue, total)
    prob2 = fractions.Fraction(numBlue - 1, total - 1)

    return prob1 * prob2

def calcProb2(x, total):
    return x/float(total) * (x-1)/float(total-1)
    
        
def findNumBlue4(total):
    magicNum = 2**.5 /2.
    blue = int(total * magicNum)+1
    return (blue, calcProb(blue, total-blue))
    #return (blue, calcProb2(blue, total))
   
def findFirst(start = 10**12):
    goal = fractions.Fraction(1,2)
    while findNumBlue4(start)[1] != goal:
        start += 1
    return start, findNumBlue4(start)

def findNextN(start, stopAfter = 10**12):
    """Uses successive approximation
    Issue: Breaks down at 10**16...
    """
    magicNum = 0.175
    temp = findFirst(start)[0]
    #print temp
    while True:
        result = findFirst(int(temp/magicNum))
        magicNum = temp/float(result[0])
        temp = result[0]
        if temp > stopAfter:
            return result
        if temp > stopAfter << 4:
            return None
        print temp

goal = fractions.Fraction(1, 2)
assert calcProb(15, 6) == goal
assert calcProb(85, 35) == goal


start = time.clock()
print findNextN(10, 10**12)
print time.clock()-start
