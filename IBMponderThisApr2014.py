#IBM Ponder This Challenge, April 2014:
#Inspired by theviral 2048 game 
#(http://en.wikipedia.org/wiki/2048_%28video_game%29) game, this month's 
#question is a simpler one-dimensional version of it. Assume that random 
#independent numbers, either 2 or 4 with a 50% chance each, come in from the 
#right side of a bar with N slots. The numbers are always squeezed to the left 
#and every time two adjacent numbers are the same - they are replaced by their 
#sum. The game ends when all the N slots are occupied - and therefore there is 
#no room for a new number. 
#What is the expected maximum number in the array when the game ends? 
#When N=1, the game ends after one round, leaving either 2 or 4 with the same 
#probability and hence the average is 3. 
#When N=2, the game can reach 8 (for example, when the input is 2, 2, 4, 2, and
#the result is 8, 2), but can also be stuck with a 4 (such as when the input is
#2, 2, 2, and the result is 4, 2). 
#Computing the average we get 5.5, or 11/2.
#What is the average when N=5? 
#Express this value as a quotient of two coprime integers.

import fractions

def consolidate(board):
    """returns none, modifies board in place"""
    b = list(board)
    index = len(b) - 1
    while index > 0:
        if b[index] == b[index - 1]:
            b[index - 1] *= 2
            b.pop(index)
        index -= 1
    return tuple(b)


def ibm_april_2014(board = tuple(), depth = 0, numSlots = 5, memo = {}):
    if board in memo: 
        return memo[board] * 2

    if len(board) >= numSlots:
        score = max(board)
        probability = fractions.Fraction(1, 2**depth)
        return probability * score
        
    left = consolidate(board + (2,))
    right = consolidate(board + (4,))
    
    memo[left] = ibm_april_2014(left, depth+1, numSlots)
    memo[right] = ibm_april_2014(right, depth+1, numSlots)
    
    return  memo[left] + memo[right]
    
print ibm_april_2014()
