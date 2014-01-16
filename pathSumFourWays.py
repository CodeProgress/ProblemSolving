##Find the minimal path sum, in matrix.txt, containing an 80x80 matrix,
##from the top left to the bottom right by moving up, down, right and left.

import networkx as nx

with open('matrix.txt', 'r') as matrix:
    bigList = [[int(y) for y in x.split(',')] for x in matrix]

#create node values as list
rowSize = len(bigList)
colSize = len(bigList[0])


def connect(G, node, maxRow = 80, maxCol = 80):
    '''node: tuple'''
    row, col = node
    #up
    if row > 0:
        G.add_edge(node, (row - 1, col), weight=bigList[row-1][col])

    #down
    if row < maxRow - 1:
        G.add_edge(node, (row + 1, col), weight=bigList[row+1][col])
        
    #right
    if col < maxCol - 1:
        G.add_edge(node, (row, col + 1), weight=bigList[row][col+1])
    
    #left
    if col > 0:
        G.add_edge(node, (row, col - 1), weight=bigList[row][col-1])
        

#create graph
G = nx.DiGraph()

nodesList = [(x,y) for x in range(rowSize) for y in range(colSize)]

for node in nodesList:
    connect(G, node)


shortestPath = nx.shortest_path_length(G, (0,0), (79,79), weight = 'weight') \
                + bigList[0][0]
    
print shortestPath


