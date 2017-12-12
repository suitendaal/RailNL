import csv
import matplotlib.pyplot as plt
import numpy as np
import os

def makeGraph(file_name, fig_name):
    plot = []
    with open(file_name) as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            plot.append(float(row[0]))

    x = np.arange(0, len(plot))
    plt.plot(x, plot)
    plt.ylabel("Score")
    plt.savefig(fig_name)
