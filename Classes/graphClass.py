import csv
from Classes.stationClass import Station
import networkx as nx
import matplotlib.pyplot as plt
from PythonFunctions.helpers import CalculateScore
import re
import os

class Graph(object):
    """Graph with station with locations, destinations and some functions."""
    def __init__(self):
        self.graph = {}
        self.allRoutes = []
        self.allStations = {}
        self.allConnections = []
        self.criticalConnections = []
        self.stationNames = []


    def load_data(self, stationsCsvFile, connectiesCsvFile, allCritical = False):
        """Function to load stations and connections into the graph."""

        # File with railwaystations and coordinates.
        stationsfile = open(stationsCsvFile, 'rt')
        stations = csv.reader(stationsfile)
        for station in stations:

            # Add railwaystation to allStations.
            self.stationNames.append(station[0])
            if allCritical:
                newStation = Station(station[0], float(station[1]), float(station[2]), 'Kritiek')
            else:
                newStation = Station(station[0], float(station[1]), float(station[2]), station[3])
            self.allStations[station[0]] = newStation
            self.graph[station[0]] = []

        stationsfile.close()

        # File with connections between stations.
        connecties = open(connectiesCsvFile, 'rt')
        directions = csv.reader(connecties)

        # Add connections to the object.
        for direction in directions:

            # Add connection to allConnections.
            self.allConnections.append([[direction[0], direction[1]], int(float(direction[2]))])

            # Add direction to the graph.
            self.graph[direction[0]].append([direction[1], int(float(direction[2]))])
            self.graph[direction[1]].append([direction[0], int(float(direction[2]))])

            self.allStations[direction[0]].addDestination(self.allStations[direction[1]])
            self.allStations[direction[1]].addDestination(self.allStations[direction[0]])

            if self.allStations[direction[0]].isCritical or self.allStations[direction[1]].isCritical:
                self.criticalConnections.append([direction[0], direction[1]])

        connecties.close()


    def makeAllRoutes(self, minutes):
        """Function to make all possible routes in a timescheme."""
        allNewRoutes = []
        for i in range(len(self.allStations)):
            for j in range(i + 1, len(self.stationNames)):

                # Put all routes in a list with corresponding time.
                allNewRoutes.extend(self.addPaths(self.stationNames[i], self.stationNames[j], minutes))
        self.allRoutes = allNewRoutes


    def addPaths(self, start, end, minutes, route=[], time=0):
        """Function to get all routes between two stations, within 2 hours."""

        # Add start to route.
        route = route + [start]

        # At the end, return the route.
        if start == end:
            return [[route, time]]

        # If the route doesn't exist, return nothing.
        elif not self.graph[start]:
            return []
        routes = []

        # Check the route for every destination.
        for destination in self.graph[start]:

            # Do not pass the same station twice.
            if destination[0] not in route:

                # Ensure the route doesn't take longer than the given timeframe.
                duration = time + int(float(destination[1]))
                if duration < minutes:

                    # Make the new routes for the further stations.
                    new_routes = self.addPaths(destination[0], end, minutes, route, duration)
                    for new_route in new_routes:
                        routes.append(new_route)
        return routes


    def ScorePathsPruning(self, n):
        """Function to determine the best n trajectories based on the score."""
        bestpaths = []
        bestscores = []
        connections_made = []

        # Add path, calculate score and keep track of the best score and trajectories.
        for path in self.allRoutes:
            score = CalculateScore([path], self.criticalConnections)
            if bestscores == [] or min(bestscores) < score:

                # If the begin or the end of a path is already chosen in another trajectory, do not choose that path.
                if (len(bestpaths) < n) and (([path[0], path[1]]) not in connections_made) and (([path[-2], path[-1]]) not in connections_made):
                        bestpaths.append(path)
                        bestscores.append(score)
                        for i in range(len(path)-1):
                            if [path[i], path[i+1]] not in connections_made:
                                connections_made.append([[path[i], path[i+1]]])

                else:
                    index = bestscores.index(min(bestscores))
                    bestpaths[index] = path
                    bestscores[index] = score

        return bestpaths, bestscores

    def draw(self):
        """Function to draw the graph"""

        # Make new graph.
        G = nx.Graph()

        # Initiate dictionaries and lists for labels and colors.
        labels = {}
        node_labels = {}
        node_color = []

        # Add node, make node blue if station is non critical and red if station
        # is critical.
        for station in self.allStations:
            thisStation = self.allStations[station]
            if thisStation.isCritical == True:
                node_color.append("r")
            else:
                node_color.append("b")
            G.add_node("" + thisStation.name, pos = (thisStation.latitude, thisStation.longitude))

            # Add abbreviation of station name as label for node.
            name = re.split('\s|-|/', thisStation.name)
            afk = ""
            for word in name:
                afk += word[0]
            node_labels[thisStation.name] = afk

        # Add edge for every connection, make edge blue if neither of the stations
        # is critical and red if at least one of them is critical.
        # Add the time between the stations as a label for the edge.
        for connection in self.allConnections:
            if [connection[0][0], connection[0][1]] in self.criticalConnections or [connection[0][1], connection[0][0]] in self.criticalConnections:
                G.add_edge("" + connection[0][0], "" + connection[0][1], color = 'r')
            else:
                G.add_edge("" + connection[0][0], "" + connection[0][1], color = 'b')
            labels.update({(connection[0][0], connection[0][1]): int(connection[1])})

        edges = G.edges()
        edge_color = [G[u][v]['color'] for u,v in edges]

        # Change position of node label.
        pos = nx.get_node_attributes(G,'pos')
        pos_higher = {}
        y_off = 0.03
        x_off = 0.01

        for k, v in pos.items():
            pos_higher[k] = (v[0]+x_off, v[1]+y_off)

        # Plot the figure and save it in Results.
        plt.figure(1, figsize = (10,10))
        nx.draw(G, pos, node_color=node_color, edge_color = edge_color, node_size=70)
        nx.draw_networkx_edge_labels(G, pos, labels)
        nx.draw_networkx_labels(G, pos_higher, node_labels)
        plt.savefig(os.path.join('Results', "Graph.png"))
