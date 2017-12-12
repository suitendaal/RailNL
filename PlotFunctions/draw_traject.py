import networkx as nx
import matplotlib.pyplot as plt
import csv
import re
import os

def drawTraject(graph, trajecten):
    # Make new graph
    G = nx.Graph()

    # Initiate dictionaries and lists for labels and colors
    node_labels = {}
    node_color = []
    critical=[]

    # Load the nodes
    for traject in trajecten:
        for station in traject[0]:

            if station not in G.nodes():
                obj_station = graph.allStations[station]
                lon = obj_station.longitude
                lat = obj_station.latitude

                if obj_station.isCritical:
                    node_color.append("r")
                else:
                    node_color.append("k")

                G.add_node("" + station, pos = (float(lat), float(lon)))

                # Node labels with abbreviation of the station names
                name = re.split('\s|-|/', station)
                afk = ""
                for i in name:
                    afk = afk + i[0]
                node_labels[station] = afk

    colors = ["k", "b", "g", "y", "m", "r", "#ff69b4"]
    for i in range(len(trajecten)):
        colour = colors[i]
        for j in range(len(trajecten[i][0])-1):
            if (""+trajecten[i][0][j], "" + trajecten[i][0][j+1]) and (""+trajecten[i][0][j+1], "" + trajecten[i][0][j]) not in G.edges():
                G.add_edge(""+trajecten[i][0][j], "" + trajecten[i][0][j+1], color = colour)

    edges = G.edges()
    edge_color = [G[u][v]['color'] for u,v in edges]

    pos=nx.get_node_attributes(G,'pos')
    pos_higher = {}
    y_off = 0.03  # offset on the y axis
    x_off = 0.01
    for k, v in pos.items():
        pos_higher[""+k] = (v[0]+x_off, v[1]+y_off)

    plt.figure(1, figsize = (10,10))
    nx.draw(G, pos, node_color=node_color, edge_color = edge_color, node_size=70)
    nx.draw_networkx_labels(G, pos_higher, node_labels)
    plt.savefig(os.path.join('results', "plot_traject.png"))
