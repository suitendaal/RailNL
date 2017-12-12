import csv
import matplotlib.pyplot as plt
import numpy as np
import os

def makeGraph(file_name, fig_name):
    # Create Figure and Axes instances
    fig,ax = plt.subplots(1)

    plot = np.genfromtxt(file_name)
    x = np.arange(0, len(plot))

    # Make your plot, set your axes labels
    ax.plot(x,plot,'k')
    ax.set_ylabel('V')
    ax.set_xlabel('t')

    plt.show()

    # plt.plot(x, plot)
    # plt.ylabel("Score")
