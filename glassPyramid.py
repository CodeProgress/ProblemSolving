#
#Imagine a pyramid of 1 litre glasses:
#
#       1
#      2 3
#    4  5  6
#  7  8  9  10
#
#If you put more than 1 litre in the top glass,
#water overflows and fills equally the 2nd and 3rd glass. 
#Glass 5 will get water from both the 2nd glass and the 3rd glass. And so on... 
#If you have X litres of water and you put that water in the top glass, 
#how much water will be contained by jth glass in ith row. 
#
#Example: X = 2 litres. 
#1st row, 1st glass - 1 litre 
#2nd row, 1st glass - 1/2 litre 
#2nd row, 2nd glass - 1/2 litre

class Pyramid(object):
    def __init__(self, pourQuantity):
        self.pyramid = []
        self.pourQuantity = pourQuantity
        
    def add_glass(self):
        self.pyramid.append(Glass())
    
    def add_to_glass(self, glass, volume):
        #recursive approach
        #excess = glass.add(volume)
        #if excess:
        #   add_to_glass(glass.left, excess/2.)
        #   add_to_glass(glass.right, excess/2.)
        pass
        
        
    
class Glass(object):
    def __init__(self, row, col, capacity = 1):
        self.row      = row #redundant? Keep track with indices of pyramid?
        self.col      = col
        self.capacity = capacity
        self.holding  = 0

    def add(self, volume):
        """adds volume to glass, returns volume of overflow or 0 if no overflow
        volume: int or double
        """
        self.holding += volume
        if self.holding > self.capacity:
            excess = self.holding - self.capacity
            self.holding = self.capacity
            return excess
        return 0            #if no overflow, excess = 0


