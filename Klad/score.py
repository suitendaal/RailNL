score = 0
bestTrajectory
for h in range(0, len(paths))
    for i in range(h + 1, len(paths)):
        for j in range(i + 2, len(paths)):
            for k in range(j + 3, len(paths)):
                for l in range(k + 4, len(paths)):
                    trajectories = [paths[h], paths[i], paths[j], paths[k], paths[l]]
                    if CalculateScore(trajectories) > score:
                        score = CalculateScore(trajectories)
                        bestTrajectory = trajectories


def bestTrajectoryScore(paths, depth, j=0, score=0, bestTrajectories=[], trajectories=[]):
    if depth == 0:
        if CalculateScore(trajectories) > score:
            score = CalculateScore(trajectories)
            bestTrajectories = trajectories
        return score, bestTrajectories

    for i in range(j, len(paths)):
        trajectories.append(paths[i])
        score, bestTrajectories = bestTrajectoryScore(paths, depth - 1, i + 1, score, bestTrajectories, trajectories)

    return score, bestTrajectories

def bestTrajectoryScore(paths, depth, critical_connections, firstdepth, score=0, bestTrajectories=[], trajectories=[], trajectory=[]):
    if depth != firstdepth:
        trajectories.append(trajectory)

    if depth == 0:
        # print(trajectories)
        if CalculateScore(trajectories, critical_connections) > score:
            score = CalculateScore(trajectories, critical_connections)
            bestTrajectories = trajectories
        return score, bestTrajectories

    for i in range(firstdepth - depth, len(paths)):
        trajectory = paths[i]
        score, bestTrajectories = bestTrajectoryScore(paths, depth - 1, critical_connections, firstdepth, score, bestTrajectories, trajectories, trajectory)

    return score, bestTrajectories

def determine_trajectories(critical_connections, max_depth, score=0, best_trajectories = [], trajectory = [], traject = [], depth=0):

    if depth == max_depth:
        new_score = CalculateScore(traject, critical_connections)
        if new_score > score:
            score = new_score
            best_trajectories = traject
        return score, best_trajectories

    traject.append(trajectory)

    for i in range(depth, len(best150paths)):
        trajectory = best150paths[i]
        score, best_trajectories = determine_trajectories(critical_connections, max_depth, score, best_trajectories, trajectory, traject, depth+1)

    return score, best_trajectories