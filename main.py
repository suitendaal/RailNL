from Classes.graphClass import Graph
from PythonFunctions.algoritm import algoritm1, algoritm3, Dijkstra
import csv
from PythonFunctions.helpers import CalculateScore, ScorePaths, getBestScore
from PythonFunctions.hillclimber import HillClimber
import os
from PythonFunctions.simulatedAnnealing import SimulatedAnnealing
from Klad.draw_traject import drawTraject


def main():

    # Files with stations and connections.
    stationsCsvFile = os.path.join('csvFiles', "StationsHolland.csv")
    connectiesCsvFile = os.path.join('csvFiles', "ConnectiesHolland.csv")

    # Load the stations and connections in a graph.
    graph = Graph()
    graph.load_data(stationsCsvFile, connectiesCsvFile)
    graph.makeAllRoutes(120)

    print("For depth first algorithm, type: 1")
    print("For Dijkstra's algorithm, type: 2")
    print("For the Hillclimber, type: 3")
    print("For Simmulated Annealing, type: 4")

    algorithm = input("Select: ")


    ##Depth first
    if (int(algorithm) == 1):

        print("For Svens algoritm, type: 1")
        print("For bestScore algoritm, type: 2")

        algoritmBestPaths = input("Select: ")

        #Sven
        if (int(algoritmBestPaths) == 1):
            bestPaths = algoritm3(graph)
            print(bestPaths[1])

        #BestScore
        elif (int(algoritmBestPaths) == 2):
            bestPaths, bestScores = ScorePaths(graph, 20)

        #Errormelding
        else:
            while (int(algoritmBestPaths) != 1 or int(algoritmBestPaths) != 2):
                algorithm = input("Please select valid algorithm: ")

        #Run algorithm
        for i in range(7):
            sc, tr = getBestScore(bestPaths, graph.criticalConnections, i)
            print("beste: ", sc)

    #Dijkstra
    elif (int(algorithm) == 2):

        #Run algorithm
        trajecten = []
        for station in graph.allStations:
            print(station.name)
            newRoute, newTime = Dijkstra(graph, station.name, [])
            #als we geen lege lijst meegeven, doet ie t niet.
            trajecten.append([newRoute, newTime])
        for traject in trajecten:
            print("begin", traject[0][0])
            print(traject)

    #Hillclimber
    elif (int(algorithm) == 3):
        print("For Svens algoritm, type: 1")
        print("For bestScore algoritm, type: 2")

        algoritmBestPaths = input("Select: ")

        #Sven
        if (int(algoritmBestPaths) == 1):
            bestPaths = algoritm3(graph)
            pathsSelected = bestPaths[0:7]

        #Bestscore
        elif (int(algoritmBestPaths) == 2):
            bestPaths, bestScores = ScorePaths(graph, 25)
            pathsSelected = bestPaths[0:7]

        #Errormelding
        else:
            while (int(algoritmBestPaths) != 1 or int(algoritmBestPaths) != 2):
                algorithm = input("Please select valid algorithm: ")

        #Run algorithm
        bestScore = CalculateScore(pathsSelected, graph.criticalConnections)
        for i in range(200):
            pathsSelected, bestScore = HillClimber(graph, pathsSelected, bestPaths, bestScore)
        print("paths: ", pathsSelected)
        print("bestScore: ", bestScore)
        drawTraject(graph, pathsSelected)

    #Sim Ann
    elif (int(algorithm) == 4):

        print("For Svens algoritm, type: 1")
        print("For bestScore algoritm, type: 2")

        algoritmBestPaths = input("Select: ")

        #Sven
        if (int(algoritmBestPaths) == 1):
            bestPaths = algoritm3(graph)
            pathsSelected = bestPaths[0:7]

        #Bestscore
        elif (int(algoritmBestPaths) == 2):
            bestPaths, bestScores = ScorePaths(graph, 25)
            pathsSelected = bestPaths[0:7]

        #Errormelding
        else:
            while (int(algoritmBestPaths) != 1 or int(algoritmBestPaths) != 2):
                algorithm = input("Please select valid algorithm: ")

        #Run algorithm
        bestScore = CalculateScore(pathsSelected, graph.criticalConnections)
        for i in range(2000):
            pathsSelected, bestScore = SimulatedAnnealing(graph, pathsSelected, bestPaths, bestScore)
        print("paths: ", pathsSelected)
        print("bestScore: ", bestScore)

    # elif (int(algorith m) == 4):
    #     graph.draw()

    #Errormelding
    else:
        while (int(algorithm) != 1 or int(algorithm) != 2 or int(algorithm) != 3 or int(algorithm) != 4):
             algorithm = input("Please select valid algorithm: ")




if __name__ == "__main__":
    main()
