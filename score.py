import helpers
import copy

# score = 0
# bestTrajectory
# for h in range(0, len(paths))
#     for i in range(h + 1, len(paths)):
#         for j in range(i + 2, len(paths)):
#             for k in range(j + 3, len(paths)):
#                 for l in range(k + 4, len(paths)):
#                     trajectories = [paths[h], paths[i], paths[j], paths[k], paths[l]]
#                     if CalculateScore(trajectories) > score:
#                         score = CalculateScore(trajectories)
#                         bestTrajectory = trajectories


# def bestTrajectoryScore(paths, depth, j=0, score=0, bestTrajectories=[], trajectories=[]):
#     if depth == 0:
#         if CalculateScore(trajectories) > score:
#             score = CalculateScore(trajectories)
#             bestTrajectories = trajectories
#         return score, bestTrajectories

#     for i in range(j, len(paths)):
#         trajectories.append(paths[i])
#         score, bestTrajectories = bestTrajectoryScore(paths, depth - 1, i + 1, score, bestTrajectories, trajectories)

#     return score, bestTrajectories

# def bestTrajectoryScore(paths, depth, critical_connections, firstdepth, score=0, bestTrajectories=[], trajectories=[], trajectory=[]):
#     if depth != firstdepth:
#         trajectories.append(trajectory)

#     if depth == 0:
#         # print(trajectories)
#         if CalculateScore(trajectories, critical_connections) > score:
#             score = CalculateScore(trajectories, critical_connections)
#             bestTrajectories = trajectories
#         return score, bestTrajectories

#     for i in range(firstdepth - depth, len(paths)):
#         trajectory = paths[i]
#         score, bestTrajectories = bestTrajectoryScore(paths, depth - 1, critical_connections, firstdepth, score, bestTrajectories, trajectories, trajectory)

#     return score, bestTrajectories

# best_trajectories = []
# best150paths = []
# best150scores = []
# score = 0
# def determine_trajectories(critical_connections, score, traject = [], depth=0):
#     if depth >= 3:
#         new_score = helpers.CalculateScore(traject, critical_connections)
#         if new_score > score:
#             score = new_score
#             print("hoi", score)
#             best_trajectories = traject
#             return score

#     else:
#         for path in best150paths:
#             traject.append(path)
#             print(traject)
#             determine_trajectories(critical_connections, score, traject, depth+1)

#         return determine_trajectories(critical_connections, score, traject, depth+1)


def scoreSven(paths, maxDepth, criticalConnections, depth=0, score=0, trajecten=[], traject=[], bestTrajecten=[], j=0):
    trajectenCopy = copy.copy(trajecten)

    if traject != []:
        trajectenCopy.append(traject)

    if depth == maxDepth:
        new_score = helpers.CalculateScore(trajectenCopy, criticalConnections)
        if new_score > score:
            score = new_score
            bestTrajecten = trajectenCopy
        return score, bestTrajecten

    for i in range(j + depth, len(paths)+1):
        new_BestScore, newBestTrajecten = scoreSven(paths, maxDepth, criticalConnections, depth+1, score, trajectenCopy, paths[i], bestTrajecten, i)
        if new_BestScore > score:
            score = new_BestScore
            bestTrajecten = newBestTrajecten
    return score, bestTrajecten


def makeAllTrajects(paths, maxDepth, traject=[], depth=0, path=[], j=0):
    trajectCopy = copy.copy(traject)

    if depth != 0:
        trajectCopy += [path]
    if depth == maxDepth:
        return [trajectCopy]

    trajecten = []

    for i in range(j + depth, len(paths)):
        newTrajects = makeAllTrajects(paths, maxDepth, trajectCopy, depth+1, paths[i], i)
        for newTraject in newTrajects:
            trajecten.append(newTraject)

    return trajecten