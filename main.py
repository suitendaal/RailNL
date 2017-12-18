import os
import sys
import csv
import random

from Classes.graphClass import Graph

from PythonFunctions.Greedy import algorithmGreedy
from PythonFunctions.DijkstraAlgorithm import algorithmDijkstra
from PythonFunctions.helpers import CalculateScore
from PythonFunctions.DepthFirst import depthFirst
from PythonFunctions.hillclimber import HillClimber
from PythonFunctions.simulatedAnnealing import SimulatedAnnealing

from PlotFunctions.drawTraject import drawTraject
from PlotFunctions.makeGraph import makeGraph


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

    drawTraject(graph, [[['Amsterdam Zuid', 'Amsterdam Amstel', 'Amsterdam Centraal', 'Amsterdam Sloterdijk', 'Haarlem', 'Heemstede-Aerdenhout', 'Leiden Centraal', 'Den Haag Centraal', 'Delft', 'Schiedam Centrum', 'Rotterdam Centraal', 'Rotterdam Alexander', 'Gouda'], 109], [['Amsterdam Centraal', 'Amsterdam Sloterdijk', 'Zaandam', 'Castricum', 'Beverwijk', 'Haarlem', 'Heemstede-Aerdenhout', 'Leiden Centraal', 'Den Haag Centraal', 'Delft', 'Schiedam Centrum', 'Rotterdam Centraal', 'Rotterdam Alexander'], 117], [['Delft', 'Schiedam Centrum', 'Rotterdam Centraal', 'Rotterdam Alexander', 'Gouda', 'Alphen a/d Rijn', 'Leiden Centraal', 'Schiphol Airport', 'Amsterdam Zuid', 'Amsterdam Amstel', 'Amsterdam Centraal', 'Amsterdam Sloterdijk', 'Haarlem'], 119], [['Delft', 'Schiedam Centrum', 'Rotterdam Centraal', 'Rotterdam Alexander', 'Gouda', 'Den Haag Centraal', 'Leiden Centraal', 'Schiphol Airport', 'Amsterdam Zuid', 'Amsterdam Amstel', 'Amsterdam Centraal', 'Amsterdam Sloterdijk', 'Zaandam'], 111], [['Delft', 'Schiedam Centrum', 'Rotterdam Centraal', 'Rotterdam Alexander', 'Gouda', 'Den Haag Centraal', 'Leiden Centraal', 'Schiphol Airport', 'Amsterdam Zuid', 'Amsterdam Amstel', 'Amsterdam Centraal', 'Amsterdam Sloterdijk', 'Haarlem'], 116], [['Schiedam Centrum', 'Rotterdam Centraal', 'Rotterdam Alexander', 'Gouda', 'Alphen a/d Rijn', 'Leiden Centraal', 'Heemstede-Aerdenhout', 'Haarlem', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Amsterdam Zuid', 'Schiphol Airport'], 116], [['Dordrecht', 'Rotterdam Centraal', 'Schiedam Centrum', 'Delft', 'Den Haag Centraal', 'Leiden Centraal', 'Heemstede-Aerdenhout', 'Haarlem', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Amsterdam Zuid', 'Schiphol Airport'], 114]], os.path.join("Results", 'hchb.png'))

    print("For Depth first algorithm, type: 1")
    print("For Greedy algorithm, type: 2")
    print("For the Hillclimber, type: 3")
    print("For Simulated Annealing, type: 4")

    algorithm = input("Select: ")
    if int(algorithm) != 2:
        print("Calculating routes...")
        graph.makeAllRoutes(maxDuration)

    # Depth first.
    if (int(algorithm) == 1):

        print("For Dijkstra algorithm, type: 1")
        print("For bestScore algorithm, type: 2")

        algorithmBestPaths = input("Select: ")

        # Dijkstra algorithm to choose paths.
        if (int(algorithmBestPaths) == 1):
            print("Choosing routes...")
            bestPaths = algorithmDijkstra(graph)
            print(bestPaths[1])

        # BestScore algorithm to choose paths.
        elif (int(algorithmBestPaths) == 2):
            print("Choosing routes...")
            bestPaths, bestScores = graph.ScorePathsPruning(maxDepth)
        # Error for invalid input.
        else:
            sys.exit("Not a valid algorithm")

        csvFileName = input("To which file do you want to save the results (must be a .csv file): ")
        figFileName = input("To which file do you want to save the plot (must be a .png file): ")

        # Run algorithm
        print("Running algorithm...")
        csvFile = open(os.path.join("Results", csvFileName), 'w')

        bestScore = None
        bestPaths = None
        for i in range(maxDepth):
            if (int(algorithmBestPaths) == 1):
                sc, tr = depthFirst(bestPaths, graph.criticalConnections, i, csvFile)
            else:
                sc, tr = depthFirst(bestPaths, graph.criticalConnections, i, csvFile)
            if bestScore == None or sc > bestScore:
                bestScore = sc
                bestPaths = tr

        # Print the outcome of the algorithm
        print("number of trajectories: ", len(bestPaths))
        print("beste score: ", bestScore)
        print("beste trajecten: ", bestPaths)
        drawTraject(graph, tr, os.path.join("Results", figFileName))

    # Greedy algorithm.
    elif (int(algorithm) == 2):

        csvFileName = input("To which file do you want to save the results (must be a .csv file): ")
        figFileName = input("To which file do you want to save the plot (must be a .png file): ")

        csvFile = open(os.path.join("Results", csvFileName), 'w')

        # Run algorithm.
        print("Running algorithm...")
        bestScore = None
        bestPaths = None

        for i in range(maxDepth):
            newBestPaths = algorithmGreedy(graph, i+1, maxDuration)
            newBestScore = CalculateScore(newBestPaths, graph.criticalConnections)
            if bestScore == None or newBestScore > bestScore:
                bestScore = newBestScore
                bestPaths = newBestPaths
            csvFile.write(repr(bestScore) + "\n")

        print("number of paths: ", len(bestPaths))
        print("best paths: ", bestPaths)
        print("best score: ", bestScore)
        drawTraject(graph, bestPaths, os.path.join("Results", figFileName))

    # Hillclimber Algorithm.
    elif (int(algorithm) == 3):
        print("For Dijkstra algorithm, type: 1")
        print("For bestScore algorithm, type: 2")

        algorithmBestPaths = input("Select: ")

        # Dijkstra algorithm.
        if (int(algorithmBestPaths) == 1):
            print("Choosing routes...")
            bestPaths = algorithmDijkstra(graph)
            pathsSelected = random.sample(bestPaths, maxDepth)

        # Bestscore algorithm.
        elif (int(algorithmBestPaths) == 2):
            print("Choosing routes...")
            bestPaths, bestScores = graph.ScorePathsPruning(5 * maxDepth)
            pathsSelected = random.sample(bestPaths, maxDepth)

        # Error
        else:
            sys.exit("Not a valid algorithm")

        csvFileName = input("To which file do you want to save the results (must be a .csv file): ")
        figFileName = input("To which file do you want to save the plot of the trajects (must be a .png file): ")

        csvFile = open(os.path.join("Results", csvFileName), 'w')

        # Run algorithm
        print("Running algorithm...")
        bestScore = 0
        for j in range(maxDepth):
            localPathsSelected = pathsSelected[0:j]
            newBestScore = CalculateScore(localPathsSelected, graph.criticalConnections)
            if newBestScore > bestScore:
                bestScore = newBestScore
                bestPaths = localPathsSelected
            for i in range(100):
                localPathsSelected, newBestScore = HillClimber(graph, pathsSelected, csvFile, bestPaths, bestScore)
                if newBestScore > bestScore:
                    bestScore = newBestScore
                    bestPaths = localPathsSelected
        print("number of paths: ", len(bestPaths))
        print("paths: ", bestPaths)
        print("bestScore: ", bestScore)
        drawTraject(graph, bestPaths, figFileName)

    # Simulated Annealing.
    elif (int(algorithm) == 4):

        print("For Dijkstra algorithm, type: 1")
        print("For bestScore algorithm, type: 2")

        algorithmBestPaths = input("Select: ")

        # Dijkstra algorithm to get paths.
        if (int(algorithmBestPaths) == 1):
            print("Choosing routes...")
            bestPaths = algorithmDijkstra(graph)
            pathsSelected = random.sample(bestPaths, maxDepth)

        # Bestscore algorithm to get paths.
        elif (int(algorithmBestPaths) == 2):
            print("Choosing routes...")
            bestPaths, bestScores = graph.ScorePathsPruning(5 * maxDepth)
            pathsSelected = random.sample(bestPaths, maxDepth)

        # Error
        else:
            sys.exit("Not a valid algorithm")

        csvFileName = input("To which file do you want to save the results (must be a .csv file): ")
        figFileName = input("To which file do you want to save the plot of the trajects (must be a .png file): ")

        csvFile = open(os.path.join("Results", csvFileName), 'w')

        # Run algorithm
        print("Running algorithm...")
        bestScore = 0

        # Try for 0 till maxDepth number of trajectories
        for j in range(maxDepth):
            localPathsSelected = pathsSelected[0:j]
            newBestScore = CalculateScore(localPathsSelected, graph.criticalConnections)
            if newBestScore > bestScore:
                bestScore = newBestScore
                bestPaths = localPathsSelected
            for i in range(100):
                localPathsSelected, newBestScore = SimulatedAnnealing(graph, localPathsSelected, csvFile, [], bestScore)
                if newBestScore > bestScore:
                    bestScore = newBestScore
                    bestPaths = localPathsSelected
        drawTraject(graph, bestPaths, os.path.join("Results", figFileName))
        print("number of paths: ", len(bestPaths))
        print("paths: ", bestPaths)
        print("bestScore: ", bestScore)

    # Error
    else:
        sys.exit("Not a valid algorithm")

    print("stations: ", stations)
    print("critical: ", critical)
    print("algorithm: ", algorithm)
    if int(algorithm) != 2:
        print("algorith best paths: ", algorithmBestPaths)

if __name__ == "__main__":
    main()
