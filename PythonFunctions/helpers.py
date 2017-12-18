import copy
import os

def CalculateScore(trajectories, criticalConnections):
    """Function to compute the score."""

    # Keep track of number of minutes, trains and critical connections.
    minutes = 0
    trains = len(trajectories)
    critical_connection = 0
    critical_connections_past = []

    # Iterate over each trajectory in trajectories.
    for trajectory in trajectories:

        # Add number of minutes to total.
        minutes += int(trajectory[1])

        # Iterate over ech station in trajectory.
        stations = trajectory[0]
        for i in range(len(stations) - 1):
            this_station = stations[i]
            next_station = stations[i + 1]

            # Check if connection is critical and if so, if the connection was not yet used.
            if [this_station, next_station] in criticalConnections or [next_station, this_station] in criticalConnections:
                if [this_station, next_station] not in critical_connections_past and [next_station, this_station] not in critical_connections_past:
                    critical_connections_past.append([this_station, next_station])
                    critical_connection += 1

    # Calculate the percentage of critical connections used.
    percentage = critical_connection/len(criticalConnections) * 100

    # Calculate the total score.
    score = percentage*100 - (trains*20 + minutes/100000)
    return score
