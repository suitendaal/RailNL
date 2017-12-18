from PythonFunctions.helpers import CalculateScore
import random
import copy
import csv
import os

def SimulatedAnnealing(graph, pathsSelected, csvFile, paths=[], bestScore=0, index=0):
    """Function that changes a traject piece by piece and calculates the new score.
        Saves the new score if it is the best score."""

    # Stop at the final index.
    if index == len(pathsSelected):
        return pathsSelected, bestScore

    if paths == []:
        paths = graph.allRoutes

    newPathsSelected = copy.copy(pathsSelected)

    # Number of times at the same score.
    iteration = 0

    # Number of times stuck in the while true loop.
    i = 0

    while True:
        i += 1
        iteration += 1

        # If more than 500 times at the same score, break.
        if iteration > 500:
            break

        # Calculate the new score and check if it is the best score.
        newScore = CalculateScore(newPathsSelected, graph.criticalConnections)
        if newScore > bestScore:
            bestScore = newScore
            pathsSelected = newPathsSelected

            # Set number of times at the same score back to 0.
            iteration = 0

        # If new score is lower, check if score has to be replaced.
        elif ScoreAnnealing(iteration, i, newScore, bestScore) > random.uniform(0.7, 1):
                bestScore = newScore
                pathsSelected = newPathsSelected
                iteration = 0

        # Write to csv.
        csvFile.write(repr(newScore) + "\n")

        # Replace a traject with the new random traject.
        newTraject = random.choice(pathsToChoose)
        newPathsSelected[index] = newTraject

    # Do it again for the next traject.
    return SimulatedAnnealing(graph, pathsSelected, csvFile, paths, bestScore, index+1)

def ScoreAnnealing(iteration, i, newScore, bestScore):
    # Returns a number between 0 and 1.
    return newScore / bestScore * iteration / i
