import csv

class Connection:
    def __init__(self, begin, end, time):
        self.begin = begin
        self.end = end
        self.time = time


class Node(object):
    """Station with name, coordinates, destinations and if it is critic"""

    def __init__(self, station, coord1, coord2, critic):

        # Name of the station.
        self.station = station

        # Coordinates of the station.
        self.coord1 = coord1
        self.coord2 = coord2

        self.critic = critic

nodes = {}
connections = []

# Function to add a destination to the station.
def add_connection(connection):
    begin = connection[0]
    destination = connection[1]
    time = connection[2]
    new_connection = Connection(begin, destination, time)
    connections.append(new_connection)

def add_node(station):
    name = station[0]
    coordinates1 = station[1]
    coordinates2 = station[2]
    if station[3] == 'kritiek':
        critic = True
    else:
        critic =  False
    new_node = Node(name, coordinates1, coordinates2, critic)
    nodes[name] = new_node

""""Store stations"""
stationsfile = open('StationsHolland.csv', 'rt')
reader2 = csv.reader(stationsfile)
# Add every station to list, consists of a station and a traject.
for station in reader2:
    add_node(station)
stationsfile.close()


"""Add destinations"""
connecties = open('ConnectiesHolland.csv', 'rt')
reader = csv.reader(connecties)
for connection in reader:
    add_connection(connection)
connecties.close()





# im = Image.open("graph.pgm")
# draw = ImageDraw.Draw(im)

# def draw_graph():
#     for node in nodes:
#         draw.point([(node.coord1, node.coord2)])

#     for connection in connections:
#         beginloc1 = nodes[connection.begin].coord1
#         beginloc2 = nodes[connection.begin].coord2
#         endloc1 = nodes[connection.end].coord1
#         endloc2 = nodes[connection.end].coord2

#         draw.line([(beginloc1, beginloc2), (endloc1, endloc2)])
#     im.save(sys.stdout, "PNG")

# draw()






