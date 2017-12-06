import csv
import matplotlib.pyplot as plt

def makeGraph(file_name, fig_name):
    plot = []
    plot_file = open(file_name, 'rt')
    data = csv.reader(plot_file)
    for item in data:
        plot.append(float(item[0]))

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    plt.sub_plot(plot)
    plt.ylabel("Score")
    plt.savefig(fig_name)
