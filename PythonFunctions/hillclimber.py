from PythonFunctions.helpers import CalculateScore
import random
import copy

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
        if newScore > bestScore:
            bestScore = newScore
            pathsSelected = newPathsSelected

        # Replace a traject with the new random traject.
        newTraject = random.choice(pathsToChoose)
        pathsToChoose.remove(newTraject)
        newPathsSelected[index] = newTraject

    # Do it again for the next traject.
    return HillClimber(graph, pathsSelected, paths, bestScore, index+1)
