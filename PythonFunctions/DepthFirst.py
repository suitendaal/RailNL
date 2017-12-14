import csv
import os
import copy
from PythonFunctions.helpers import CalculateScore

def depthFirst(paths, criticalConnections, maxDepth, csvFile, newTraject=[], path=[], depth=0, bestScore=0, bestTraject=[], j=-1):
    """Depth first algoritm to determine best combination of maxDepth trajectories"""
    newTrajectCopy = copy.copy(newTraject)
    # Add new traject to trajectories.
    if path != []:
        newTrajectCopy.append(path)

    # Calculate the score if maximum number of trajects was reached.
    if depth == maxDepth:
        newBestScore = CalculateScore(newTrajectCopy, criticalConnections)
        if newBestScore > bestScore:
            bestScore = newBestScore
            bestTraject = newTrajectCopy

        return bestScore, bestTraject

    # Use recursion to determine next best score and traject.
    for i in range(j + 1, len(paths)):
        newBestScore, newBestTraject = depthFirst(paths, criticalConnections, maxDepth, csvFile, newTrajectCopy, paths[i], depth+1, bestScore, bestTraject, i)
        if newBestScore > bestScore:
            bestScore = newBestScore
            bestTraject = newBestTraject
            csvFile.write(repr(bestScore) + "\n")

            print(bestScore)

    return bestScore, bestTraject
