# Results of experimentation with algorithms

We looked in to Dijkstra's algorithm, Simulated Annealing, Hillclimber and depth first.
The Simualated Annealing algorithm can be iterated over a certain number of times. We tried a few different number of iterations.
When we use 1 iteration, the score is relatively low (as example 899859.99574). While, when we use 500 or more iterations, we get a
score almost always around 999859,9.

The Hillclimber is being iterated over 200 times. Our best score so far is 999859,99593.
We also made functions to draw the trajects we choose and the complete graph. We want to begin to work with the stations of the
entire Netherlands a.s.a.p.
We experimented in this case with different parameters.
Changing the number of iterations and changing the scorefunction are examples of this.

# Depth first experiments

With the depth first algorithm we implemented different algorithms to get the best N paths to choose from. This number N has also been changed to check if the results were different.

We choose N equal to 20, because we want as much trajectories as possible, but also want the algorithm to solve the case in a certain time.

If we combine this algorithm with dijkstra, we can stop the algorithm after the best score of a combination of 4 trajectories. If we would choose more than 4 trajectories the score could not become better, because of the upperbound of the scorefunction.

If we choose the bestScorealgorithm, the algorithm gets a lot faster, but the score will become really low. This results are shown in the DepthFirst_bestscore.

Also, we used pruning with the depthfirst algorithm. This made the function a lot faster. This pruning makes sure that trajectories do not overlap when unnecessary.

if (int(algorithm) == 5):
      drawTraject(graph, [[['Alkmaar', 'Hoorn', 'Zaandam', 'Beverwijk', 'Haarlem', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel'], 116], [['Den Haag Centraal', 'Gouda', 'Rotterdam Alexander', 'Rotterdam Centraal', 'Dordrecht'], 53], [['Den Helder', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Haarlem', 'Heemstede-Aerdenhout', 'Leiden Centraal'], 93], [['Gouda', 'Alphen a/d Rijn', 'Leiden Centraal', 'Den Haag Centraal', 'Delft', 'Schiedam Centrum', 'Rotterdam Centraal'], 70]])
