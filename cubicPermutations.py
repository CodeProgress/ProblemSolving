#Problem Statement:
#The cube, 41063625 (3453), can be permuted to produce two other cubes: 
#56623104 (3843) and 66430125 (4053). 
#In fact, 41063625 is the smallest cube which has exactly three permutations 
#of its digits which are also cube.
#
#Find the smallest cube for which exactly five permutations of its digits are 
#cubes.
#
#PEuler 62

#Solution:
#convert the digits of num**3 to a sorted tuple, i.e. a hashable histogram
#use this tuple as a key and num**3 as the values
#numbers with the same histogram are permutations
#return min value when a key has the desired number of values

def cubes(start = 1):
    '''generator, yields cubes: 1, 8, 27, 64...
    '''
    num = start
    while True: 
        yield num**3
        num += 1

def create_hist(num):
    '''returns the digits of num as a sorted tuple, i.e. a hashable histogram
    '''
    return tuple(sorted(str(num)))

def smallest_cube(numPerms):
    '''returns the smallest cube for which exactly numPerms permutations of its
    digits are cubes
    numPerms: int > 1
    '''
    assert numPerms > 1
    cubeVals = cubes()
    cubesDict = {}
    flag = False        
    posAnswers = []
    maxDigits = 1
    count = 0
    for i in cubeVals:
        #continue iterating until next order of mag to guarantee smallest value
        if flag:
            count += 1
            numDigits = len(str(i))
            #check if next order of magnitude has been reached
            if numDigits > maxDigits:
                assert maxDigits != 1
                break 
        cubeAsHist = create_hist(i)
        if cubeAsHist in cubesDict:
            cubesDict[cubeAsHist].append(i)
            if len(cubesDict[cubeAsHist]) == numPerms:
                if flag:
                    posAnswers.append(min(cubesDict[cubeAsHist]))
                else:
                    flag = True
                    #Set current order of magnitude
                    maxDigits = len(str(i))
                    posAnswers.append(min(cubesDict[cubeAsHist]))
        else:
            cubesDict[cubeAsHist] = [i]

    return min(posAnswers)


print smallest_cube(5)

