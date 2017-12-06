import csv
import matplotlib.pyplot as plt

def makeGraph(file_name, fig_name):
    plot = []
    plot_file = open(file_name, 'rt')
    data = csv.reader(plot_file)
    for item in data:
        plot.append(float(item[0]))

    plt.plot(plot)
    plt.ylabel("Score")
    plt.savefig(fig_name)
