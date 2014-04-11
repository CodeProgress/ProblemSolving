#It is well known that if the square root of a natural number is not an integer,
#then it is irrational. The decimal expansion of such square roots is infinite 
#without any repeating pattern at all.
#
#The square root of two is 1.41421356237309504880..., and the digital sum of
#the first one hundred decimal digits is 475.
#
#For the first one hundred natural numbers, find the total of the digital sums
#of the first one hundred decimal digits for all the irrational square roots.
#
#PEuler 80
#

import decimal


def sum_decimal(num, numDigits = 100):
    """returns the sum of the first numDigits of sqrt(num)
    """
    decimal.getcontext().prec = int(numDigits * 1.1)

    strDec = str(decimal.Decimal(num).sqrt())

    decPointIndex = strDec.index('.')

    return sum(map(int, strDec[0:decPointIndex] 
                         + strDec[decPointIndex+1 : numDigits+1]))

def nat_nums_decimal_sums(firstNatNums = 100, numDigits = 100):
    """returns the sum of sum_decimal(x) from 0 to firstNatNums 
    if x is not a perfect square
    """
    total = 0
    squares = set([x**2 for x in range(int(firstNatNums**.5)+1)])
    for i in range(firstNatNums):
        if i not in squares:
            total += sum_decimal(i, numDigits)
    
    return total

assert sum_decimal(2, 100) == 475

if __name__ == "__main__":
    print nat_nums_decimal_sums()

