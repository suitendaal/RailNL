import csv
import copy
import os

DepthFirst_sven = open(os.path.join('results', "DepthFirst_sven.csv"), "w")
DepthFirst_bestscores = open(os.path.join('results', "DepthFirst_bestscores.csv"), "w")

def CalculateScore(trajecten, criticalConnections):
    """Function to compute the score"""

    minutes = 0
    trains = len(trajecten)
    critical_connection = 0
    critical_connections_past = []

    for traject in trajecten:
        minutes += int(traject[1])
        for i in range(len(traject[0]) - 1):
            this_station = traject[0][i]
            next_station = traject[0][i + 1]
            if [this_station, next_station] in criticalConnections or [next_station, this_station] in criticalConnections:
                if [this_station, next_station] not in critical_connections_past and [next_station, this_station] not in critical_connections_past:
                    critical_connections_past.append([this_station, next_station])
                    critical_connection += 1

    percentage = critical_connection/len(criticalConnections) * 100
    score = percentage*10000 - (trains*20 + minutes/100000)
    return score

def getBestScore(method, paths, criticalConnections, maxDepth, newTraject=[], path=[], depth=0, bestScore=0, bestTraject=[], j=-1):
    "Depth first algoritm to determine best combination of maxDepth trajectories"
    newTrajectCopy = copy.copy(newTraject)

    # Add new traject to trajectories
    if path != []:
        newTrajectCopy.append(path)

    # Calculate the score if maximum number of trajects was reached
    if depth == maxDepth:
        newBestScore = CalculateScore(newTrajectCopy, criticalConnections)
        if newBestScore > bestScore:
            bestScore = newBestScore
            bestTraject = newTrajectCopy

        return bestScore, bestTraject

    # Use recursion to determine next best score and traject
    for i in range(j + 1, len(paths)):
        newBestScore, newBestTraject = getBestScore(method, paths, criticalConnections, maxDepth, newTrajectCopy, paths[i], depth+1, bestScore, bestTraject, i)
        if newBestScore > bestScore:
            bestScore = newBestScore
            bestTraject = newBestTraject
            if method == 1:
                DepthFirst_sven.write(repr(bestScore) + "\n")
            if method == 2:
                DepthFirst_bestscores.write(repr(bestScore) + "\n")

            print(bestScore)

    return bestScore, bestTraject
