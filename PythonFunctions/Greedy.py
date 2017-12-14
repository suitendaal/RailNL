import copy

def Greedy(graph, station, maxTime, allConnections, route=[], time=0):
    critical = []
    nonCritical = []

    route.append(station)

    if time == maxTime:
        return route, time

    destinations = graph.graph[station]
    for destination in destinations:
        goOn = True
        for connection in allConnections:
            if ([station, destination] or [destination, station]) == connection[0]:
                goOn = False
                break
        if goOn:
            if destination[0] not in route:
                if [destination[0], station] in graph.criticalConnections or [station, destination[0]] in graph.criticalConnections:
                    critical.append(destination)
                else:
                    nonCritical.append(destination)

    shortestTime = None
    shortestConnection = None
    if len(critical) != 0:
        for traject in critical:
            if traject not in route:
                if shortestTime == None or int(traject[1]) < shortestTime:
                    shortestTime = int(traject[1])
                    if time + shortestTime <= maxTime:
                        shortestConnection = traject[0]
        if shortestConnection != None:
            return Greedy(graph, shortestConnection, maxTime, allConnections, route, time + shortestTime)

    if len(nonCritical) != 0:
        for traject in nonCritical:
            if traject not in route:
                if shortestTime == None or int(traject[1]) < shortestTime:
                    shortestTime = int(traject[1])
                    if time + shortestTime <= maxTime:
                        shortestConnection = traject[0]
        if shortestConnection != None:
            return Greedy(graph, shortestConnection, maxTime, allConnections, route, time + shortestTime)

    return route, time

def bestBeginStation(allConnections, allStations):
    criticalDestinations = None
    nonCriticalDestinations = None
    bestBeginStation = None

    for station in allStations:
        myCriticalDestinations = []
        myNonCriticalDestinations = []
        for destination in allStations[station].destinations:
            for connection in allConnections:
                if [station, destination.name] == connection[0] or [destination.name, station] == connection[0]:
                    if allStations[station].isCritical or destination.isCritical:
                        myCriticalDestinations.append(connection)
                    else:
                        myNonCriticalDestinations.append(connection)
                    break
        if bestBeginStation == None:
            bestBeginStation = station
            criticalDestinations = myCriticalDestinations
            nonCriticalDestinations = myNonCriticalDestinations
        elif len(myCriticalDestinations) % 2 == 1:
            if len(criticalDestinations) % 2 == 1:
                if len(myCriticalDestinations) < len(criticalDestinations):
                    bestBeginStation = station
                    criticalDestinations = myCriticalDestinations
                    nonCriticalDestinations = myNonCriticalDestinations
                elif len(myCriticalDestinations) == len(criticalDestinations):
                    minimumTime = None
                    for connection in criticalDestinations:
                        if minimumTime == None or connection[1] < minimumTime:
                            minimumTime = connection[1]
                    myMinimumTime = None
                    for connection in myCriticalDestinations:
                        if myMinimumTime == None or connection[1] < myMinimumTime:
                            myMinimumTime = connection[1]
                    if myMinimumTime < minimumTime:
                        bestBeginStation = station
                        criticalDestinations = myCriticalDestinations
                        nonCriticalDestinations = myNonCriticalDestinations
            else:
                bestBeginStation = station
                criticalDestinations = myCriticalDestinations
                nonCriticalDestinations = myNonCriticalDestinations
        elif len(criticalDestinations) % 2 == 0:
            if len(myCriticalDestinations) < len(criticalDestinations):
                bestBeginStation = station
                criticalDestinations = myCriticalDestinations
                nonCriticalDestinations = myNonCriticalDestinations
            elif len(myCriticalDestinations) == len(criticalDestinations):
                minimumTime = None
                for connection in criticalDestinations:
                    if minimumTime == None or connection[1] < minimumTime:
                        minimumTime = connection[1]
                myMinimumTime = None
                for connection in myCriticalDestinations:
                    if myMinimumTime == None or connection[1] < myMinimumTime:
                        myMinimumTime = connection[1]
                if myMinimumTime != None and myMinimumTime < minimumTime:
                    bestBeginStation = station
                    criticalDestinations = myCriticalDestinations
                    nonCriticalDestinations = myNonCriticalDestinations

    return bestBeginStation


def algorithmGreedy(graph, maxDepth, maxTime):
    allConnections = copy.copy(graph.allConnections)
    allStations = copy.copy(graph.allStations)

    pathsSelected = []
    for i in range(maxDepth):
        beginStation = bestBeginStation(allConnections, allStations)
        # Je moet een lege lijst meegeven anders doet hij het niet.
        route, time = Greedy(graph, beginStation, maxTime, allConnections, [])
        connectionsToRemove = []
        for i in range(len(route) - 1):
            for connection in allConnections:
                if [route[i], route[i+1]] == connection[0] or [route[i+1], route[i]] == connection[0]:
                    connectionsToRemove.append(connection)
        for connection in connectionsToRemove:
            allConnections.remove(connection)
        pathsSelected.append([route, time])

    return pathsSelected
