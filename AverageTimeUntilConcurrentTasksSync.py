# -*- coding: utf-8 -*-

'''
You've just finished unwrapping your holiday presents. You and your sister got 
brand-new smartphones, opening them at the same moment. You immediately both 
start doing important tasks on the Internet, and each task you do takes one to 
five minutes. (All tasks take exactly one, two, three, four or five minutes, 
with an equal probability of each). After each task, you have a brief moment of
clarity. During these, you remember that you and your sister are supposed to 
join the rest of the family for dinner and that you promised each other you'd 
arrive together. You ask if your sister is ready to eat, but if she is still 
in the middle of a task, she asks for time to finish it. In that case, you now 
have time to kill, so you start a new task (again, it will take one, two, three,
four or five minutes, exactly, with an equal probability of each). If she asks 
you if it's time for dinner while you're still busy, you ask for time to finish 
up and she starts a new task and so on. From the moment you first open your 
gifts, how long on average does it take for both of you to be between tasks at 
the same time so you can finally eat? (You can assume the “moments of clarity” 
are so brief as to take no measurable time at all.)
'''

import numpy


def getNewTaskDuration(low=1, high=5):
    return numpy.random.randint(low, high + 1)

def run_simulation(numTrials=200000):
    sumOfTotals = 0.
    
    for i in xrange(numTrials):
        total1 = getNewTaskDuration()
        total2 = getNewTaskDuration()
        while total1 != total2:
            if total1 < total2:
                total1 += getNewTaskDuration()
            else:
                total2 += getNewTaskDuration()
        sumOfTotals += total1
    
    return sumOfTotals/numTrials

print run_simulation()

