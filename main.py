from Classes.graphClass import Graph
from PythonFunctions.algoritm import algoritm1, algoritm3, Dijkstra
import csv
from PythonFunctions.helpers import CalculateScore, ScorePaths, getBestScore
from PythonFunctions.hillclimber import HillClimber


def main():

    # Files with stations and connections.
    stationsCsvFile = 'C:/Users/britt/RailNL/csvFiles/StationsHolland.csv'
    connectiesCsvFile = 'C:/Users/britt/RailNL/csvFiles/ConnectiesHolland.csv'

    # Load the stations and connections in a graph.
    graph = Graph()
    graph.load_data(stationsCsvFile, connectiesCsvFile)
    graph.makeAllRoutes()

    print("For depth first algorithm, type: 1")
    print("For Dijkstra's algorithm, type: 2")
    print("For the Hillclimber, type: 3")

    algorithm = input("Select: ")



    if (int(algorithm) == 1):

        print("For Svens algoritm, type: 1")
        print("For bestScore algoritm, type: 2")

        algoritmBestPaths = input("Select: ")

        if (int(algoritmBestPaths) == 1):
            bestPaths = algoritm3(graph)
        
        elif (int(algoritmBestPaths) == 2):
            bestPaths, bestScores = ScorePaths(graph, 20)

        else:
            while (int(algoritmBestPaths) != 1 or int(algoritmBestPaths) != 2):
                algorithm = input("Please select valid algorithm: ")
        
        for i in range(7):
            sc, tr = getBestScore(bestPaths, graph.criticalConnections, i)
            print("beste: ", sc)

    elif (int(algorithm) == 2):

        trajecten = []
        for station in graph.allStations:
            print(station.name)
            newRoute, newTime = Dijkstra(graph, station.name, [])
            trajecten.append([newRoute, newTime])
        for traject in trajecten:
            print("begin", traject[0][0])
            print(traject)
        

    elif (int(algorithm) == 3):
        print("For Svens algoritm, type: 1")
        print("For bestScore algoritm, type: 2")

        algoritmBestPaths = input("Select: ")

        if (int(algoritmBestPaths) == 1):
            bestPaths = algoritm3(graph)
            pathsSelected = bestPaths[0:7]
        
        elif (int(algoritmBestPaths) == 2):
            bestPaths, bestScores = ScorePaths(graph, 20)
            pathsSelected = bestPaths[0:7]

        else:
            while (int(algoritmBestPaths) != 1 or int(algoritmBestPaths) != 2):
                algorithm = input("Please select valid algorithm: ")

        bestScore = CalculateScore(pathsSelected, graph.criticalConnections)
        for i in range(100):
            pathsSelected, bestScore = HillClimber(graph, pathsSelected, bestPaths, bestScore)
        print("paths: ", pathsSelected)
        print("bestScore: ", bestScore)
    else:
        while (int(algorithm) != 1 or int(algorithm) != 2 or int(algorithm) != 3):
             algorithm = input("Please select valid algorithm: ")




if __name__ == "__main__":
    main()
