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

    pathsSelected = graph.allRoutes[0:7]
    paths, bestScore = HillClimber(graph.allRoutes, pathsSelected, graph.criticalConnections)

    print("paths: ", paths)
    print("bestScore: ", bestScore)

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
