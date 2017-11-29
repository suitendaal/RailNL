import csv
from Classes.stationClass import Station
import networkx as nx
import matplotlib.pyplot as plt
import re
import os

class Graph(object):
    """Graph with station with locations, destinations and some functions"""
    def __init__(self):
        self.graph = {}
        self.allRoutes = []
        self.allStations = []
        self.criticalStations = []
        self.allConnections = []
        self.criticalConnections = []
        self.coordinates = {}


    def load_data(self, stationsCsvFile, connectiesCsvFile):
        """Function to load stations and connections into the graph"""

        # File with railwaystations and coordinates
        stationsfile = open(stationsCsvFile, 'rt')
        stations = csv.reader(stationsfile)
        for station in stations:

            # Add railwaystation to allStations
            newStation = Station(station[0], station[1], station[2], station[3])
            self.allStations.append(newStation)
            self.graph[station[0]] = []
            self.coordinates[station[0]] = [station[2], station[1]]

            # Add critical railwaystations to criticalStations
            if station[3] == 'Kritiek':
                self.criticalStations.append(station[0])
        stationsfile.close()

        connecties = open(connectiesCsvFile, 'rt')
        directions = csv.reader(connecties)
        for direction in directions:
            self.allConnections.append([direction[0], direction[1]])
            self.graph[direction[0]].append([direction[1], direction[2]])
            self.graph[direction[1]].append([direction[0], direction[2]])
            if direction[0] in self.criticalStations or direction[1] in self.criticalStations:
                self.criticalConnections.append([direction[0], direction[1]])
        connecties.close()

    def makeAllRoutes(self):
        allNewRoutes = []
        for i in range(len(self.allStations)):
            for j in range(i + 1, len(self.allStations)):
                allNewRoutes.extend(self.addPaths(self.allStations[i].name, self.allStations[j].name))
        self.allRoutes = allNewRoutes

    def addPaths(self, start, end, route=[], time=0):
        """Function to get all routes between to stations, within 2 hours"""

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
                # Ensure the route doesn't take longer than 2 hours.
                duration = time + int(destination[1])
                if duration < 120:
                    # Make the new routes for the further stations.
                    new_routes = self.addPaths(destination[0], end, route, duration)
                    for new_route in new_routes:
                        routes.append(new_route)
        return routes

    def draw(self):

        # Make new graph
        G = nx.Graph()

        # Initiate dictionaries and lists for labels and colors
        labels = {}
        node_labels = {}
        node_color = []

        for station in self.allStations:
            if station.isCritical == True:
                node_color.append("r")
            else:
                node_color.append("b")
            G.add_node("" + station.name, pos = (station.aLatitude, station.aLongitude)
            name = re.split('\s|-|/', station.name)
            afk = ""
            for word in name:
                afk += word[0]
            node_labels[station.name] = afk

        for connections in self.allConnections:
            if connection[0] in self.criticalConnections:
                G.add_edge("" + connection[0][0], "" + connection[0][1], color = 'r')
            else:
                G.add_edge("" + connection[0][0], "" + connection[0][1], color = 'b')
            labels.update({(connection[0][0], connection[0][1]): int(connection[1])})

        edges = G.edges()
        edge_color = [G[u][v]['color'] for u,v in edges]

        pos=nx.get_node_attributes(G,'pos')
        pos_higher = {}
        y_off = 0.03  # offset on the y axis
        x_off = 0.01

        for k, v in pos.items():
            pos_higher[k] = (v[0]+x_off, v[1]+y_off)

        plt.figure(1, figsize = (10,10))
        nx.draw(G, pos, node_color=node_color, edge_color = edge_color, node_size=70)
        nx.draw_networkx_edge_labels(G, pos, labels)
        nx.draw_networkx_labels(G, pos_higher, node_labels)
        plt.savefig("plot.png")
        plt.show()
