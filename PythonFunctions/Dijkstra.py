# def BestBeginStationsDijkstra(graph, amountOfStations, criticalConnectionsToChoose=[], bestBeginTrajectories=[]):
#     if amountOfStations == 0:
#         return bestBeginTrajectories
#
#     if criticalConnectionsToChoose == []:
#         criticalConnectionsToChoose = copy.copy(graph.criticalConnections)
#
#     bestCriticalConnections = None
#     bestCriticalDestinations = None
#     bestBeginStation = None
#
#     for station in graph.allStations:
#         criticalConnections = 0
#         criticalDestinations = []
#         for destination in station.destinations:
#             if ([station.name, destination] or [destination, station.name]) in criticalConnectionsToChoose:
#                 criticalConnections += 1
#                 criticalDestinations.append(destination)
#
#         if bestCriticalConnections == None:
#             bestCriticalConnections = criticalConnections
#             bestCriticalDestinations = criticalDestinations
#             bestBeginStation = station
#
#         elif criticalConnections % 2 == 1:
#             if bestCriticalConnections % 2 == 1:
#                 if criticalConnections < bestCriticalConnections:
#                     bestCriticalConnections = criticalConnections
#                     bestCriticalDestinations = criticalDestinations
#                     bestBeginStation = station
#             else:
#                 bestCriticalConnections = criticalConnections
#                 bestCriticalDestinations = criticalDestinations
#                 bestBeginStation = station
#
#         else:
#             if bestCriticalConnections % 2 == 0 and criticalConnections < bestCriticalConnections:
#                 bestCriticalConnections = criticalConnections
#                 bestCriticalDestinations = criticalDestinations
#                 bestBeginStation = station
#
#     bestBeginTrajectory = [bestBeginStation, random.choice(bestCriticalDestinations)]
#     criticalConnectionsToChoose.remove(bestBeginTrajectory)
#     bestBeginTrajectories.append(bestBeginTrajectory)
#
#     return BestBeginStationsDijkstra(graph, amountOfStations-1, criticalConnectionsToChoose, bestBeginTrajectories)

def Britt(graph, station, maxTime, allConnections, route=[], time=0):
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
                if int(traject[1]) < shortestTime:
                    shortestTime = int(traject[1])
                    if time + shortestTime <= maxTime:
                        shortestConnection = traject[0]
        if shortestConnection != None:
            return Britt(graph, shortestConnection, allConnections, route, time + shortestTime)

    if len(nonCritical) != 0:
        for traject in nonCritical:
            if traject not in route:
                if int(traject[1]) < shortestTime:
                    shortestTime = int(traject[1])
                    if time + shortestTime <= maxTime:
                        shortestConnection = traject[0]
        if shortestConnection != None:
            return Britt(graph, shortestConnection, allConnections, route, time + shortestTime)

    return route, time

def bestBeginStation(allConnections, allStations):
    criticalDestinations = None
    nonCriticalDestinations = None
    bestBeginStation = None

    for station in allStations:
        myCriticalDestinations = []
        myNonCriticalDestinations = []
        for destination in station.destinations:
            for connection in allConnections:
                if ([station.name, destination.name] or [destination.name, station.name]) in connection[0]:
                    if station.isCritical or destination.isCritical:
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
                    if myMimimumTime < minimumTime:
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
                if myMimimumTime < minimumTime:
                    bestBeginStation = station
                    criticalDestinations = myCriticalDestinations
                    nonCriticalDestinations = myNonCriticalDestinations

    return bestBeginStation.name


def algorithmBritt(graph, maxDepth, maxTime):
    allConnections = copy.copy(graph.allConnections)
    allStations = copy.copy(graph.allStations)

    pathsSelected = []
    for i in range(maxDepth):
        beginStation = bestBeginStation(allConnections, allStations)
        # Je moet een lege lijst meegeven anders doet hij het niet.
        route, time = Britt(graph, beginStation, maxTime, allConnections, [])
        connectionsToRemove = []
        for i in range(len(route) - 1):
            for connection in allConnections:
                if ([route[i],  route[i+1]] or [route[i+1],  route[i]]) == connection[0]:
                    connectionsToRemove.append(connection)
        for connection in connectionsToRemove:
            allConnections.remove(connection)
        pathsSelected.append[route, time]

    return pathsSelected
