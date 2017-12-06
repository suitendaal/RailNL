import csv
import matplotlib.pyplot as plt
import numpy as np

def makeGraph(file_name, fig_name):
    plot = []
    with open(file_name) as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            plot.append(float(row[0]))
    print(len(plot))

<<<<<<< HEAD
    x = np.arange(0, len(plot))
    plt.plot(x, plot)
=======
    plt.plot(plot)
>>>>>>> 108ef022af7b8e58a58ba619c80589b8695fb520
    plt.ylabel("Score")
    plt.savefig(fig_name)
