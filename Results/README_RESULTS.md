# Results of experimentation with algoritms

Wij hebben met deze case geexperimenteerd op verschillende manieren.
Het veranderen van het aantal iteraties of het veranderen van de sacorefunctie zijn hier voorbeelden van.

# Depth first experiments

With the depth first algoritm we implemented different algoritms to get the best N paths to choose from. This number N has also been changed to check if the results were different.

We choose N equal to 20, because we want as much trajectories as possible, but also want the algoritm to solve the case in a certain time.

In the DepthFirst_sven file, the results of the depth first algoritm with sven's algoritm is shown. Here we stopped the algoritm after the best score of a combination of 4 trajectories. If we would choose more than 4 trajectories the score could not become better, because of the upperbound of the scorefunction.

If we choose the bestScorealgoritm, the algoritm gets a lot faster, but the score will become really low. This results are shown in the DepthFirst_bestscore.

Also, we used pruning with the depthfirst algoritm. This made the function a lot faster. This pruning makes sure that trajectories do not overlap when unnecessary.

