from PythonFunctions.helpers import CalculateScore
import random

def HillClimber(paths, pathsSelected, criticalConnections, index = 0, bestScore = 0, bestPaths=[]):

    if index == len(pathsSelected):
        return pathsSelected, bestScore

    newScore = CalculateScore(pathsSelected, criticalConnections)
    if newScore > bestScore:
        bestScore = newScore
        bestPaths = pathsSelected

    pathsToChoose = paths
    pathsToChoose.

    newPathsSelected = pathsSelected
    for i in range(1000):
        newPath = random.choice(paths)
        while newPath in pathsChosen:
            newPath = random.choice(paths)
        pathsChosen.append(newPath)
        newPathsSelected[index] = random.choice(paths)
        newScore = CalculateScore(newPathsSelected, criticalConnections)
        if newScore > bestScore:
            bestScore = newScore
            bestPaths = newPathsSelected

    return HillClimber(paths, bestPaths, criticalConnections, index+1, bestScore, bestPaths)
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
