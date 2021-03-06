from PythonFunctions.helpers import CalculateScore
import random
import copy
import csv
import os

def HillClimber(graph, pathsSelected, csvFile, paths=[], bestScore=0, index=0):
    """Function that changes a traject piece by piece and calculates the new score.
        Saves the new score if it is the best score"""

    # Stop at the final index.
    if index == len(pathsSelected):
        return pathsSelected, bestScore

    if paths == []:
        paths = graph.allRoutes

    newPathsSelected = copy.copy(pathsSelected)

    # Change a traject 100 times and check if it is the best score.
    for i in range(100):

        # Calculate the new score and check if it is the best score.
        newScore = CalculateScore(newPathsSelected, graph.criticalConnections)
        csvFile.write(repr(newScore)+"\n")
        if newScore > bestScore:
            bestScore = newScore
            pathsSelected = newPathsSelected

        # Replace a traject with the new random traject.
        newTraject = random.choice(paths)
        newPathsSelected[index] = newTraject

    # Do it again for the next traject.
    return HillClimber(graph, pathsSelected, csvFile, paths, bestScore, index+1)
