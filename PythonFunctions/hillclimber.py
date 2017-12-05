from PythonFunctions.helpers import CalculateScore
import random
import copy
import csv

HillClimberScores = open("HillClimberScore.csv", "w")
HillClimberScoresNew = open("HillClimberScoreNew.csv", "w")

def HillClimber(graph, pathsSelected, paths=[], bestScore=0, index=0):
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
    pathsToChoose.remove(newPathsSelected[index])

    # Change a traject 1000 times and check if it is the best score.
    for i in range(1000):

        # Calculate the new score and check if it is the best score.
        newScore = CalculateScore(newPathsSelected, graph.criticalConnections)
        HillClimberScoresNew.write(str(newScore))
        if newScore > bestScore:
            bestScore = newScore
            pathsSelected = newPathsSelected

        HillClimberScores.write(str(bestScore))

        # Replace a traject with the new random traject.
        newTraject = random.choice(pathsToChoose)
        pathsToChoose.remove(newTraject)
        newPathsSelected[index] = newTraject

    # Do it again for the next traject.
    return HillClimber(graph, pathsSelected, paths, bestScore, index+1)
