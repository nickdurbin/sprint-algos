#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) The number of times the equation is run is dependent on what n is. For instance, our while loop would run 2x if n = 2. If n = 3, then the loop runs 3 times. This makes me believe that the equation is linear. The amount of times the equation runs is dependent on the input of n. My best guess is O(n). When looking at it initially, I thought O(n^3).

b) My initial thought is nested loops, which Artem said would be a giveaway for polynomial time or O(n^2). We would need to go through both loops in order to complete an iteration.

c) We are using recursion in this function. This to me seems like it would then be O(n). The input of bunnies would then determine the iterations of this function.

## Exercise II

If the determining factor on this equation is the total amount of eggs dropped + how many are broken, then I believe the best approach would be a binary search.

We could take the len(arr) // 2 to find our middle position. This will give us the opportunity to have the lowest possible number and iterations, which best case scenario would be 2 and our final number of the equation as 2 dropped + 1 broken egg = 3.

If we land on our target of f, then we would still need to run a second iteration upward to verify we have found our target value.

The run time complexity of a binary search is O(log n). The reason is because our size would decrease with each iteration. The first obviously would more than likely elminate half the possibilities. If the egg breaks, then we eliminate our ceiling and the middle becomes our new ceiling as we move downward in floors.

The opposite is true if the egg does not break. Meaning, we would make the floor our new middle position and move upward.

However, if the only number that was significant in the equation was broken eggs, then an iterative approach would be best. This would allow for only 1 broken egg guaranteed. This approach would be O(n).
