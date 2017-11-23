best_trajectories = []
best150paths = []
best150scores = []
score = 0
def determine_trajectories(critical_connections, score, traject = [], depth=0):
    if depth >= 3:
        new_score = helpers.CalculateScore(traject, critical_connections)
        if new_score > score:
            score = new_score
            print("hoi", score)
            best_trajectories = traject
            return score

    else:
        for path in best150paths:
            traject.append(path)
            print(traject)
            determine_trajectories(critical_connections, score, traject, depth+1)

        return determine_trajectories(critical_connections, score, traject, depth+1)

def bestTrajectoryScore(paths, critical_connections, depth, j=0, score=0, bestTrajectories = [], trajectories = [], trajectory = []):

    if j != 0:
        trajectories.append(trajectory)

    if depth == 0:
        if helpers.CalculateScore(trajectories, critical_connections) > score:
            score = helpers.CalculateScore(trajectories, critical_connections)
            bestTrajectories = trajectories
        return score, bestTrajectories

    for i in range(j, len(paths)):
        trajectories.append(paths[i])
        score, bestTrajectories = bestTrajectoryScore(paths, critical_connections, depth - 1, i + 1, score, bestTrajectories, trajectories, trajectory)

    return score, bestTrajectories


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