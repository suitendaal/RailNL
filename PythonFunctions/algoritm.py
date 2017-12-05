from PythonFunctions.helpers import CalculateScore, ScorePaths, getBestScore
import copy

def algoritm1(graph):
    """Algoritm to get best n paths, then use depth first search to calculate best trajectories"""

    # Use the scorefunction to get the best n trajects.
    n = 20
    bestNpaths, bestNscores = ScorePaths(graph, n)

    # With the bestNpaths, calculate via depth-first search the best traject with the best score.
    bestScore = 0
    bestTraject = []
    for i in range(1, 8):
        newBestScore, newBestTraject = getBestScore(bestNpaths, graph.criticalConnections, i)
        if newBestScore > bestScore:
            bestScore = newBestScore
            bestTraject = newBestTraject
    print("bestScore: ", bestScore)
    print("lengte: ", bestTraject)



def algoritm3Function(graph, start, end):
    """Algoritm to """
    bestPath = []
    score = 0
    for path in graph.allRoutes:

        if path[0][0] == start and path[0][-1] == end:
            criticalPathCounter = 0
            for i in range(len(path[0]) - 1):
                if [path[0][i], path[0][i+1]] in graph.criticalConnections:
                    criticalPathCounter += 1

            criticalPercentage = 100 * criticalPathCounter / len(path[0])
            newScore = criticalPercentage
            if newScore > score:
                score = newScore
                bestPath = path
    return bestPath



def algoritm3(graph):
    """Also known as Sven's algoritm"""
    bestPaths = []
    for i in range(len(graph.allStations)):
        for j in range(i + 1, len(graph.stationNames)):
            newPath = algoritm3Function(graph, graph.stationNames[i], graph.stationNames[j])
            if newPath != []:
                bestPaths.append(newPath)

    return bestPaths


def BestBeginStationsDijkstra(graph, numberOfTrajectories):
    criticalConnectionsNotBeenYet = copy.copy(graph.criticalConnections)
    numberOfCriticalDestinations = 0

    for station in graph.allStations:
        new_numberOfCriticalDestinations = 0
        for connection in criticalConnectionsNotBeenYet:
            if station.name == connection[0] or station.name == connection[1]:
                new_number += 1

        if (new_number < number or number == 0) and new_number != 0:
            number = new_number
            beginstation = station

        if number of criticalConnections not been yet = 1:
            Take as begin
            stop for loop
        elif number of criticalConnections not been yet > 1:
            Take the shortest as begin
            stop for loopp


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
