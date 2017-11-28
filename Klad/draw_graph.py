import networkx as nx
import matplotlib.pyplot as plt
import csv

G = nx.Graph()
labels = {}
stationsCsvFile = 'C:/Users/Susanne/RailNL/csvFiles/StationsHolland.csv'
stationsfile = open(stationsCsvFile, 'rt')
stations = csv.reader(stationsfile)
for station in stations:
    G.add_node("" + station[0], pos = (float(station[2]), float(station[1])))


connectiesCsvFile = 'C:/Users/Susanne/RailNL/csvFiles/ConnectiesHolland.csv'
connecties = open(connectiesCsvFile, 'rt')
directions = csv.reader(connecties)
for direction in directions:
    G.add_edge(""+direction[0], ""+direction[1])
    labels.update({(direction[0],direction[1]) : int(direction[2])})
print(labels)

pos=nx.get_node_attributes(G,'pos')
plt.figure(1, figsize = (10,10))
nx.draw(G, pos, with_labels = True, node_size=70, font_size=9, label_pos=3)
nx.draw_networkx_edge_labels(G, pos, labels, alpha = 0.5)
plt.savefig("plot.png")
#plt.show()
