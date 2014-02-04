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

#recursive solution:
    
class Pyramid(object):
    def __init__(self, capacity = 1.0):
        self.pyramid = {}
        self.capacity = capacity

    def update_glass(self, volume, row, col):
        """handles the excess from the add_volume method and updates pyramid
        """
        if (row, col) in self.pyramid:
            excess = self.add_volume(volume, row, col)    
            if excess:
                self.update_glass(excess/2., row+1, col)
                self.update_glass(excess/2., row+1, col+1)
        else:
            self.pyramid[(row, col)] = 0
            excess = self.add_volume(volume, row, col)    
            if excess:
                self.update_glass(excess/2., row+1, col)
                self.update_glass(excess/2., row+1, col+1)
        
        return self.pyramid

    def add_volume(self, volume, row, col):
        """adds volume to glass in pyramid, if excess return excess, else return 0
        """
        if self.pyramid[(row, col)] + volume > self.capacity:
            excess = (self.pyramid[(row, col)] + volume) - self.capacity
            self.pyramid[(row, col)] = self.capacity
            return excess
        self.pyramid[(row, col)] += volume
        return 0
    
    def pour_into_top(self, volume):
        self.update_glass(volume, 1, 1)
    
    def pour_into_custom(self, volume, row, col):
        """add volume to glass at row, col in pyramid
        """
        self.update_glass(volume, row, col)

    def vol_in_row_col(self, row, col):
        """returns the volume in the glass at row, col in pyramid
        """
        if (row, col) in self.pyramid:
            return self.pyramid[(row,col)]
        return 0


pyr = Pyramid()

pyr.pour_into_top(20)            #pouring in 20 litres
print pyr.vol_in_row_col(7, 3)  #row 7, col 3 = .71875 L

