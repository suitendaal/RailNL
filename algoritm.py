import helpers

def algoritm1(paths, critical_connections):
    """Algoritm to get best n paths, then use depth first search to calculate best trajects"""

    # Use the scorefunction to get the best n trajects.
    n = 20
    bestNpaths, bestNscores = helpers.ScorePaths(paths, critical_connections, n)

    # With the bestNpaths, calculate via depth-first search the best traject with the best score.
    bestScore = 0
    bestTraject = []
    for i in range(1, 8):
        newBestScore, newBestTraject = helpers.getBestScore(bestNpaths, critical_connections, i)
        if newBestScore > bestScore:
            bestScore = newBestScore
            bestTraject = newBestTraject
    print("bestScore: ", bestScore)
    print("lengte: ", bestTraject)



def algoritm3Function(paths, critical_connections, start, end):
    bestPath = []
    score = 0
    for path in paths:

        if path[0][0] == start and path[0][-1] == end:
            criticalPathCounter = 0
            for i in range(len(path[0]) - 1):
                if [path[0][i], path[0][i+1]] in critical_connections:
                    criticalPathCounter += 1

            criticalPercentage = 100 * criticalPathCounter / len(path[0])
            newScore = criticalPercentage / path[1]
            if newScore > score:
                score = newScore
                bestPath = path
    return bestPath



def algoritm3(paths, critical_connections, stationnames):
    best_paths = []
    for i in range(len(stationnames)):
        for j in range(i + 1, len(stationnames)):
            best_paths.append(algoritm3Function(paths, critical_connections, stationnames[i], stationnames[j]))

    print("lendte: ", len(best_paths))

    bestScore = 0
    bestTraject = []
    for i in range(1, 4):
        newBestScore, newBestTraject = helpers.getBestScore(best_paths, critical_connections, i)
        if newBestScore > bestScore:
            bestScore = newBestScore
            bestTraject = newBestTraject
    print("bestScore: ", bestScore)
    print("lengte: ", bestTraject)




def Dijkstra(graph, station, critical_connections, route = [], time = 0):
    critical = []
    non_critical = []

    route.append(station)

    if time >= 120:
        return route, time

    else:
        destinations = graph[station]
        for destination in destinations:
            if destination[0] not in route:
                if [destination[0], station] in critical_connections or [station, destination[0]] in critical_connections:
                    critical.append(destination)
                else:
                    non_critical.append(destination)

        shortest_time = 120
        shortest_connection = ''
        if len(critical) != 0:
            for i in range(len(critical)):
                if int(critical[i][1]) < shortest_time:
                    shortest_time = int(critical[i][1])
                    shortest_connection = critical[i][0]
                    print(critical[i][0])

        else:
            for i in range(len(non_critical)):
                if int(non_critical[i][1]) < shortest_time:
                    shortest_time = int(non_critical[i][1])
                    shortest_connection += non_critical[i][0]

        time += shortest_time
        return Dijkstra(graph, shortest_connection, critical_connections, route, time)
