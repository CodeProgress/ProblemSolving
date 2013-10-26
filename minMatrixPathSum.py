#In an NxN matrix of integers, find the minimal path sum 
#from the top left cell to the bottom right cell
#by only moving to the right and down

#example:

#131    673     234     103     18
#201	96	342	965	150
#630	803	746	422	111
#537	699	497	121	956
#805	732	524	37	331

#minimal path = 2427

#Problem:
#Find the minimal path sum in bigMatrix.txt
#Dimensions: 80x80S


with open('bigMatrix.txt', 'r') as matrix:
    bigList = [[int(y) for y in x.split(',')] for x in matrix]

numRows = len(bigList[0])
numCols = len(bigList)

minSumList = [[] for j in range(numCols)]

#first row

runningTotal = 0
for val in bigList[0]:
    minSumList[0].append(runningTotal + val)
    runningTotal += val

#subsequent rows, use dynamic programming
#minSum = cell value + min(val above, val left)

for row in range(1, numCols):
    for cell in range(numRows):
        if cell == 0:   #no left value, so just add above value
            minSumList[row].append(bigList[row][cell] \
            + minSumList[row-1][cell])
        else:
            minSumList[row].append( \
            bigList[row][cell]      \
            + min(minSumList[row-1][cell], minSumList[row][cell-1]))

print minSumList[-1][-1] #solution: 427337
