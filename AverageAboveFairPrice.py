# -*- coding: utf-8 -*-
'''
You go to buy a specific car, whose fair price we’ll call N. You have absolutely
no idea what N is and the dealer, sadistic capitalist that he is, won’t tell 
you. The dealer enjoys a good chase, though, so without directly revealing the
value of N, he takes five index cards and writes down a number on each of them:
    N, N+100, N+200, N+300 and N+400. 
Important: the guy’s sadistic but not a math major. 
The numbers on the cards are numbers,not algebra equations.

He presents the cards to you, one at a time, in random order. 
(For example, if the price on the second card is $100 more than the first, 
you can’t be sure if those are the two smallest prices, the two largest, 
or somewhere in between.) Each time he shows you a card, you must either 
pay the price on that card, or ask to see the next card. You cannot go back to 
previous cards. If you make it to the fifth and final card, then that is what 
you must pay. If you play the dealer’s game optimally, how much should you 
expect to pay on average above the fair price N?
'''

#Monte Carlo approach for quick conceptualization
import random

numTrials = 1000
n = 500
baseLineOutcome = n + 200

prices = [n + (i*100) for i in range(5)]

outcomesTotal = 0.

# example strategy
for trial in range(numTrials):
    random.shuffle(prices)
    chosenPrice = prices[0]
    if prices[1] > prices[0]:
        chosenPrice = prices[1]
    elif prices[2] > prices[0]:
        chosenPrice = prices[2]
    elif prices[3] > prices[0]:
        chosenPrice = prices[3]
    else: 
        chosenPrice = prices[4]
    outcomesTotal += chosenPrice

averageOutcome = outcomesTotal/numTrials
percentAboveBaseline = (averageOutcome-baseLineOutcome)/baseLineOutcome*100

print 'The example strategy performed {} percent above the baseline'.format(percentAboveBaseline)

