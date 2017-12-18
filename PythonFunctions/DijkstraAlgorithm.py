def algorithmDijkstraFunction(graph, start, end):
    """algorithm get the best route between two stations"""

    bestPath = None
    score = 0
    for path in graph.allRoutes:

        # If the path has the given begin- and endstation, calculate the score.
        if (path[0][0] == start and path[0][-1] == end) or (path[0][-1] == start and path[0][0] == end):

            # Calculate amount of critical connections.
            criticalPathCounter = 0
            for i in range(len(path[0]) - 1):
                if [path[0][i], path[0][i+1]] in graph.criticalConnections:
                    criticalPathCounter += 1

            # Calculate the critical percentage.
            newScore = 100 * criticalPathCounter / len(path[0])
            if newScore > score:
                score = newScore
                bestPath = path
    return bestPath



def algorithmDijkstra(graph):
    """Also known as Sven's algorithm, returns the best paths for between every station"""
    bestPaths = []
    for i in range(len(graph.allStations)):
        for j in range(i + 1, len(graph.stationNames)):

            # Calculate the best path between every begin- and endstation.
            newPath = algorithmDijkstraFunction(graph, graph.stationNames[i], graph.stationNames[j])

            # Append the route to the list.
            if newPath != None:
                bestPaths.append(newPath)

    return bestPaths
