import csv
import os

def depthFirst(paths, criticalConnections, maxDepth, csv = "new.csv", newTraject=[], path=[], depth=0, bestScore=0, bestTraject=[], j=-1):
    """Depth first algoritm to determine best combination of maxDepth trajectories"""
    newTrajectCopy = copy.copy(newTraject)
    csvFile = os.path.join("Results", csv)
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
        newBestScore, newBestTraject = depthFirst(paths, criticalConnections, maxDepth, newTrajectCopy, paths[i], depth+1, bestScore, bestTraject, i)
        if newBestScore > bestScore:
            bestScore = newBestScore
            bestTraject = newBestTraject
            csvFile.write(repr(bestScore) + "\n")

            print(bestScore)

    return bestScore, bestTraject
