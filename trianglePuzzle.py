# Problem Statement:
# Start at the top of triangle.txt
# Move to one of the two adjacent numbers on the row below
# After reaching the final row, a path will have been created.
# Find the maximum possible sum for all paths.

def maxPathSum(tri):
    '''returns the max path sum in tri
    tri: list of lists for each row of the triangle
    assumes values in lists are ints
    '''
    place = len(tri) - 1
    updatedRow = tri[place][:] # avoid mutating original list
    
    while place > 0:
        for i in xrange(place):
            updatedRow[i] = tri[place-1][i] + max(updatedRow[i], updatedRow[i+1])
        place -= 1

    return updatedRow[0]

        
with open('triangle.txt', 'r') as triangle:
    tri = [map(int, line.split()) for line in triangle]

print maxPathSum(tri)
