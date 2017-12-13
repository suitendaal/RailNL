import os
import sys
import csv
import random

from Classes.graphClass import Graph

from PythonFunctions.Dijkstra import Dijkstra
from PythonFunctions.SvensAlgorithm import algoritm3
from PythonFunctions.helpers import CalculateScore
from PythonFunctions.depthFirst import depthFirst
from PythonFunctions.hillClimber import HillClimber
from PythonFunctions.simulatedAnnealing import SimulatedAnnealing

from PlotFunctions.draw_traject import drawTraject
from PlotFunctions.make_graph import makeGraph


def main():

    # Initialize graph.
    graph = Graph()

    # Ask user which stations to run.
    print("For North - and South - Holland, type: H")
    print("For the entire Netherlands, type: N")
    stations = input("Select:")

    # Open the correct file with stations and connections.
    print("Loading data...")
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

    critical = input("Make all stations critical: y/n? ")

    # Load the stations and connections in a graph.
    if critical == "y" or critical == "Y" or critical == "yes":
        graph.load_data(stationsCsvFile, connectiesCsvFile, True)
    elif critical == "n" or critical == "N" or critical == "no":
        graph.load_data(stationsCsvFile, connectiesCsvFile)
    else:
        sys.exit("Not a valid input")

    print("For depth first algorithm, type: 1")
    print("For Dijkstra's algorithm, type: 2")
    print("For the Hillclimber, type: 3")
    print("For Simulated Annealing, type: 4")

    algorithm = input("Select: ")
    if int(algorithm != 2):
        print("Calculating routes...")
        graph.makeAllRoutes(maxDuration)

    # Depth first.
    if (int(algorithm) == 1):

        print("For Svens algoritm, type: 1")
        print("For bestScore algoritm, type: 2")

        algoritmBestPaths = input("Select: ")

        # Sven's algorithm to choose paths.
        if (int(algoritmBestPaths) == 1):
            print("Choosing routes...")
            bestPaths = algoritm3(graph)
            print(bestPaths[1])

        # BestScore algorithm to choose paths.
        elif (int(algoritmBestPaths) == 2):
            print("Choosing routes...")
            bestPaths, bestScores = graph.ScorePathsPruning(maxDepth)

        # Error for invalid input.
        else:
            sys.exit("Not a valid algorithm")

        csvFile = input("To which file do you want to save the results (must be a .csv file): ")

        #Run algorithm
        print("Running algorithm...")
        for i in range(maxDepth):
            if (int(algoritmBestPaths) == 1):
                sc, tr = depthFirst(bestPaths, graph.criticalConnections, i, csvFile)
            else:
                sc, tr = depthFirst(bestPaths, graph.criticalConnections, i, csvFile)
            print("beste score: ", sc)
            print("beste trajecten: ", tr)
        drawTraject(graph, tr)

    # Dijkstra's algorithm.
    elif (int(algorithm) == 2):

        #Run algorithm
        print("Running algorithm...")
        bestScore = None
        bestPaths = None
        for i in range(maxDepth):
            newBestPaths = algorithmBritt(graph, i+1, maxDuration)
            newBestScore = CalculateScore(newBestPaths, graph.criticalConnections)
            if bestScore == None or newBestScore > bestScore:
                bestScore = newBestScore
                bestPaths = newBestPaths

        print("number of paths: ", len(bestPaths))
        print("best paths: ", bestPaths)
        print("best score: ", bestScore)
        drawTraject(graph, bestPaths)

    # Hillclimber Algorithm.
    elif (int(algorithm) == 3):
        print("For Svens algoritm, type: 1")
        print("For bestScore algoritm, type: 2")

        algoritmBestPaths = input("Select: ")

        # Sven's algorithm.
        if (int(algoritmBestPaths) == 1):
            print("Choosing routes...")
            bestPaths = algoritm3(graph)
            pathsSelected = random.sample(bestPaths, maxDepth)

        # Bestscore algorithm.
        elif (int(algoritmBestPaths) == 2):
            print("Choosing routes...")
            bestPaths, bestScores = graph.ScorePaths(5 * maxDepth)
            pathsSelected = random.sample(bestPaths, maxDepth)

        #Errormelding
        else:
            sys.exit("Not a valid algorithm")

        #Run algorithm
        print("Running algorithm...")
        bestScore = 0
        for j in range(maxDepth):
            localPathsSelected = pathsSelected[0:j]
            newBestScore = CalculateScore(localPathsSelected, graph.criticalConnections)
            if newBestScore > bestScore:
                bestScore = newBestScore
                bestPaths = localPathsSelected
            for i in range(100):
                localPathsSelected, newBestScore = HillClimber(graph, pathsSelected, bestPaths, bestScore)
                if newBestScore > bestScore:
                    bestScore = newBestScore
                    bestPaths = localPathsSelected
        print("number of paths: ", len(bestPaths))
        print("paths: ", bestPaths)
        print("bestScore: ", bestScore)
        drawTraject(graph, pathsSelected)
        makeGraph("HillClimberScore.csv", "hillclimber_plot.png")

    # Simulated Annealing.
    elif (int(algorithm) == 4):

        print("For Svens algoritm, type: 1")
        print("For bestScore algoritm, type: 2")

        algoritmBestPaths = input("Select: ")

        # Sven's algorithm to get paths.
        if (int(algoritmBestPaths) == 1):
            print("Choosing routes...")
            bestPaths = algoritm3(graph)
            pathsSelected = random.sample(bestPaths, maxDepth)

        # Bestscore algoritm to get paths.
        elif (int(algoritmBestPaths) == 2):
            print("Choosing routes...")
            bestPaths, bestScores = graph.ScorePaths(5 * maxDepth)
            pathsSelected = random.sample(bestPaths, maxDepth)

        # Error
        else:
            sys.exit("Not a valid algorithm")

        #Run algorithm
        print("Running algorithm...")
        bestScore = 0
        for j in range(maxDepth):
            localPathsSelected = pathsSelected[0:j]
            newBestScore = CalculateScore(localPathsSelected, graph.criticalConnections)
            if newBestScore > bestScore:
                bestScore = newBestScore
                bestPaths = localPathsSelected
            for i in range(50):
                localPathsSelected, newBestScore = SimulatedAnnealing(graph, localPathsSelected, [], bestScore)
                if newBestScore > bestScore:
                    bestScore = newBestScore
                    bestPaths = localPathsSelected
        drawTraject(graph, pathsSelected)
        print("number of paths: ", len(bestPaths))
        print("paths: ", bestPaths)
        print("bestScore: ", bestScore)
        makeGraph(os.path.join("Results", "AnnealingScore.csv"), os.path.join("Results","annealing_plot.png"))

    #Errormelding
    else:
        sys.exit("Not a valid algorithm")


if __name__ == "__main__":
    main()
