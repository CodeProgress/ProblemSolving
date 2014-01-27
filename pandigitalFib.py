
def are_start_end_pan_dig(start, end, goal = set('123456789')):
    """returns True if start is pandigital and end is pandigital
    start, end:  ints
    """
    if set(str(end)) != goal:
        return False
    #digits = int(math.log(x,10)) + 1
    if set(str(start)[:9]) != goal:
        return False
    return True

def fib_start_end_gen():
    """generates the starting 18 digits and ending 9 digits of the numbers 
    in the fib sequence and yields tuple (start, end) as ints
    """
    start, startNext = 0, 1
    end, endNext = 0, 1
    while True: 
        yield (start, end)
        end, endNext = endNext, (end + endNext) % 10**9
        start, startNext = startNext, start + startNext
        if startNext > 10**18:
            start /= 10
            startNext /= 10
        
def find_fib_pandig():
    """returns the Kth fib number where the first 9 digits and last 9 digits
    are pandigital
    """
    x = fib_start_end_gen()
    count = 0
    while True:
        start, end = x.next()
        if are_start_end_pan_dig(start, end):
            return count
        count += 1
    
print find_fib_pandig()
