# Problem Statement:
# Start at the top of triangle.txt
# Move to one of the two adjacent numbers on the row below
# After reaching the final row, a path will have been created.
# Find the maximum possible sum for all paths.


#Recursive solution, takes around .01 seconds

def maxPathSum(tri):
    '''returns the highest path sum in tri
    tri: list of lists for each row of the triangle
    assumes lists are composed of ints
    '''
    #base case
    if len(tri[-1]) == 1:
        return tri[-1]

    #iterate through the second to last row and update each value
    for i in xrange(len(tri[-2])):
        #update tri[-2][i] by adding the max of the two adjacent nums of the last row
        tri[-2][i] += max(tri[-1][i], tri[-1][i+1])

    #recursive step
    return maxPathSum(tri[:-1])
    
with open('triangle.txt', 'r') as triangle:
    tri = [map(int, line.split()) for line in triangle]

print maxPathSum(tri)[0]
