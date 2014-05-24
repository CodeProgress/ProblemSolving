
# Recursive solution to the Towers of Hanoi problem

def hanoi(numDiscs, a = 1, b = 2, c = 3):
    #Base case
    if numDiscs <= 0: return
    
    #Recursive steps
    hanoi(numDiscs - 1, a, c, b)
    print "Move from {} to {}".format(a, b)
    hanoi(numDiscs - 1, c, b, a)

hanoi(3)
