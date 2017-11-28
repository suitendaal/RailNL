import csv
import copy

def CalculateScore(trajecten, criticalConnections):
    """Function to compute the score"""

    minutes = 0
    trains = len(trajecten)
    critical_connection = 0
    critical_connections_past = []

    for traject in trajecten:
        minutes += int(traject[1])
        for i in range(len(traject[0]) - 1):
            this_station = traject[0][i]
            next_station = traject[0][i + 1]
            if [this_station, next_station] in criticalConnections or [next_station, this_station] in criticalConnections:
                if [this_station, next_station] not in critical_connections_past and [next_station, this_station] not in critical_connections_past:
                    critical_connections_past.append([this_station, next_station])
                    critical_connection += 1

    percentage = critical_connection/len(criticalConnections) * 100
    score = percentage*10000 - (trains*20 + minutes/100000)
    return score



def make_all_routes(graph, start, end, route=[], time=0):
    """Function to get all routes between to stations, within 2 hours"""

    # Add start to route.
    route = route + [start]

    # At the end, return the route.
    if start == end:
        return [[route, time]]

    # If the route doesn't exist, return nothing.
    elif not graph[start]:
        return []
    routes = []

    # Check the route for every destination.
    for destination in graph[start]:

        # Do not pass the same station twice.
        if destination[0] not in route:
            # Ensure the route doesn't take longer than 2 hours.
            duration = time + int(destination[1])
            if duration < 120:
                # Make the new routes for the further stations.
                new_routes = make_all_routes(graph, destination[0], end, route, duration)
                for new_route in new_routes:
                    routes.append(new_route)
    return routes

def ScorePaths(graph, n):
    "Function to determine the best n trajectories based on the score"
    bestpaths = []
    bestscores = []

    # Add path, calculate score and keep track of the best score and trajectories
    for path in graph.allRoutes:
        score = CalculateScore([path], graph.criticalConnections)
        if bestscores == [] or min(bestscores) < score:
            if len(bestpaths) < n:
                bestpaths.append(path)
                bestscores.append(score)
            else:
                index = bestscores.index(min(bestscores))
                bestpaths[index] = path
                bestscores[index] = score

    return bestpaths, bestscores


def getBestScore(paths, criticalConnections, maxDepth, newTraject=[], path=[], depth=0, bestScore=0, bestTraject=[], j=-1):
    "Depth first algoritm to determine best combination of n trajectories"
    newTrajectCopy = copy.copy(newTraject)

    # Add new traject to trajectories
    if path != []:
        newTrajectCopy.append(path)

    # Calculate the score if maximum number of trajects was reached
    if depth == maxDepth:
        newBestScore = CalculateScore(newTrajectCopy, criticalConnections)
        if newBestScore > bestScore:
            bestScore = newBestScore
            bestTraject = newTrajectCopy

        return bestScore, bestTraject

    # Use recursion to determine next best score and traject
    for i in range(j + 1, len(paths)):
        newBestScore, newBestTraject = getBestScore(paths, criticalConnections, maxDepth, newTrajectCopy, paths[i], depth+1, bestScore, bestTraject, i)
        if newBestScore > bestScore:
            bestScore = newBestScore
            bestTraject = newBestTraject
            print(bestScore)

    return bestScore, bestTraject
