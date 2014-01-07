
#By counting carefully it can be seen that a rectangular grid measuring
#3 by 2 contains eighteen rectangles.
# 1x1: 6
# 1x2: 3
# 2x1: 4
# 2x2: 2
# 3x1: 2
# 3x2: 1
# -------
#   = 18

#Although there exists no rectangular grid that contains exactly 
#two million rectangles, find the area of the grid with the nearest 
#solution.

# PEuler-85

def count(x, y):
    '''counts the number of rectangles in a grid x by y
    x, y: ints
    '''
    return ( x*(x+1) * y*(y+1) )/4

def findArea(goal = 2000000):
    '''returns the area (int) of the grid with total rectangles closest to goal
    goal: int > 0
    '''
    assert goal > 0
    
    x = 1
    y = 1

    diff = goal
    smallestDiff = goal

    dimens = (1, 1)

    while True:
        numRec = count(x,y)
        diff = abs(goal - numRec)

        if diff < smallestDiff:
            smallestDiff = diff
            dimens = (x,y)
        
        if numRec < goal:
            x += 1
            y += 1
        else:
            x -= 1
        
        #terminating condition
        if x == 1:
            break
    
    return dimens[0]*dimens[1]


print findArea()
