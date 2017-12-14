def algoritmDijkstraFunction(graph, start, end):
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



def algoritmDijkstra(graph):
    """Also known as Sven's algoritm"""
    bestPaths = []
    for i in range(len(graph.allStations)):
        for j in range(i + 1, len(graph.stationNames)):
            newPath = algoritmDijkstraFunction(graph, graph.stationNames[i], graph.stationNames[j])
            if newPath != []:
                bestPaths.append(newPath)

    return bestPaths
