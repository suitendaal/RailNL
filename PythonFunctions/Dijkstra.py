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

def Dijkstra(graph, station, route = [], time = 0):
    critical = []
    nonCritical = []

    route.append(station)

    if time == 120:
        return route, time

    destinations = graph.graph[station]
    for destination in destinations:
        if destination[0] not in route:
            if [destination[0], station] in graph.criticalConnections or [station, destination[0]] in graph.criticalConnections:
                critical.append(destination)
            else:
                nonCritical.append(destination)

    shortestTime = 120
    shortestConnection = ''
    if len(critical) != 0:
        for traject in critical:
            if traject not in route:
                if int(traject[1]) < shortestTime:
                    shortestTime = int(traject[1])
                    if time + shortestTime <= 120:
                        shortestConnection = traject[0]
        if shortestConnection != '':
            return Dijkstra(graph, shortestConnection, route, time + shortestTime)

    if len(nonCritical) != 0:
        for traject in nonCritical:
            if traject not in route:
                if int(traject[1]) < shortestTime:
                    shortestTime = int(traject[1])
                    if time + shortestTime <= 120:
                        shortestConnection = traject[0]
        if shortestConnection != '':
            return Dijkstra(graph, shortestConnection, route, time + shortestTime)

    return route, time
