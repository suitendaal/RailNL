import copy

def Greedy(graph, station, maxTime, allConnections, route=[], time=0):
    """Algorithm which picks the most critical route for a given beginstation."""

    # Keep a list of critical- and non-critical destinations.
    critical = []
    nonCritical = []

    route.append(station)

    # Ensure greedy does not cross the maximum time frame.
    if time == maxTime:
        return route, time

    destinations = graph.graph[station]
    for destination in destinations:

        # Ensure connection is not passed already.
        goOn = False
        for connection in allConnections:
            if [station, destination] == connection[0] or [destination, station] == connection[0]:
                goOn = True
                break
        if goOn:
            if destination[0] not in route:
                if [destination[0], station] in graph.criticalConnections or [station, destination[0]] in graph.criticalConnections:
                    critical.append(destination)
                else:
                    nonCritical.append(destination)

    # Choose the shortest critical connection.
    shortestTime = None
    shortestConnection = None
    if len(critical) != 0:
        for traject in critical:
            if traject not in route:

                # Choose the shortest connection.
                if shortestTime == None or int(traject[1]) < shortestTime:
                    shortestTime = int(traject[1])

                    # Ensure route doesn't pass the maximum timeframe.
                    if time + shortestTime <= maxTime:
                        shortestConnection = traject[0]

        # Ensure there is a new connection added.
        if shortestConnection != None:

            # Choose the next station.
            return Greedy(graph, shortestConnection, maxTime, allConnections, route, time + shortestTime)

    # If there is no critical connection, choose the shortest connenction.
    if len(nonCritical) != 0:
        for traject in nonCritical:
            if traject not in route:

                # Choose the shortest connection.
                if shortestTime == None or int(traject[1]) < shortestTime:
                    shortestTime = int(traject[1])

                    # Ensure route doesn't pass the maximum timeframe.
                    if time + shortestTime <= maxTime:
                        shortestConnection = traject[0]

        # Ensure there is a new connection added.
        if shortestConnection != None:

            # Choose the next station.
            return Greedy(graph, shortestConnection, maxTime, allConnections, route, time + shortestTime)

    return route, time

def bestBeginStation(allConnections, allStations):
    """Function which picks the best next beginstation for greedy.
    The best beginstation has as preference to have the least amount
    of critical connection, where number of critical connections %2 == 1.
    It also wants the shortest one."""

    criticalDestinations = None
    nonCriticalDestinations = None
    bestBeginStation = None

    for station in allStations:

        # Keep track of local critical- and non-critical connections
        myCriticalDestinations = []
        myNonCriticalDestinations = []
        for destination in allStations[station].destinations:
            for connection in allConnections:

                # Check if connection is still available.
                if [station, destination.name] == connection[0] or [destination.name, station] == connection[0]:

                    # Check if connection is critical.
                    if allStations[station].isCritical or destination.isCritical:
                        myCriticalDestinations.append(connection)
                    else:
                        myNonCriticalDestinations.append(connection)
                    break

        # Check if station is the best beginstation.
        if bestBeginStation == None:
            bestBeginStation = station
            criticalDestinations = myCriticalDestinations
            nonCriticalDestinations = myNonCriticalDestinations

        # Preference is the least amount of critical connections, where that
        # number % 2 == 1.
        elif len(myCriticalDestinations) % 2 == 1:
            if len(criticalDestinations) % 2 == 1:
                if len(myCriticalDestinations) < len(criticalDestinations):
                    bestBeginStation = station
                    criticalDestinations = myCriticalDestinations
                    nonCriticalDestinations = myNonCriticalDestinations

                # The shortest time is preferred.
                elif len(myCriticalDestinations) == len(criticalDestinations):
                    minimumTime = None
                    for connection in criticalDestinations:
                        if minimumTime == None or connection[1] < minimumTime:
                            minimumTime = connection[1]
                    myMinimumTime = None
                    for connection in myCriticalDestinations:
                        if myMinimumTime == None or connection[1] < myMinimumTime:
                            myMinimumTime = connection[1]
                    if myMinimumTime < minimumTime:
                        bestBeginStation = station
                        criticalDestinations = myCriticalDestinations
                        nonCriticalDestinations = myNonCriticalDestinations
            else:
                bestBeginStation = station
                criticalDestinations = myCriticalDestinations
                nonCriticalDestinations = myNonCriticalDestinations

        # After that, preference is to have the least amount of critical
        # connections.
        elif len(criticalDestinations) % 2 == 0:
            if len(myCriticalDestinations) < len(criticalDestinations):
                bestBeginStation = station
                criticalDestinations = myCriticalDestinations
                nonCriticalDestinations = myNonCriticalDestinations

            # Shortest time is preferred.
            elif len(myCriticalDestinations) == len(criticalDestinations):
                minimumTime = None
                for connection in criticalDestinations:
                    if minimumTime == None or connection[1] < minimumTime:
                        minimumTime = connection[1]
                myMinimumTime = None
                for connection in myCriticalDestinations:
                    if myMinimumTime == None or connection[1] < myMinimumTime:
                        myMinimumTime = connection[1]
                if myMinimumTime != None and myMinimumTime < minimumTime:
                    bestBeginStation = station
                    criticalDestinations = myCriticalDestinations
                    nonCriticalDestinations = myNonCriticalDestinations

    return bestBeginStation


def algorithmGreedy(graph, maxDepth, maxTime):
    """Greedy algorithm which chooses a 'best begin station', then calculates
    the most optimal route for this station. Then starts over again with a new
    beginstation, until it has it's maximum number of station. It keeps track of
    which connections it has passed already."""

    allConnections = copy.copy(graph.allConnections)
    allStations = copy.copy(graph.allStations)

    pathsSelected = []
    for i in range(maxDepth):

        # Calculate best begin station.
        beginStation = bestBeginStation(allConnections, allStations)

        # You have to give an empty list, otherwise it doesn't work.
        route, time = Greedy(graph, beginStation, maxTime, allConnections, [])

        # Remove connections which has been passed.
        connectionsToRemove = []
        for i in range(len(route) - 1):
            for connection in allConnections:
                if [route[i], route[i+1]] == connection[0] or [route[i+1], route[i]] == connection[0]:
                    connectionsToRemove.append(connection)
        for connection in connectionsToRemove:
            allConnections.remove(connection)

        # Add new trajectory to list of trajectories.
        pathsSelected.append([route, time])

    return pathsSelected
