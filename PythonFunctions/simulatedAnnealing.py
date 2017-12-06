from PythonFunctions.helpers import CalculateScore
import random
import copy
import csv

AnnealingScores = open("AnnealingScore.csv", "w")
AnnealingScoresNew = open("AnnealingScoreNew.csv", "w")

def SimulatedAnnealing(graph, pathsSelected, paths=[], bestScore=0, index=0):
    """Function that changes a traject piece by piece and calculates the new score.
        Saves the new score if it is the best score"""

    # Stop at the final index.
    if index == len(pathsSelected):
        return pathsSelected, bestScore

    if paths == []:
        paths = graph.allRoutes

    newPathsSelected = pathsSelected

    # Archive
    pathsToChoose = copy.copy(paths)
    # pathsToChoose.remove(newPathsSelected[index])

    n = 1000
    if n > len(paths):
        n = len(paths)

    iteratie = 0
    i = 0
    # Change a traject 1000 times and check if it is the best score.
    while True:
        i += 1
        iteratie += 1

        if iteratie > 50:
            break
        # Calculate the new score and check if it is the best score.
        newScore = CalculateScore(newPathsSelected, graph.criticalConnections)
        AnnealingScoresNew.write(repr(newScore) + "\n")
        if newScore > bestScore:
            bestScore = newScore
            pathsSelected = newPathsSelected
            iteratie = 0

        elif ScoreAnnealing(iteratie, i, newScore, bestScore) > 0.98:
            # 0.8 kan ook vervangen worden door random tussen 0 en 1
            bestScore = newScore
            pathsSelected = newPathsSelected
            iteratie = 0

        AnnealingScores.write(repr(bestScore)+"\n")

        # Replace a traject with the new random traject.
        newTraject = random.choice(pathsToChoose)
        # pathsToChoose.remove(newTraject)
        newPathsSelected[index] = newTraject

    # Do it again for the next traject.
    return SimulatedAnnealing(graph, pathsSelected, paths, bestScore, index+1)

def ScoreAnnealing(iteratie, i, newScore, bestScore):
    # Scorefunctie kan worden aangepast, bijv (newScore / bestScore)^3 * iteratie / i
    return newScore / bestScore * iteratie / i
