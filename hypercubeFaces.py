#Problem     : Find all groups of three hypercubes 
#              that have the same number of faces

#Output      : [(numFaces, [(m1, n1), (m2, n2), (m3, n3)]), ...]

#Example     : One solution for a group of two hypercubes:

#              a 4D hypercube has eight 3D faces 
#              a 3D hypercube has eight 0D faces
#              [(8, [(3, 4), (0,3)])]

#              numFaces = number of m dimensional faces
#              (m1, n1) = m dimensional hypercube, n dimensional hypercube

#Constraints : Hypercube dimensions <= 1000
#              0 <= m < n
#              m1, m2, m3, ... are all different
#              n1, n2, n3, ... are all different


from math import factorial
from itertools import combinations


def m_cube_faces_on_n_cube(m, n, facts = {}):
    """returns the number of m dimensional faces on an n dimensional hypercube
    m, n    : int
    assumes : 0 <= m < n
    facts   : dict (key = n, value = n!)
    
    Example using a 3D cube
    m_cube_faces_on_n_cube(2, 3) =  6 sides
    m_cube_faces_on_n_cube(1, 3) = 12 edges
    m_cube_faces_on_n_cube(0, 3) =  8 vertices
    """
    
    #memoize factorials
    if m not in facts:
        facts[m] = factorial(m)
        
    if n not in facts:
        facts[n] = factorial(n)
    
    if n-m not in facts:
        facts[n-m] = factorial(n - m)

    mFact = facts[m]
    nFact = facts[n]
    n_mFact = facts[n - m]
    
    #closed form expression for determining m dimensional faces on n cube
    numFaces = 2**(n - m) * (nFact / (mFact * n_mFact))
    
    return numFaces

def are_m_n_dif(group):
    """returns True if m1, m2, ... are all different and n1, n2 ... are all dif
    otherwise returns False
    """
    mUsed = {}
    nUsed = {}
    for i in group:
        if i[0] in mUsed or i[1] in nUsed:
            return False
        mUsed[i[0]] = True
        nUsed[i[1]] = True
    return True
    

def hypercubes_same_num_faces(groupSize, maxDimensions = 1000):
    """returns a list of tuples [(numFaces, [(m1, n1), (m2,n2), ... ]), ...]
    (m1, n1) = an n dimentional hypercube and m dimensional faces
    numFaces = m_cube_faces_on_n_cube(m, n)
    
    returns empty list if no solutions found
    
    groupSize: int (the length of the desired group)
    maxDimensions: int (upperbound on hypercube dimensions)
    """
    
    facesOnCubes = {}         # key   = output of m_cube_faces_on_n_cube
                              # value = list of (m,n) tuples that produce key
    
    m = 0
    n = 1
    while n <= maxDimensions:
        mTemp = m
        nTemp = n
        while mTemp >= 0:
            faces = m_cube_faces_on_n_cube(mTemp,nTemp)
            if faces in facesOnCubes:
                facesOnCubes[faces].append((mTemp,nTemp))
            else:
                facesOnCubes[faces] = [(mTemp,nTemp)]
            mTemp -= 1
                
        n += 1
        m += 1
    
    solutions = []
    
    for numFaces in facesOnCubes:
        cubes = facesOnCubes[numFaces]
        if len(cubes) > groupSize:
            for reSized in combinations(cubes, groupSize):
                if are_m_n_dif(reSized):
                    solutions.append((numFaces, list(reSized)))
        
        elif len(cubes) == groupSize:
            if are_m_n_dif(cubes):
                solutions.append((numFaces, cubes))

    return solutions


if __name__ == "__main__":
    print hypercubes_same_num_faces(3)

