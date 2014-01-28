
# -*- coding: utf-8 -*-
"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, 
is the first Fibonacci number for which the last nine digits are 1-9 pandigital
(contain all the digits 1 to 9, but not necessarily in order). 
And F2749, which contains 575 digits, is the first Fibonacci number 
for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits 
AND the last nine digits are 1-9 pandigital, find k.

PEuler104
"""

def are_start_end_pan_dig(start, end, goal = set('123456789')):
    """returns True if start is pandigital and end is pandigital, else False
    start, end:  ints
    """
    if set(str(end)) != goal:
        return False

    if set(str(start)[:9]) != goal:
        return False
        
    return True

def fib_start_end_gen():
    """generates the first 18 digits and last 9 digits of numbers 
    in the fib sequence and yields tuple (start, end) as ints
    """
    #keep track of starting 18 digits of fib number
    start, startNext = 0, 1
    
    #and last 9 digits of fib number
    end, endNext = 0, 1
    
    while True: 
        yield (start, end)
        end, endNext = endNext, (end + endNext) % 10**9 #leaves only last 9 dig
        start, startNext = startNext, start + startNext
        if startNext > 10**18:
            start /= 10                                 #removes last dig
            startNext /= 10                                 #if num > 10**18
        
def find_fib_pandig():
    """returns the Kth fib number where the first 9 digits and last 9 digits
    are pandigital
    """
    x = fib_start_end_gen()
    count = 0               #keep track of Kth fib
    while True:
        start, end = x.next()
        if are_start_end_pan_dig(start, end):
            return count
        count += 1
    
print find_fib_pandig()
