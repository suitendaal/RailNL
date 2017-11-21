import helpers

def algoritm1(paths, critical_connections):
    """Algoritm to get best n paths, then use depth first search to calculate best trajects"""

    # Use the scorefunction to get the best n trajects.
    n = 20
    bestNpaths, bestNscores = helpers.ScorePaths(paths, critical_connections, n)

    # With the bestNpaths, calculate via depth-first search the best traject with the best score.
    bestScore = 0
    bestTraject = []
    for i in range(1, 7):
        newBestScore, newBestTraject = helpers.getBestScore(bestNpaths, critical_connections, i)
        if newBestScore > bestScore:
            bestScore = newBestScore
            bestTraject = newBestTraject
    print("bestScore: ", bestScore)
    print("lengte: ", len(bestTraject))



# def algoritm3Functions(paths, critical_connections, start, end):
#     for path in paths:
#         if path[0][0] == start and path[0][-1] == end:



# def algoritm3(paths, critical_connections, stationnames):
#     best_paths = []
#     for i in range(len(stationnames)):
#         for j in range(i + 1, len(stationnames)):
#             best_paths.extend(algoritm3Function(paths, critical_connections, stationnames[i], stationnames[j]))
#     return best_paths

def Dijkstra(graph, station):
    critical = []
    non_critical = []
    for destination in range(0, len(station)):
        if [station[destination][0], station] in critical_connections or [station, station[destination][0]] in critical_connections:
          critical.append(station[destination])
        else:
            non_critical.append(station[destination])

        shortest = 0
        shortest_route = ''
        if len(critical) != 0:
            for i in range(0, len(critical)):
                if critical[i][1] < shortest:
                    shortest = critical[i][1]
                    shortest_route = critical[i][0]

        else:
            for i in range(0, len(non_critical)):
                if non_critical[i][1] < shortest:
                    shortest = non_critical[i][1]
                    shortest_route = non_critical[i][0]
        Dijkstra(graph, shortest_route, critical_connections)