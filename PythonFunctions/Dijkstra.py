def BestBeginStationsDijkstra(graph, amountOfStations, criticalConnectionsToChoose=[], bestBeginTrajectories=[]):
    if amountOfStations == 0:
        return bestBeginTrajectories

    if criticalConnectionsToChoose == []:
        criticalConnectionsToChoose = copy.copy(graph.criticalConnections)

    bestCriticalConnections = None
    bestCriticalDestinations = None
    bestBeginStation = None

    for station in graph.allStations:
        criticalConnections = 0
        criticalDestinations = []
        for destination in station.destinations:
            if ([station.name, destination] or [destination, station.name]) in criticalConnectionsToChoose:
                criticalConnections += 1
                criticalDestinations.append(destination)

        if bestCriticalConnections == None:
            bestCriticalConnections = criticalConnections
            bestCriticalDestinations = criticalDestinations
            bestBeginStation = station

        elif criticalConnections % 2 == 1:
            if bestCriticalConnections % 2 == 1:
                if criticalConnections < bestCriticalConnections:
                    bestCriticalConnections = criticalConnections
                    bestCriticalDestinations = criticalDestinations
                    bestBeginStation = station
            else:
                bestCriticalConnections = criticalConnections
                bestCriticalDestinations = criticalDestinations
                bestBeginStation = station

        else:
            if bestCriticalConnections % 2 == 0 and criticalConnections < bestCriticalConnections:
                bestCriticalConnections = criticalConnections
                bestCriticalDestinations = criticalDestinations
                bestBeginStation = station

    bestBeginTrajectory = [bestBeginStation, random.choice(bestCriticalDestinations)]
    criticalConnectionsToChoose.remove(bestBeginTrajectory)
    bestBeginTrajectories.append(bestBeginTrajectory)

    return BestBeginStationsDijkstra(graph, amountOfStations-1, criticalConnectionsToChoose, bestBeginTrajectories)
