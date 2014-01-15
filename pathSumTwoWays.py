
with open('matrix.txt', 'r') as matrix:
    bigList = [[int(y) for y in x.split(',')] for x in matrix]

rowSize = len(bigList[0])
colSize = len(bigList)

minSumList = [[] for j in range(colSize)]

#top row

runningTotal = 0
for i in bigList[0]:
    minSumList[0].append(runningTotal+i)
    runningTotal += i

#subsequent rows
#minSum = number + min(val above, val left)

for row in range(1, colSize):
    for cell in range(rowSize):
        if cell == 0:
            minSumList[row].append(bigList[row][cell] \
            + minSumList[row-1][cell]) #no left val
        else:
            minSumList[row].append(bigList[row][cell] \
            + min(minSumList[row-1][cell], minSumList[row][cell-1]))

print minSumList[-1][-1]

#shortest path can also be found using Dijkstra's algorithm