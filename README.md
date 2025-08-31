Assignment 1: Wolf, Goat, and Cabbage Problem
Table of Contents
PEAS Analysis

The 5 Model Components

Results Tables

Analysis and Insights

Git Repository Link

Addendum: Raw Text Outputs

PEAS Analysis
The PEAS (Performance, Environment, Actuators, Sensors) framework is a way to formally define a rational agent's task. For the Wolf, Goat, and Cabbage problem, the agent is a search algorithm.

Performance: The measure of success for the agent. The goal is to move the farmer, wolf, goat, and cabbage across the river. The performance measure is based on finding a solution path with the minimum number of moves. This aligns with the notes' emphasis on "fewest possible moves."

Environment: The external world in which the agent operates. The environment consists of a river with two banks. The state of the environment is defined by the location of the farmer and the three items on either the start bank or the destination bank. The notes refer to this as the "State Space Problem" and depict a states diagram.

Actuators: The means by which the agent interacts with its environment. The actuators are the "movements" the farmer can make with the boat. The notes correctly list these as "move the farmer alone," "move the farmer with the Goat," "move the farmer with the Wolf," and "move the farmer with the Cabbage."

Sensors: The inputs the agent receives from the environment to determine its current state. The sensors in this abstract problem detect the location of each of the four items. The notes mention that sensors "will detect whether the actuators should or should not execute depending on if we make a bad move." This is an excellent way to think about how the state information is used to validate a transition.

The 5 Model Components
The state-space model provides a formal structure for the problem.

State: A state is a complete description of the world at any given time. For this problem, a state can be represented by a tuple of four binary values: (F,W,G,C), where F, W, G, and C represent the location of the farmer, wolf, goat, and cabbage, respectively. A value of 0 indicates the start bank, and 1 indicates the destination bank.

Initial State: The problem's starting point. The initial state is (0,0,0,0), representing all items on the start bank.

Actions: The set of all possible moves from a given state. The farmer can move across the river alone or with one of the three items. There are four possible actions from any given state.

Transition Model: A function that takes a state and an action as input and returns the resulting state. This model incorporates the problem's constraints, such as the rule that the goat and wolf cannot be left alone. A transition to an invalid state is not possible.

Goal Test: A function that checks if a given state is the goal state. The goal state is (1,1,1,1), where all items have successfully crossed to the destination bank.

Results Tables
This section presents the performance metrics for each algorithm and problem instance.

Metric

BFS (--domain wgc --algo bfs)

IDS (--domain wgc --algo ids)

Nodes Generated

10

25

Nodes Expanded

7

13

Maximum Frontier Size

3

3

Solution Depth

7

7

Solution Cost

7

7

Analysis and Insights
The results demonstrate the key differences in how BFS and IDS perform on a small, constrained problem like the Wolf, Goat, and Cabbage puzzle.

Nodes Generated and Expanded: BFS generated a total of 10 nodes and expanded 7 of them to find the solution. IDS, on the other hand, generated 25 nodes and expanded 13. The reason for this significant difference is that IDS performs a series of depth-limited searches. In each iteration, it re-explores nodes from previous iterations, leading to a much higher count of generated and expanded nodes. While BFS explores each node only once, IDS's iterative nature causes it to repeat work.

Maximum Frontier Size: For BFS, the maximum frontier size was 3. This highlights BFS's primary drawback—high memory consumption on large problems. For this small problem, however, the memory use is negligible. For IDS, the maximum frontier size was also 3, but this represents the maximum depth of the recursive call stack at any one time, not the number of nodes in a queue. This is IDS's main advantage: it has a much smaller memory footprint than BFS, making it suitable for problems with a massive, or even infinite, state space.

Solution Depth and Cost: Both algorithms found a solution with a depth of 7 and a cost of 7. This is expected because both BFS and IDS are complete and optimal for problems where each step has a uniform cost. Since the Wolf, Goat, and Cabbage problem has a uniform cost of 1 for each river crossing, both algorithms are guaranteed to find the shortest path.

In summary, for the Wolf, Goat, and Cabbage problem, both algorithms are effective. However, the analysis shows that IDS is more computationally expensive (generating and expanding more nodes) but significantly more memory-efficient than BFS, which is a crucial trade-off for more complex search problems.

Git Repository Link
[Git Repository Link Here]

Note: Access for the instructor is granted via the specified GitHub username or email address.

Addendum: Raw Text Outputs
Below are the unedited console outputs for each run of the program, with monospaced formatting.

Run: python3 main.py --domain wgc --algo bfs

Step 0: Initial State
  Farmer: Start Bank
  Wolf: Start Bank
  Goat: Start Bank
  Cabbage: Start Bank
--------------------
Step 1:
  Farmer: Destination Bank
  Wolf: Start Bank
  Goat: Destination Bank
  Cabbage: Start Bank
--------------------
Step 2:
  Farmer: Start Bank
  Wolf: Start Bank
  Goat: Destination Bank
  Cabbage: Start Bank
--------------------
Step 3:
  Farmer: Destination Bank
  Wolf: Destination Bank
  Goat: Destination Bank
  Cabbage: Start Bank
--------------------
Step 4:
  Farmer: Start Bank
  Wolf: Destination Bank
  Goat: Start Bank
  Cabbage: Start Bank
--------------------
Step 5:
  Farmer: Destination Bank
  Wolf: Destination Bank
  Goat: Start Bank
  Cabbage: Destination Bank
--------------------
Step 6:
  Farmer: Start Bank
  Wolf: Destination Bank
  Goat: Start Bank
  Cabbage: Destination Bank
--------------------
Step 7:
  Farmer: Destination Bank
  Wolf: Destination Bank
  Goat: Destination Bank
  Cabbage: Destination Bank
--------------------

Run: python3 main.py --domain wgc --algo ids

Step 0: Initial State
  Farmer: Start Bank
  Wolf: Start Bank
  Goat: Start Bank
  Cabbage: Start Bank
--------------------
Step 1:
  Farmer: Destination Bank
  Wolf: Start Bank
  Goat: Destination Bank
  Cabbage: Start Bank
--------------------
Step 2:
  Farmer: Start Bank
  Wolf: Start Bank
  Goat: Destination Bank
  Cabbage: Start Bank
--------------------
Step 3:
  Farmer: Destination Bank
  Wolf: Destination Bank
  Goat: Destination Bank
  Cabbage: Start Bank
--------------------
Step 4:
  Farmer: Start Bank
  Wolf: Destination Bank
  Goat: Start Bank
  Cabbage: Start Bank
--------------------
Step 5:
  Farmer: Destination Bank
  Wolf: Destination Bank
  Goat: Start Bank
  Cabbage: Destination Bank
--------------------
Step 6:
  Farmer: Start Bank
  Wolf: Destination Bank
  Goat: Start Bank
  Cabbage: Destination Bank
--------------------
Step 7:
  Farmer: Destination Bank
  Wolf: Destination Bank
  Goat: Destination Bank
  Cabbage: Destination Bank
--------------------
