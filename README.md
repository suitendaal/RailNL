# RailNL
This case is about the line manegement of intercity trains. In other words, in a given time we have to give a number of trajectories, which is as efficient as possible. Een trajectory is a route of connections between stations. Trajectories can not be longer than 120 minutes for the North- and South-Holland case.
For the entire Netherlands, this timeframe is 180 minutes.

For the first part We are going to take a look at the 22 most important intercity stations in North- and South-Holland.
The second part will be the entire netherlands (the 61 most important intercity stations).
The connections between stations are given in csv files.
Some stations are critical. A critical connection is a connection between 2 stations of which at least one is a critical station.
With our score function, the trajectories get more efficient with more critical connections.

## Getting Started
The program can be run by using the command "python main.py".  The program will first ask you which part of the Netherlands to use (not yet).
The program will then ask you which algorithm you want to use. There are four options: Simulated Annealing, Hillclimber, Depth
First and Dijkstra's Algorithm. The algorithms Simulated Annealing and Hillclimber can be run with either a combination of the best
scored trajects or a combination from Sven's algorithm. Each algorithm produces a picture of the choosen paths.

### Prerequisites

### Installing

## Experimeting
We already looked in to Dijkstra's algorithm, Simulated Annealing, Hillclimber and depth first.
The Simualated Annealing algoritm can be iterated over a certain number of times. We tried a few different number of iterations.
When we use 1 iteration, the score is relatively low (as example 899859.99574). While, when we use 500 or more iterations, we get a
score almost always around 999859,9.

The Hillclimber is being iterated over 200 times. Our best score so far is 999859,99593.
We also made functions to draw the trajects we choose and the complete graph. We want to begin to work with the stations of the
entire Netherlands a.s.a.p.

## Versioning
* **Atom 1.22.1**
* **GitHub**
* **python 3**

## Authors
* **Sven Uitendaal**
* **Britt van Leeuwen**
* **Susanne Binkhorst**

# Acknowledgment

We have been working on a line management for both North- and South-Holland and the entire Netherlands.
For the first case, we have a maximum of 7 trajectories within a time frame of 120 minutes, in which as many critical connections as possible are passed.
For the second case, we have a maximum of 20 trajectories within a time frame of 180 minutes, in which as many critical connections as possible are passed.
To measure the efficiency of a line manegement, we keep track of a certain score, calculated as follows:
S = p\*10000 - (t\*20 + min/100000)
Where S is the score, p the percentage of passed critical connections, t the number of trains and min the minutes it takes the line manegement to be used.

This scorefunction has a upper and lower bound.
For the first case the lower bound is -140.00094, based on 7 trajectories, no critical connections and so 94 minutes.
The upper bound is 999939.99713, based on the idea that all ceritical stations are connected, the total of minutes equal to 287 and so 3

We calculated the statespace equal to 5 \* 10\^19. This number comes from 2223 (the total possible trajectories choose 7). To implement these in brute force is unreal. It would take to much time, so we use some pruning. For instance, we pruned to prevent to get unnessecary overlapping trajectories.
