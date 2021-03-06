import networkx as nx
import matplotlib.pyplot as plt
import csv
import re
import os

def drawTraject(graph, trajecten, figName):
    # Make new graph.
    G = nx.Graph()

    # Initiate dictionaries and lists for labels and colors.
    node_labels = {}
    node_color = []
    critical=[]

    # Load the nodes.
    for traject in trajecten:
        for station in traject[0]:

            # If node of station is not yet added, add the node.
            if station not in G.nodes():
                obj_station = graph.allStations[station]
                lon = obj_station.longitude
                lat = obj_station.latitude

                # Make node red if station is critical and blue if non critical.
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


    colors = ["k", "b", "g", "y", "m", "r", "#ff69b4", "#fa8072", "#00ee76", "#7d26cd", "#8b0000", "#cd96cd", "#187867", "#78186a", "#777818", "#337818", "#172131", "#c14d4d", "#376037", "#375f60", "#5d6300", "#176300"]
    # Add the edge for every connection if edge not yet added.
    # Give an edge a new color for every new traject, choose from colors.
    for i in range(len(trajecten)):
        stations = trajecten[i][0]
        colour = colors[i]
        for j in range(len(stations)-1):
            this_station = trajecten[i][0][j]
            next_station = trajecten[i][0][j+1]
            if (""+this_station, "" + next_station) and (""+next_station, "" + this_station) not in G.edges():
                G.add_edge(""+this_station, "" + next_station, color = colour)

    edges = G.edges()
    edge_color = [G[u][v]['color'] for u,v in edges]

    # Change the position of the node labels.
    pos=nx.get_node_attributes(G,'pos')
    pos_higher = {}
    y_off = 0.03
    x_off = 0.01
    for k, v in pos.items():
        pos_higher[""+k] = (v[0]+x_off, v[1]+y_off)

    # Plot the graph and save to the given filename.
    fig,ax = plt.subplots(1, figsize = (10,10))
    nx.draw(G, pos, node_color=node_color, edge_color = edge_color, node_size=70)
    nx.draw_networkx_labels(G, pos_higher, node_labels)
    plt.savefig(figName)
