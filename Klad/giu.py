print("For depth first algorithm, type: 1")
print("For Dijkstra's algorithm, type: 2")
print("For Sven's algorithm, type: 3")
print("For the Hillclimber, type: 4")

algorithm = input("Select: ")



if (int(algorithm) == 1):
	bestPaths, bestScores = ScorePaths(graph.allRoutes, graph.criticalConnections, 20)
	for i in range(7):
        sc, tr = getBestScore(bestPaths, graph.criticalConnections, i)
        print("beste: ", sc)

elif (int(algorithm) == 2):

elif (int(algorithm) == 3):

elif (int(algorithm) == 4):
    bestPaths = algoritm3(graph)
    pathsSelected = bestPaths[0:7]

    bestScore = CalculateScore(pathsSelected, graph.criticalConnections)
    for i in range(100):
        pathsSelected, bestScore = HillClimber(graph, pathsSelected, bestPaths, bestScore)
    print("paths: ", pathsSelected)
    print("bestScore: ", bestScore)
else:
    while (int(algorithm) != 1 or int(algorithm) != 2 or int(algorithm) != 3 or int(algorithm) != 4):
         algorithm = input("Please select valid algorithm: ")
