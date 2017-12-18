import csv
import matplotlib.pyplot as plt
import numpy as np
import os

def main():

    file_name = input("Please enter the file you want to plot: ")
    fig_name = input("Please enter to which png file you want to save you plot: ")

    # Create Figure and Axes instances
    fig,ax = plt.subplots(1)

    plot = np.genfromtxt(os.path.join('Results', file_name))
    x = np.arange(0, len(plot))

    # Make your plot, set your axes labels
    ax.plot(x,plot,'k')
    ax.set_ylabel('Score')
    ax.set_xlabel('Iterations')
    plt.savefig(os.path.join('Results', fig_name))
    plt.show()

if __name__ == '__main__':
    main()
