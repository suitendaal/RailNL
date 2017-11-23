import csv

class Station(object):
    """Station with name, coordinates, destinations and if it is critic"""

    def __init__(self, name, coordinates):

        # Name of the station.
        self.name = name

        # Coordinates of the station.
        self.coordinates = coordinates

        # Destinations from the station.
        self.destinations = []

        # If the station is critic.
        self.critic = False

        # For the 7 trajecten, if the station is visited.
        self.visited = False

    # Function to add a destination to the station.
    def add_destination(self, destination, time):
        self.destinations.append([destination, time])



# def make_children(self, station):
#     new_station = Station(station[0], root)
#     for destination in reader:
#         if new_station.name == destination[0]:
#             new_station.destinations[destination[1]] = Station(destination[1], new_station.name)
#         elif new_station.name == destination[1]:
#             new_station.destinations[destination[0],] = Station(destination[0], new_station.name)
#         self.name = new_station.name
#         time += new_station.destination[]
#         if new_station.name = root:
#             endoftraject = True
#         elif time > 120
#             endoftraject = True
#         elif not visited
#             make_children()


""""Store stations"""
stations = {}
stationsfile = open('StationsHolland.csv', 'rt')
reader2 = csv.reader(stationsfile)

# Add every station to list, consists of a station and a traject.
"""Niet meer naar kijken, neem gewoon aan dat het klopt"""
for row in reader2:
    station = Station(row[0], [row[1], row[2]])
    if row[3] == 'Kritiek':
        station.critic = True
    new_station = {'station': station, 'traject':[]}
    stations[station.name] = new_station
    # Gebruiksaanwijzing: stations['Alphen aan den Rijn']['station'].destinations geeft de destinations van Alphen aan den Rijn
    # stations['kies station']['kies 'station' of 'traject'][''station' gekozen? kies uit '.name', '.coordinates', '.destinations', '.critic' of '.visited'']
stationsfile.close()
print(stations)


"""Add destinations"""
connecties = open('ConnectiesHolland.csv', 'rt')
reader = csv.reader(connecties)
for row in reader:
    stations[row[0]]['station'].add_destination(row[1], row[2])
    stations[row[1]]['station'].add_destination(row[0], row[2])
connecties.close()

print(stations['Gouda']['station'].destinations)
#for station in stations:

    # make_children(station)
