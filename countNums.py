
#How many 20 digit numbers n (without any leading zero) exist such that no three
#consecutive digits of n have a sum greater than 9?
#
#PEuler 164


def count_nums(numDigits = 20, threeConsecLimit = 9):
    if numDigits < 2:
        return -1
    
    firstTwo = {(x,y):1 for x in range(1,10) 
                            for y in range(10) 
                                if x+y <= threeConsecLimit}
    
    for i in range(numDigits - 2):
        nextTwo = {}
        for a, b in firstTwo.keys():
    
            posThirdVals = range(9 - a - b + 1)
    
            for c in posThirdVals:
                if (b,c) in nextTwo:
                    nextTwo[(b, c)] += firstTwo[(a,b)]
                else:
                    nextTwo[(b, c)] = firstTwo[(a, b)]
            
        firstTwo = nextTwo

    return sum(firstTwo.values())

def count_nums_rec(numDigits=20, firstTwo=None):
    """recursive implementation"""

    if firstTwo == None:
        firstTwo = {(x,y):1 for x in range(1,10) 
                            for y in range(10) 
                                if x+y <= 9}
    #Base Case    
    if numDigits <= 2:
        return sum(firstTwo.values())
    
    nextTwo = {}
    for a, b in firstTwo.keys():
        posThirdVals = range(9 - a - b + 1)
        for c in posThirdVals:
            if (b,c) in nextTwo:
                nextTwo[(b, c)] += firstTwo[(a,b)]
            else:
                nextTwo[(b, c)] = firstTwo[(a, b)]
        
    return count_nums_rec(numDigits - 1, nextTwo) 


assert count_nums(2) == 45
assert count_nums(3) == 165

assert count_nums_rec(2) == 45
assert count_nums_rec(3) == 165

result     = count_nums()
result_rec = count_nums_rec()

assert result == result_rec

print result

