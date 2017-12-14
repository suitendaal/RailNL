# Results of experimentation with algoritms

We experimented in this case with different parameters.
Changing the number of iterations and changing the scorefunction are examples of this.

# Depth first experiments

With the depth first algoritm we implemented different algoritms to get the best N paths to choose from. This number N has also been changed to check if the results were different.

We choose N equal to 20, because we want as much trajectories as possible, but also want the algoritm to solve the case in a certain time.

If we combine this algoritm with dijkstra, we can stop the algoritm after the best score of a combination of 4 trajectories. If we would choose more than 4 trajectories the score could not become better, because of the upperbound of the scorefunction.

If we choose the bestScorealgoritm, the algoritm gets a lot faster, but the score will become really low. This results are shown in the DepthFirst_bestscore.

Also, we used pruning with the depthfirst algoritm. This made the function a lot faster. This pruning makes sure that trajectories do not overlap when unnecessary.

if (int(algorithm) == 5):
      drawTraject(graph, [[['Alkmaar', 'Hoorn', 'Zaandam', 'Beverwijk', 'Haarlem', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel'], 116], [['Den Haag Centraal', 'Gouda', 'Rotterdam Alexander', 'Rotterdam Centraal', 'Dordrecht'], 53], [['Den Helder', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Haarlem', 'Heemstede-Aerdenhout', 'Leiden Centraal'], 93], [['Gouda', 'Alphen a/d Rijn', 'Leiden Centraal', 'Den Haag Centraal', 'Delft', 'Schiedam Centrum', 'Rotterdam Centraal'], 70]])
