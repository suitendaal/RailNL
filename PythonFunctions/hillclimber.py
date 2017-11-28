from PythonFunctions.helpers import CalculateScore
import random
import copy

def HillClimber(paths, pathsSelected, criticalConnections, bestScore, index = 0, bestPaths=[]):
    """Function that changes a traject piece by piece and calculates the new score.
        Saves the new score if it is the best score"""

    print(len(pathsSelected))
    print(index)
    # Stop at the final index.
    if index == len(pathsSelected):
        return pathsSelected, bestScore

    # Archive
    pathsToChoose = copy.copy(paths)
    pathsToChoose.remove(pathsSelected[index])

    # Change a traject 1000 times and check if it is the best score.
    for i in range(1000):

        # Replace a traject with the new random traject.
        newTraject = random.choice(pathsToChoose)
        pathsToChoose.remove(newTraject)
        pathsSelected[index] = newTraject

        # Calculate the new score and check if it is the best score.
        newScore = CalculateScore(pathsSelected, criticalConnections)
        if newScore > bestScore:
            bestScore = newScore
            bestPaths = pathsSelected

    # Do it again for the next traject.
    return HillClimber(paths, bestPaths, criticalConnections, bestScore, index+1, bestPaths)
    # score = helpers.CalculateScore(paths_selected, critical_connections)
    #


        # lowest_score = 1000000
        # lowest_path
        # for path in paths_selected:
        #     path_score = helpers.CalculateScore(path, critical_connections)
        #     if path_score < lowest_score:
        #         lowest_score = path_score
        #         lowest_path = paths_selected.index(path)
    # score = CalculateScore(paths_selected, critical_connections)
    # if score > best_score:
    #     best_score = score
    #
    # for path in paths_selected:
    #     n = 0
    #     new_paths = paths_selected
    #     while (score <= best_score and n < 100):
    #         new_paths[new_paths.index(path)] = random.choice(paths)
    #         new_score = CalculateScore(new_paths, critical_connections)
    #         print("score: ",score)
    #         n+=1
    #         if new_score > best_score:
    #             paths_selected = new_paths
    #             best_score = new_score


    return HillClimber(paths, paths_selected, critical_connections, best_score, m + 1)
