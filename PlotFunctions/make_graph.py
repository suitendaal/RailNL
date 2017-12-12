import csv
import matplotlib.pyplot as plt
import numpy as np
import os

def makeGraph(file_name, fig_name):
    plot = np.genfromtxt(file_name)

    x = np.arange(0, len(plot))
    plt.plot(x, plot)
    # plt.ylabel("Score")
    plt.savefig(fig_name)
