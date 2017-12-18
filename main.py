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

    print("For Depth first algorithm, type: 1")
    print("For Greedy algorithm, type: 2")
    print("For the Hillclimber, type: 3")
    print("For Simulated Annealing, type: 4")


    drawTraject(graph, [[['Eindhoven', 's-Hertogenbosch', 'Tilburg', 'Breda', 'Dordrecht', 'Rotterdam Centraal', 'Schiedam Centrum'], 86], [['Groningen', 'Assen', 'Zwolle', 'Amersfoort', 'Utrecht Centraal', 'Amsterdam Amstel', 'Amsterdam Centraal', 'Amsterdam Sloterdijk', 'Haarlem', 'Heemstede-Aerdenhout'], 156], [['Delft', 'Den Haag HS', 'Leiden Centraal', 'Schiphol Airport', 'Utrecht Centraal', 'Gouda', 'Den Haag Centraal'], 104], [['Dordrecht', 'Rotterdam Centraal', 'Rotterdam Alexander', 'Gouda', 'Utrecht Centraal', 'Amersfoort', 'Zwolle', 'Assen', 'Groningen'], 159], [['Amsterdam Centraal', 'Amsterdam Sloterdijk', 'Amsterdam Zuid', 'Schiphol Airport', 'Utrecht Centraal', 's-Hertogenbosch', 'Oss', 'Nijmegen', 'Arnhem Centraal'], 127], [['Heerenveen', 'Steenwijk', 'Zwolle', 'Amersfoort', 'Utrecht Centraal', 'Amsterdam Amstel', 'Amsterdam Centraal', 'Almere Centrum', 'Lelystad Centrum'], 148], [['Enschede', 'Hengelo', 'Almelo', 'Zwolle', 'Amersfoort', 'Utrecht Centraal', 'Amsterdam Amstel', 'Amsterdam Centraal', 'Amsterdam Sloterdijk', 'Amsterdam Zuid', 'Schiphol Airport'], 163], [['Almelo', 'Zwolle', 'Steenwijk', 'Heerenveen', 'Leeuwarden', 'Groningen', 'Assen'], 148], [['Almere Centrum', 'Hilversum', 'Utrecht Centraal', 'Gouda', 'Rotterdam Alexander', 'Rotterdam Blaak', 'Dordrecht', 'Rotterdam Centraal', 'Schiedam Centrum', 'Delft', 'Den Haag HS', 'Leiden Centraal', 'Heemstede-Aerdenhout', 'Haarlem', 'Amsterdam Sloterdijk', 'Amsterdam Centraal'], 177], [['Apeldoorn', 'Amersfoort', 'Utrecht Centraal', 's-Hertogenbosch', 'Tilburg', 'Breda', 'Dordrecht', 'Rotterdam Centraal', 'Rotterdam Alexander'], 136], [['Oss', 'Nijmegen', 'Arnhem Centraal', 'Ede-Wageningen', 'Utrecht Centraal', 's-Hertogenbosch', 'Tilburg'], 104], [['Delft', 'Den Haag Centraal', 'Leiden Centraal', 'Schiphol Airport', 'Utrecht Centraal', 'Gouda', 'Den Haag HS'], 112], [['Beverwijk', 'Haarlem', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Utrecht Centraal', 's-Hertogenbosch', 'Tilburg', 'Breda', 'Dordrecht', 'Rotterdam Centraal', 'Rotterdam Alexander', 'Gouda'], 168], [['Etten-Leur', 'Roosendaal', 'Dordrecht', 'Breda', 'Tilburg', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht'], 146], [['Eindhoven', 'Tilburg', 'Breda', 'Dordrecht', 'Rotterdam Centraal', 'Rotterdam Alexander', 'Gouda', 'Utrecht Centraal', 's-Hertogenbosch', 'Oss', 'Nijmegen'], 159], [['Den Helder', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Utrecht Centraal', 's-Hertogenbosch', 'Tilburg', 'Breda', 'Dordrecht'], 169], [['Alphen a/d Rijn', 'Gouda', 'Den Haag Centraal', 'Leiden Centraal', 'Heemstede-Aerdenhout', 'Haarlem', 'Amsterdam Sloterdijk', 'Amsterdam Zuid', 'Schiphol Airport', 'Utrecht Centraal', 's-Hertogenbosch', 'Oss'], 172], [['Amersfoort', 'Utrecht Centraal', 's-Hertogenbosch', 'Tilburg', 'Breda', 'Dordrecht', 'Rotterdam Centraal'], 104], [['Leiden Centraal', 'Den Haag HS', 'Delft', 'Den Haag Centraal', 'Gouda', 'Utrecht Centraal', 's-Hertogenbosch', 'Tilburg', 'Eindhoven', 'Weert', 'Roermond', 'Sittard'], 178], [['Den Haag Laan v NOI', 'Leiden Centraal', 'Schiphol Airport', 'Utrecht Centraal', 'Amsterdam Amstel', 'Amsterdam Centraal', 'Amsterdam Sloterdijk', 'Haarlem', 'Beverwijk', 'Zaandam'], 142], [['Den Haag Laan v NOI', 'Leiden Centraal', 'Heemstede-Aerdenhout', 'Haarlem', 'Amsterdam Sloterdijk', 'Amsterdam Zuid', 'Schiphol Airport', 'Utrecht Centraal', 'Amersfoort', 'Zwolle', 'Steenwijk'], 167], [['Roermond', 'Weert', 'Eindhoven', 's-Hertogenbosch', 'Tilburg', 'Breda', 'Dordrecht', 'Rotterdam Blaak'], 109]], os.path.join("Results", 'nnhd.png'))
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
