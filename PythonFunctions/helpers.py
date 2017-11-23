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




def load_data(stationsCsvFile, connectiesCsvFile):

    # List to store stations.
    graph = {}

    # List to store critical stations.
    critical_stations = []

    # List to store the names of the stations.
    stationnames = []
    stationsfile = open(stationsCsvFile, 'rt')
    stations = csv.reader(stationsfile)
    for station in stations:
        stationnames.append(station[0])
        graph[station[0]] = []
        if station[3] == 'Kritiek':
            critical_stations.append(station[0])
    stationsfile.close()


    critical_connections = []

    # Add connections to the stations.
    connecties = open(connectiesCsvFile, 'rt')
    directions = csv.reader(connecties)
    for direction in directions:
        graph[direction[0]].append([direction[1], direction[2]])
        graph[direction[1]].append([direction[0], direction[2]])
        if direction[0] in critical_stations or direction[1] in critical_stations:
            critical_connections.append([direction[0], direction[1]])
    connecties.close()

    return critical_stations, critical_connections, graph, stationnames




def add_paths(graph, stationnames):
    paths = []
    for i in range(len(stationnames)):
        for j in range(i + 1, len(stationnames)):
            paths.extend(make_all_routes(graph, stationnames[i], stationnames[j]))
    return paths



def ScorePaths(paths, critical_connections, n):
    bestpaths = []
    bestscores = []
    for path in paths:
        score = CalculateScore([path], critical_connections)
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

    newTrajectCopy = copy.copy(newTraject)

    if path != []:
        newTrajectCopy.append(path)

    if depth == maxDepth:
        newBestScore = CalculateScore(newTrajectCopy, criticalConnections)
        if newBestScore > bestScore:
            bestScore = newBestScore
            bestTraject = newTrajectCopy

        return bestScore, bestTraject

    for i in range(j + 1, len(paths)):
        newBestScore, newBestTraject = getBestScore(paths, criticalConnections, maxDepth, newTrajectCopy, paths[i], depth+1, bestScore, bestTraject, i)
        if newBestScore > bestScore:
            bestScore = newBestScore
            bestTraject = newBestTraject

    return bestScore, bestTraject