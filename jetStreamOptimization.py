# -*- coding: utf-8 -*-

'''
To save energy, a plane can use jet streams 
It gets the following input to help plan the flight:

The first line contains only 1 integer, which is the constant energy it takes to 
fly 1 mile WITHOUT jet streams.
Every subsequent line contains 3 space-separated integers: 
    the start mile marker of the jet stream, 
    the end mile marker of the jet stream, 
    and lastly an integer denoting the overall energy needed 
    to fly that jet stream’s distance.
    
For instance, the line "5 9 13" means it takes 13 energy units
to fly the 4 miles between miles 5 and 9.

Note that jet streams can overlap, 
but the plane cannot be on more than one jet stream at a time, 
and it cannot fly partial jet streams.

Consider the end mile marker of the farthest jet stream as the endpoint.

Write a program that takes in an input file streams.txt
to plan out the optimal sequence of jet streams the plane
should fly on to minimize energy consumption throughout the entire journey. 
All integers in the input file are non-negative. 
As output, print out the mininum total energy 
and a list of tuples denoting the jet streams’ endpoints.

For example, given this input:
23
0 5 29
1 5 6
2 4 3
1 2 1
4 5 1
the minimum total energy needed to fly all 5 miles is 28 energy units, 
and the optimal sequence of jet streams is [(1, 2), (2, 4), (4, 5)].
'''

with open('streams.txt', 'r') as text:

    allStreams = []
    
    constEnergy = int(text.readline())
    
    for i in text.readlines():
        stream = i.split()
        stream = tuple(int(x) for x in stream)
        allStreams.append(stream)

# sort by jet stream endpoint to avoid missing max endpoint distance
allStreams.sort(key = lambda x: x[1])  

# create list to hold: minEnergyConsumed and lastStreamTaken for all distances
energyForDist = []  # Indices represent distances from start

# start by appending constEnergy * distance to energyForDistance
for i in range(allStreams[0][1]+1):   # iterate to endpoint of first stream
    lastStreamTaken = None
    baseCostPerMile = i*constEnergy    
    energyForDist.append([baseCostPerMile, lastStreamTaken])

for i in range(len(allStreams)):      # iterate through all jet streams   
    start = allStreams[i][0]           # starting point of stream
    end = allStreams[i][1]             # endpoint of stream
    energy = allStreams[i][2]          # energy needed to travel stream
    
    lastStreamTaken = energyForDist[-1][1]
    prevBest = energyForDist[-1][0]
    streamBest = energyForDist[start][0] + energy
    
    if streamBest < prevBest:
        lastStreamTaken = i
        energyForDist[-1] = [streamBest, lastStreamTaken]

    # Append successive values to energyForDist until next stream's endpoint
    # successive values are incremented by constValue each iteration
    if i != len(allStreams) - 1: #not for last stream since it has no successor
        nextStreamEnd = allStreams[i+1][1]
        curEnd = len(energyForDist) - 1
        curVal = energyForDist[-1][0]
        for i in range(abs(curEnd - nextStreamEnd)):
            curVal += constEnergy
            energyForDist.append([curVal, lastStreamTaken])
        
minEnergyConsumption = energyForDist[-1][0]

# backtrack and unwind energyForDist to see which streams were taken
streamsTaken = []
finalStream = energyForDist[-1][1]

if finalStream == None:  # i.e. optimal to not take any jet streams
    print minEnergyConsumption, streamsTaken
else:
    # keep updating finalStream with the stream used before it until 'None'
    while finalStream != None:
        streamsTaken.append(allStreams[finalStream])
        startOfFinalStream = allStreams[finalStream][0] # find start of stream
        finalStream = energyForDist[startOfFinalStream][1] 
            
    print minEnergyConsumption
    print [(x, y) for x, y, z in sorted(streamsTaken)]