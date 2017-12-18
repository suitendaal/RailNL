# RailNL
This case is about the line manegement of intercity trains. In other words, in a given time we have to give a number of trajectories, which is as efficient as possible. Een trajectory is a route of connections between stations. Trajectories can not be longer than 120 minutes for the North- and South-Holland case.
For the entire Netherlands, this timeframe is 180 minutes.

For the first part We are going to take a look at the 22 most important intercity stations in North- and South-Holland.
The second part will be the entire netherlands with the 61 most important intercity stations.
The connections between stations and the travel time between the stations are given in csv files wich are in the csvFiles directory.
Some stations are critical. A critical connection is a connection between two stations of which at least one is a critical station.
With our score function, the trajectories get more efficient with more critical connections.

We have been working on a line management for both North- and South-Holland and the entire Netherlands.
For the first case, we have a maximum of 7 trajectories within a time frame of 120 minutes, in which as many critical connections as
possible are passed.
For the second case, we have a maximum of 20 trajectories within a time frame of 180 minutes, in which as many critical connections
as possible are passed.
To measure the efficiency of a line manegement, we keep track of a certain score, calculated as follows:
S = p\*10000 - (t\*20 + min/100000)
Where S is the score, p the percentage of passed critical connections devided by 100, t the number of trains and min the total time
of the line management. This scorefunction has a upper and lower bound.

For the first case the lower bound is -140.00094, based on 7 trains, no critical connections and so 94 minutes.
The upper bound is 9939.99713, based on the idea that all critical stations are connected, the total of minutes equal to 287 and 3
trains.
We calculated the statespace equal to 5 \* 10\^19. This number comes from 2223 (the total possible trajectories) choose 7. To
 implement these in brute force is unreal. It would take to much time, so we use some pruning. For instance, we pruned to prevent to
  get unnessecary overlapping trajectories.

For the second case the lower bound is -400.0054, based on 20 trajectories, no critical connections and so 540 minutes.
The upper bound is 9879.9946, based on the idea that all ceritical stations are connected, the total of minutes equal to 1011 and so on 6 trains.
We calculated the statespace equal to 1.16 \* 10\^97. This number comes from 592258 (the total possible trajectories) choose 22. To implement these in brute force is unreal. It would take to much time, so we use some pruning. For instance, we pruned to prevent to get unnessecary overlapping trajectories.

## Getting Started
The program can be run by using the command "python main.py".  The program will first ask you which part of the Netherlands to use.
The program will then ask you which algorithm you want to use. There are four options: Simulated Annealing, Hillclimber, Depth
First and Dijkstra's Algorithm. The algorithms Simulated Annealing and Hillclimber can be run with either a combination of the best
scored trajects or a combination from Sven's algorithm. The depth first algorithm can be run with a combination of the best scored trajects or with Dijkstra's algorithm. Each algorithm produces a picture of the choosen paths.

### Prerequisites
* **matplotlib 2.1.0**
* **os 16.1**
* **sys 29.1**
* **csv 14.1**
* **random 9.6**
* **networkx 2.0**
* **re 6.2**
* **numpy 1.14.1**

## Versioning
* **Atom 1.22.1**
* **GitHub**
* **Python 3.6.4**

## Authors
* **Sven Uitendaal**
* **Britt van Leeuwen**
* **Susanne Binkhorst**

# Acknowledgment
We would like to thank our Tech Assist Bart van Baal for helping us througout this project.
