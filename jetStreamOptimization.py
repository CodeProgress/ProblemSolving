# Jet stream optimization

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