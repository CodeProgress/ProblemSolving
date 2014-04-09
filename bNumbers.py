#
#Working from left-to-right if no digit is exceeded by the digit to its left
#it is called an increasing number; for example, 134468.
#
#Similarly if no digit is exceeded by the digit to its right it is called a
#decreasing number; for example, 66420.
#
#We shall call a positive integer that is neither increasing nor decreasing
#a "bouncy" number; for example, 155349.
#
#Clearly there cannot be any bouncy numbers below one-hundred, but just over
#half of the numbers below one-thousand (525) are bouncy. In fact, the least
#number for which the proportion of bouncy numbers first reaches 50% is 538.
#
#Surprisingly, bouncy numbers become more and more common and by the time we
#reach 21780 the proportion of bouncy numbers is equal to 90%.
#
#Find the least number for which the proportion of bouncy numbers
#is exactly 99%.

#PEuler 112


def is_bouncy(x):
    asString = str(x)
    asList = list(asString)
    xSorted = sorted(asString)

    isIncreasing = xSorted == asList        #boolean
    
    if isIncreasing: return False
    
    isDecreasing = xSorted[::-1] == asList  #boolean

    if isDecreasing: return False
    
    return True


def is_bouncy_rec(x, incr = None):
    """returns True if x is bouncy, False otherwise
    (Recursive version
    Twice as fast as isBouncy for numbers < one million
    exponentially faster for larger numbers
    ex:  is_bouncy_rec is   13 times faster for 2**5000
                            51 times faster for 2**50000
                           385 times faster for 2**500000
                          3170 times faster for 2**5000000)
    """

    #base case
    if x == 0:return False

    a = x % 10

    x /= 10
    if x == 0: return False

    b = x % 10
    
    #handle when numbers are equal, and avoid max recursion depth
    #recursion depth guaranteed to be <= 10
    while b == a:
        a = x % 10
        x /= 10
        if x == 0: return False    
        b = x % 10

    direction = b > a
    if incr == None:      return is_bouncy_rec(x, direction)
    if incr == direction: return is_bouncy_rec(x, direction)
    return True


def num_when_bouncy_proportion(percentage = .99):
    bouncyCounter = 0.
    num = 1
    while bouncyCounter/num < percentage:
        num += 1
        if is_bouncy_rec(num):
            bouncyCounter += 1
    
    return num


def test():
    #unit test
    unitTestRange = xrange(1, 100000, 3573)
    output1 = [is_bouncy(x) for x in unitTestRange]
    output2 = [is_bouncy_rec(x) for x in unitTestRange]
    
    assert  output1 == output2 == [False, True, True, True, True, True, True, True,
                                    True, True, True, True, True, True, True, True, 
                                    True, True, True, False, True, True,True, True, 
                                    True, True, True, True]
    
    #regression test
    regTestRange = xrange(1, 10000000,137)
    output3 = [is_bouncy(x) for x in regTestRange]
    output4 = [is_bouncy_rec(x) for x in regTestRange]
    
    assert output3 == output4



test()
print num_when_bouncy_proportion()


