The first algorithm we used is depthfirst: Every traject is put in the scorefunction and the 20 best trajectories (with the pruning explained above) with the highest score are chosen. Then the score for every combination for these 20 trajectories is calculated and the one with the best score is chosen.

The second algorithm is a greedy algorithm: Beginstations are chosen according to the number of critical connections and the number of minutes the connection takes.

The third algorithm is a hillclimber: It takes a random combination of n trajectories and does this algorithm for n equal to 1 till the maximum of trajectories. The algorithm replaces every traject 1000 times with a random other trajectory and calculates the score. If the score is higher then the last best score, take that combination of trajectories and continue the algorithm from there.

The fourth algorithm is a hillclimber with simulated annealing: The idea is the same as a hillclimber, but the simulated annealing allows the function to become lower. This would help with getting out of a local maximum.
