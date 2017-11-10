#!/usr/bin/env python3

import sys
import csv
import os

class Station:
    """Station with name, coordinates, destinations and if it is critic"""

    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates
        self.destinations = {}
        self.critic = False
        self.visited = False

    # Function to add a destination to the station.
    def add_destination(self, destination, time):
        self.destinations[destination] = time

# List to store stations.
stations = {}
stationsfile = open('StationsHolland.csv', 'rt')
reader2 = csv.reader(stationsfile)
for row in reader2:
    stations[row[0]] = Station(row[0], [row[1], row[2]])
    if row[3] == 'Kritiek':
        stations[row[0]].isCritic()
stationsfile.close()


# Add connections to the stations.
connecties = open('ConnectiesHolland.csv', 'rt')
reader = csv.reader(connecties)
for row in reader:
    stations[row[0]].add_destination(row[1], row[2])
    stations[row[1]].add_destination(row[0], row[2])
connecties.close()

# traject = []
# for i in range(7):
#     print('traject[{}]'.format(i))
#     time = 0
#     traject.append([])
#     while True:
#         plaats = input("Station: ")
#         if plaats == 'end':
#             print('End')
#             break
#         if stations[plaats]:
#             if traject[i] != []:
#                 time += int(stations[plaats].destinations[parent])
#                 if time > 120:
#                     print('Out of time')
#                     break
#             traject[i].append(stations[plaats].name)
#             stations[plaats].isVisited()
#             parent = plaats
#             print(stations[plaats].destinations)
#     print(traject[i])