
def bowling_score(rollsList):
    """returns the final score for a complete game
    rollsList = [int, int, int, ...]

    Tests:
    >>> rollsList = [10,10,5,4,3,7,10,4,5,10,9,1,10,10,2,3]
    >>> bowling_score(rollsList)
    178
    >>> rollsList2 = [10]*12
    >>> bowling_score(rollsList2)
    300
    >>> rollsList3 = [10]*11
    >>> rollsList3.append(9)
    >>> bowling_score(rollsList3)
    299
    >>> rollsList2 = [0]*22
    >>> bowling_score(rollsList2)
    0
    """

    index = 0       #keep track of position within list
    score = 0
    frame = 0

    while frame < 10:
        frame += 1

        #stirke
        if rollsList[index] == 10:
            score += 10
            score += rollsList[index + 1]
            score += rollsList[index + 2]
            index += 1

        #spare
        elif rollsList[index] + rollsList[index + 1] == 10:
            score += 10
            score += rollsList[index + 2]
            index += 2

        else:
            score += rollsList[index]
            score += rollsList[index + 1]
            index += 2
    
    return score

if __name__ == "__main__":
    import doctest
    doctest.testmod()

