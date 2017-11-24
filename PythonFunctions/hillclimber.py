import helpers
import random

def HillClimber(paths, paths_selected, critical_connections, best_score = 0, m = 0):

    if m == 1000:
        return paths_selected, best_score
    # score = helpers.CalculateScore(paths_selected, critical_connections)
    #


        # lowest_score = 1000000
        # lowest_path
        # for path in paths_selected:
        #     path_score = helpers.CalculateScore(path, critical_connections)
        #     if path_score < lowest_score:
        #         lowest_score = path_score
        #         lowest_path = paths_selected.index(path)

    for path in paths_selected:
        score = best_score
        n = 0
        new_paths = paths_selected
        while (score < best_score and n < 100):
            new_paths[new_paths.index(path)] = rondom.choice(paths)
            score = helper.CalculateScore(new_paths, critical_connections)
            n++
        if score > best_score:
            paths_selected = new_paths
            best_score = score

    HillClimber(paths, paths_selected, critical_connections, best_score, m + 1)
