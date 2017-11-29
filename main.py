from Classes.graphClass import Graph
from PythonFunctions.algoritm import algoritm1, algoritm3, Dijkstra
import csv
from PythonFunctions.helpers import CalculateScore, ScorePaths, getBestScore
from PythonFunctions.hillclimber import HillClimber


def main():

    # Files with stations and connections.
    stationsCsvFile = 'C:/Users/svenu/RailNL/csvFiles/StationsHolland.csv'
    connectiesCsvFile = 'C:/Users/svenu/RailNL/csvFiles/ConnectiesHolland.csv'

    # Load the stations and connections in a graph.
    graph = Graph()
    graph.load_data(stationsCsvFile, connectiesCsvFile)
    graph.makeAllRoutes()

    trajecten = []
    for station in graph.allStations:
        print(station.name)
        newRoute, newTime = Dijkstra(graph, station.name, [])
        trajecten.append([newRoute, newTime])
    for traject in trajecten:
        print("begin", traject[0][0])
        print(traject)
    # bestPaths = algoritm3(graph)
    # pathsSelected = bestPaths[0:7]
    #
    # bestScore = CalculateScore(pathsSelected, graph.criticalConnections)
    # for i in range(100):
    #     pathsSelected, bestScore = HillClimber(graph, pathsSelected, bestPaths, bestScore)
    # print("paths: ", pathsSelected)
    # print("bestScore: ", bestScore)

    # bestPaths, bestScores = ScorePaths(graph.allRoutes, graph.criticalConnections, 100)
    #
    # for i in range(7):
    #     sc, tr = getBestScore(bestPaths, graph.criticalConnections, i)
    #     print("beste: ", sc)


    # print("paths: ", pathsSelected)
    # print("bestScore: ", bestScore)

    # pathsSelected = graph.allRoutes[0:7]
    # bestScore = CalculateScore(pathsSelected, graph.criticalConnections)
    # for i in range(100):
    #     pathsSelected, bestScore = HillClimber(graph.allRoutes, pathsSelected, graph.criticalConnections, bestScore)

    # print("paths: ", pathsSelected)
    # print("bestScore: ", bestScore)

    # print(len(new_graph.criticalConnections))

    # algoritm.algoritm3(paths, critical_connections, stationnames)

    # routes = []
    # for stationname in stationnames:
    # route, time = algoritm.Dijkstra(graph, stationnames[4], critical_connections)
    # print([route, time])
        # routes.append([route, time])
    # print(routes)




if __name__ == "__main__":
    main()
