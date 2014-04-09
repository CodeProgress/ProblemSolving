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


def isBouncy(x):
    asString = str(x)
    asList = list(asString)
    xSorted = sorted(asString)

    isIncreasing = xSorted == asList        #boolean
    
    if isIncreasing: return False
    
    isDecreasing = xSorted[::-1] == asList  #boolean

    if isDecreasing: return False
    
    return True
 

bouncyCounter = 0.
num = 1
while bouncyCounter/num < .99:
    num += 1
    if isBouncy(num):
        bouncyCounter += 1

print num

