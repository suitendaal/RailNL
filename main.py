from Classes.graphClass import Graph
from PythonFunctions.algoritm import algoritm1, algoritm3, Dijkstra
import csv
from PythonFunctions.helpers import CalculateScore, ScorePaths, getBestScore
from PythonFunctions.hillclimber import HillClimber
import os
import sys
from PythonFunctions.simulatedAnnealing import SimulatedAnnealing
from PlotFunctions.draw_traject import drawTraject
from PlotFunctions.make_graph import makeGraph


def main():

    # Ask user which stations to run.
    print("For North - and South - Holland, type: H")
    print("For the entire Netherlands, type: N")
    stations = input("Select:")

    if stations == "H" or stations == "h":
        stationsCsvFile = os.path.join('csvFiles', "StationsHolland.csv")
        connectiesCsvFile = os.path.join('csvFiles', "ConnectiesHolland.csv")
        maxDepth = 7
        maxDuration = 120
    elif stations == "N" or stations == "n":
        stationsCsvFile = os.path.join('csvFiles', "StationsNationaal.csv")
        connectiesCsvFile = os.path.join('csvFiles', "ConnectiesNationaal.csv")
        maxDepth = 22
        maxDuration = 180
    else:
        sys.exit("Not a valid input")
    # Files with stations and connections.


    critical = input("Make all stations critical: y/n? ")
    # Load the stations and connections in a graph.
    graph = Graph()
    if critical == "y" or critical == "Y" or critical == "yes":
        graph.load_data(stationsCsvFile, connectiesCsvFile, True)
    elif critical == "n" or critical == "N" or critical == "no":
        graph.load_data(stationsCsvFile, connectiesCsvFile)
    else:
        sys.exit("Not a valid input")
    graph.makeAllRoutes(maxDuration)

    print("For depth first algorithm, type: 1")
    print("For Dijkstra's algorithm, type: 2")
    print("For the Hillclimber, type: 3")
    print("For Simulated Annealing, type: 4")

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
            bestPaths, bestScores = ScorePaths(graph, maxDepth)

        #Errormelding
        else:
            while (int(algoritmBestPaths) != 1 or int(algoritmBestPaths) != 2):
                algorithm = input("Please select valid algorithm: ")

        #Run algorithm
        for i in range(maxDepth):
            if (int(algoritmBestPaths) == 1):
                sc, tr = getBestScore(1, bestPaths, graph.criticalConnections, i)
            else:
                sc, tr = getBestScore(2, bestPaths, graph.criticalConnections, i)
            print("beste score: ", sc)
            print("beste trajecten: ", tr)
        drawTraject(graph, tr)

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
        drawTraject(graph, trajecten)

    #Hillclimber
    elif (int(algorithm) == 3):
        print("For Svens algoritm, type: 1")
        print("For bestScore algoritm, type: 2")

        algoritmBestPaths = input("Select: ")

        #Sven
        if (int(algoritmBestPaths) == 1):
            bestPaths = algoritm3(graph)
            pathsSelected = bestPaths[0:maxDepth]

        #Bestscore
        elif (int(algoritmBestPaths) == 2):
            bestPaths, bestScores = ScorePaths(graph, maxDepth)
            pathsSelected = bestPaths[0:maxDepth]

        #Errormelding
        else:
            sys.exit("Not a valid algorithm")

        #Run algorithm
        bestScore = CalculateScore(pathsSelected, graph.criticalConnections)
        for i in range(400):
            pathsSelected, bestScore = HillClimber(graph, pathsSelected, bestPaths, bestScore)
        print("paths: ", pathsSelected)
        print("bestScore: ", bestScore)
        drawTraject(graph, pathsSelected)
        makeGraph("HillClimberScore.csv", "hillclimber_plot.png")

    #Sim Ann
    elif (int(algorithm) == 4):

        print("For Svens algoritm, type: 1")
        print("For bestScore algoritm, type: 2")

        algoritmBestPaths = input("Select: ")

        #Sven
        if (int(algoritmBestPaths) == 1):
            bestPaths = algoritm3(graph)
            pathsSelected = bestPaths[0:maxDepth]

        #Bestscore
        elif (int(algoritmBestPaths) == 2):
            bestPaths, bestScores = ScorePaths(graph, maxDepth)
            pathsSelected = bestPaths[0:maxDepth]

        #Errormelding
        else:
            sys.exit("Not a valid algorithm")

        #Run algorithm
        bestScore = CalculateScore(pathsSelected, graph.criticalConnections)
        for i in range(50):
            pathsSelected, bestScore = SimulatedAnnealing(graph, pathsSelected, [], bestScore)
        drawTraject(graph, pathsSelected)
        print("paths: ", pathsSelected)
        print("bestScore: ", bestScore)
        makeGraph("AnnealingScore.csv", "annealing_plot.png")

    # elif (int(algorith m) == 4):
    #     graph.draw()

    #Errormelding
    else:
        sys.exit("Not a valid algorithm")


if __name__ == "__main__":
    main()
