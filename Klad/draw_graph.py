import networkx as nx
import matplotlib.pyplot as plt
import csv
import re

# Make new graph
G = nx.Graph()

# Initiate dictionaries and lists for labels and colors
labels = {}
node_labels = {}
node_color = []
critical=[]

# Load the nodes
stationsCsvFile = 'C:/Users/Susanne/RailNL/csvFiles/StationsHolland.csv'
stationsfile = open(stationsCsvFile, 'rt')
stations = csv.reader(stationsfile)
for station in stations:

    # Give critical nodes colour red and non-critical colour blue
    if station[3] == "Kritiek":
        node_color.append("r")
        critical.append(station[0])
    else:
        node_color.append("b")
    G.add_node("" + station[0], pos = (float(station[2]), float(station[1])))

    # Node labels with abbreviation of the station names
    name = station[0]
    name = re.split('\s|-|/', name)
    print(name)
    afk = ""
    for i in name:
        afk = afk + i[0]
    node_labels[station[0]] = afk

#node_labels["Heemstede-Aerdenhout"] = "H-A"


connectiesCsvFile = 'C:/Users/Susanne/RailNL/csvFiles/ConnectiesHolland.csv'
connecties = open(connectiesCsvFile, 'rt')
directions = csv.reader(connecties)
for direction in directions:
    if direction[0] in critical or direction[1] in critical:
        G.add_edge(""+direction[0], ""+direction[1], color = 'r')
    else:
        G.add_edge(""+direction[0], ""+direction[1], color = 'b')
    labels.update({(direction[0],direction[1]) : int(direction[2])})

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
