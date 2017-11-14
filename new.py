import csv
import helpers

best_trajectories = []
best150paths = []
best150scores = []
score = 0
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


def main():

    critical_stations, critical_connections, graph, stationnames = helpers.load_data()

    # Add all of the routes to the list paths, don't use a station twice.
    paths = []
    for i in range(len(stationnames)):
        for j in range(i + 1, len(stationnames)):
            paths.extend(helpers.make_all_routes(graph, stationnames[i], stationnames[j]))

    best150paths = []
    best150scores = []
    for path in paths:
        score = helpers.CalculateScore([path], critical_connections)
        if best150scores == [] or min(best150scores) < score:
            if len(best150paths) < 9:
                best150paths.append(path)
                best150scores.append(score)
            else:
                index = best150scores.index(min(best150scores))
                best150paths[index] = path
                best150scores[index] = score

    print(best150scores)
    # best_score, trajectories = bestTrajectoryScore(best150paths, critical_connections, 3)
    # # best_score = determine_trajectories(critical_connections, 5)

    # print(best_score)

if __name__ == "__main__":
    main()