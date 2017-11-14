import csv

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
    # print(percentage)
    # print(minutes)
    # print(len(trajecten))
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


best_trajectories = []
best150paths = []
best150scores = []
score = 0
def determine_trajectories(critical_connections, score, traject = [], depth=0):
    if depth >= 3:
        new_score = CalculateScore(traject, critical_connections)
        if new_score > score:
            score = new_score
            print("hoi", score)
            best_trajectories = traject
            return score

    else:
        for path in best150paths:
            traject.append(path)
            determine_trajectories(critical_connections, score, traject, depth+1)
    return


def main():
    # List to store stations.
    graph = {}

    # List to store critical stations.
    critical_stations = []

    # List to store the names of the stations.
    stationnames = []
    stationsfile = open('StationsHolland.csv', 'rt')
    stations = csv.reader(stationsfile)
    for station in stations:
        stationnames.append(station[0])
        graph[station[0]] = []
        if station[3] == 'Kritiek':
            critical_stations.append(station[0])
    stationsfile.close()


    critical_connections = []
    # Add connections to the stations.
    connecties = open('ConnectiesHolland.csv', 'rt')
    directions = csv.reader(connecties)
    for direction in directions:
        graph[direction[0]].append([direction[1], direction[2]])
        graph[direction[1]].append([direction[0], direction[2]])
        if direction[0] in critical_stations or direction[1] in critical_stations:
            critical_connections.append([direction[0], direction[1]])
    connecties.close()


    # Add all of the routes to the list paths, don't use a station twice.
    paths = []
    for i in range(len(stationnames)):
        for j in range(i + 1, len(stationnames)):
            paths.extend(make_all_routes(graph, stationnames[i], stationnames[j]))


    for path in paths:
        score = CalculateScore([path], critical_connections)
        if best150scores == [] or min(best150scores) < score:
            if len(best150paths) < 150:
                best150paths.append(path)
                best150scores.append(score)
            else:
                index = best150scores.index(min(best150scores))
                best150paths[index] = path
                best150scores[index] = score

    best_score = determine_trajectories(critical_connections, 0)
    print("Best score: ", best_score)



if __name__ == "__main__":
    main()