#The file, poker.txt, contains one-thousand random hands dealt to two players.
#Each line of the file contains ten cards (separated by a single space):
#the first five are Player 1's cards and the last five are Player 2's cards. 
#You can assume that all hands are valid (no invalid characters or 
#repeated cards), each player's hand is in no specific order, 
#and in each hand there is a clear winner.
#
#How many hands does Player 1 win?
#
#PEuler 54
#
#coded on 2/3/13, modified 2/27/14
#

def convertNotation(card):
    convDictNums = {}
    for i in range(2,10):
                convDictNums[str(i)] = i
    convDictNames = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    convDictSuits = {'C':'c', 'H':'h', 'S':'s', 'D':'d'}
    convDictAll   = dict(convDictNums.items() 
                         + convDictNames.items() 
                         + convDictSuits.items()
                         )
    
    return convDictAll[card[0]], convDictAll[card[1]]


def rankHand(hand):
    #for resolving high pair/kickers
    rankDict = {14:'m', 13:'l', 12:'k', 11:'j', 10:'i', 9:'h', 8:'g',\
                7:'f', 6:'e', 5:'d', 4:'c', 3:'b', 2:'a'} 
    
    hand.sort(reverse = True)
    
    card0 = hand[0]
    card1 = hand[1]
    card2 = hand[2]
    card3 = hand[3]
    card4 = hand[4]
    
    #rank = card0[0]
    #suit = card0[1]
    
    
    #9) straight flush
    if (card0[0] - card1[0] == 1 and
        card1[0] - card2[0] == 1 and
        card2[0] - card3[0] == 1 and
        card3[0] - card4[0] == 1) and \
        (card0[1] == card1[1] == card2[1] == card3[1] == card4[1]):
            rank = '9' + rankDict[card0[0]]
            return rank
    elif (card1[0] - card2[0] == 1 and
        card2[0] - card3[0] == 1 and
        card3[0] - card4[0] == 1 and
        card0[0] == 14) and \
        (card0[1] == card1[1] == card2[1] == card3[1] == card4[1]):
            rank = '9' + rankDict[card1[0]]
            return rank
        
    #8) four of a kind
    elif card0[0] == card1[0] == card2[0] == card3[0]:
        rank = '8'
        for i in hand:
            rank += rankDict[i[0]]
        return rank
    elif card1[0] == card2[0] == card3[0] == card4[0]:
        rank ='8'
        for i in hand[1:]:
            rank += rankDict[i[0]]
        rank += rankDict[card0[0]]
        return rank                 

    #7) full house
    elif card0[0] == card1[0] == card2[0] and card3[0] == card4[0]: 
        rank = '7'
        for i in hand:
            rank += rankDict[i[0]]
        return rank
    elif card0[0] == card1[0] and card2[0] == card3[0] == card4[0]:
        rank = '7'
        for i in sorted(hand):
            rank += rankDict[i[0]]
        return rank

    #6) flush
    elif card0[1] == card1[1] == card2[1] == card3[1] == card4[1]:
        rank = '6'
        for i in hand:
            rank += rankDict[i[0]]
        return rank

    #5) straight
    elif card0[0] - card1[0] == 1 and \
         card1[0] - card2[0] == 1 and \
         card2[0] - card3[0] == 1 and \
         card3[0] - card4[0] == 1:
        rank = '5' + rankDict[card0[0]]
        return rank
    elif card1[0] - card2[0] == 1 and \
         card2[0] - card3[0] == 1 and \
         card3[0] - card4[0] == 1 and \
         card0[0] == 14:
        rank = '5' + rankDict[card1[0]]
        return rank

    #4) three of a kind
    elif card0[0] == card1[0] == card2[0]:
        rank = '4'
        for i in hand:
            rank += rankDict[i[0]]
        return rank
    elif card1[0] == card2[0] == card3[0]:
        rank ='4'
        for i in hand[1:4]:
            rank += rankDict[i[0]]
        rank += rankDict[card0[0]]
        rank += rankDict[card4[0]]
        return rank
    elif card2[0] == card3[0] == card4[0]:
        rank ='4'
        for i in hand[2:]:
            rank += rankDict[i[0]]
        rank += rankDict[card0[0]]
        rank += rankDict[card1[0]]
        return rank 

    #3) two pair
    elif card0[0] == card1[0] and card2[0] == card3[0]:
        rank = '3'
        for i in hand:
            rank += rankDict[i[0]]
        return rank
    elif card0[0] == card1[0] and card3[0] == card4[0]:
        rank ='3'
        rank += rankDict[card0[0]]
        rank += rankDict[card1[0]]
        rank += rankDict[card3[0]]
        rank += rankDict[card4[0]]
        rank += rankDict[card2[0]]
        return rank
    elif card1[0] == card2[0] and card3[0] == card4[0]:
        rank ='3'
        for i in hand[1:]:
            rank += rankDict[i[0]]
        rank += rankDict[card0[0]]
        return rank

    #2) pair
    elif card0[0] == card1[0]:
        rank = '2'
        for i in hand:
            rank += rankDict[i[0]]
        return rank
    elif card1[0] == card2[0]:
        rank ='2'
        for i in hand[1:3]:
            rank += rankDict[i[0]]
        rank += rankDict[card0[0]]
        rank += rankDict[card3[0]]
        rank += rankDict[card4[0]]
        return rank
    elif card2[0] == card3[0]:
        rank ='2'
        for i in hand[2:4]:
            rank += rankDict[i[0]]
        rank += rankDict[card0[0]]
        rank += rankDict[card1[0]]
        rank += rankDict[card4[0]]
        return rank
    elif card3[0] == card4[0]:
        rank ='2'
        for i in hand[3:]:
            rank += rankDict[i[0]]
        rank += rankDict[card0[0]]
        rank += rankDict[card1[0]]
        rank += rankDict[card2[0]]
        return rank 

    #1) high card
    else:
        rank = '1'
        for i in hand:
            rank += rankDict[i[0]]
        return rank

def countWins(player, textFile):
    """returns the number of times "player" won.
    player: 1 = player one, 2 = player two
    textFile: text file containing hands for player one and two
    """
    with open(textFile, 'r') as poker:
        content = poker.readlines()

    if player == 1:
        countWin = lambda p1, p2: p1 > p2
    elif player == 2:
        countWin = lambda p1, p2: p2 > p1
    else:
        raise TypeError("{} is an invalid player".format(player))

    counter = 0
    for line in content:
        hands   = str(line).split()
        player1 = [convertNotation(i) for i in hands[:5]]
        player2 = [convertNotation(i) for i in hands[5:]]
        if countWin(rankHand(player1), rankHand(player2)):
            counter += 1
                
    return counter

print countWins(1, 'pokerHands.txt')


