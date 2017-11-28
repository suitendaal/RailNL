from PythonFunctions.helpers import CalculateScore, ScorePaths, getBestScore

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

            criticalPercentage = 100 * criticalPathCounter / path[1]
            newScore = criticalPercentage / path[1]
            if newScore > score:
                score = newScore
                bestPath = path
    return bestPath



def algoritm3(graph):
    bestPaths = []
    for i in range(len(graph.allStations)):
        for j in range(i + 1, len(graph.allStations)):
            best_paths.append(algoritm3Function(graph, graph.allStations[i], graph.allStations[j]))

    print("lendte: ", len(bestPaths))

    bestScore = 0
    bestTraject = []
    for i in range(1, 4):
        newBestScore, newBestTraject = getBestScore(bestPaths, graph.criticalConnections, i)
        if newBestScore > bestScore:
            bestScore = newBestScore
            bestTraject = newBestTraject
    print("bestScore: ", bestScore)
    print("lengte: ", bestTraject)



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
            if int(traject[1]) < shortestTime:
                shortestTime = int(critical[i][1])
                if time + shortestTime <= 120
                    shortestConnection = critical[i][0]
                    print(traject[0])
        if shortestConnection =! '':
            return Dijkstra(graph, shortestConnection, route, time + shortestTime)

    if len(nonCritical) != 0:
        for traject in nonCritical:
            if int(traject[1]) < shortestTime:
                shortestTime = int(critical[i][1])
                if time + shortestTime <= 120
                    shortestConnection = critical[i][0]
                    print(traject[0])
        if shortestConnection =! '':
            return Dijkstra(graph, shortestConnection, route, time + shortestTime)

    return route, time
