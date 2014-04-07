def num_fibs_below(numDigits):
    """returns how many Fibonacci numbers have less than numDigits digits.
    ex: num_fibs_below(2) -> 7 - since 0,1,1,2,3,5,8 have less than 2 digits
    
    PEuler 25
    """
    count = 0
    x, y  = 0, 1
    
    while len(str(x)) < numDigits:
        count += 1
        x, y   = y, x+y
    
    return count


assert num_fibs_below(1) == 0
assert num_fibs_below(2) == 7

print num_fibs_below(1000)

