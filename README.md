# tsp-genetic-algorithm
# Solving the Traveling Salesman Problem using Genetic Algorithm

## 1. Introduction

This project studies the Traveling Salesman Problem (TSP) and applies
different algorithms to solve it.

The main objective of the project is to understand the complete process:

Problem
→ Mathematical model
→ Solution representation
→ Algorithm
→ Implementation
→ Experiment
→ Evaluation

The project focuses mainly on applying a Genetic Algorithm (GA) to TSP.

---

## 2. Traveling Salesman Problem

The Traveling Salesman Problem asks:

> Given a set of cities and the distances between each pair of cities,
> find the shortest possible route that visits every city exactly once
> and returns to the starting city.

### Input

- A set of `n` cities.
- The distance between every pair of cities.

For example:

```text
Cities = {0, 1, 2, 3, 4}

Output
A tour that:
- visits every city exactly once;
- returns to the starting city;
- has minimum total distance.
Example:
0 -> 2 -> 4 -> 1 -> 3 -> 0

3. Objective Function
The objective is to minimize the total distance of the tour.
Minimize:

Total Tour Distance

If the tour is:
0 -> 2 -> 4 -> 1 -> 3 -> 0

then the total distance is:
d(0,2)
+ d(2,4)
+ d(4,1)
+ d(1,3)
+ d(3,0)

4. Constraints
A valid TSP solution must satisfy:
1. Every city is visited exactly once.
2. No city is omitted.
3. No city is visited more than once.
4. The route returns to the starting city.
5. Previous Approaches
Before applying Genetic Algorithm, two basic methods were studied.
Brute Force
Brute Force generates all possible tours and chooses the shortest one.
Advantages:
- Guarantees the optimal solution.
Disadvantages:
- Very high computational cost.
- The number of possible solutions grows factorially.
O(n!)

Therefore, Brute Force becomes impractical when the number of cities increases.
Greedy / Nearest Neighbor
The Greedy method starts from a city and repeatedly chooses the nearest
unvisited city.
Advantages:
- Simple.
- Fast.
- Easy to implement.
Disadvantages:
- Makes decisions based only on local information.
- Does not guarantee the globally optimal solution.
6. Genetic Algorithm
The main part of this project is solving TSP using a Genetic Algorithm.
Genetic Algorithm is a population-based optimization method inspired by
natural evolution.
Instead of working with only one solution, GA maintains a population of
candidate solutions.
The general process is:
Initial Population
        ↓
Fitness Evaluation
        ↓
Selection
        ↓
Crossover
        ↓
Mutation
        ↓
New Population
        ↓
Repeat
        ↓
Best Solution

The main components that will be implemented are:
1. Chromosome / solution encoding
2. Population initialization
3. Fitness function
4. Selection
5. Crossover
6. Mutation
7. Elitism / replacement
8. Stopping condition
9. Experimental evaluation
7. Solution Representation
For TSP, one chromosome represents one complete tour.
For example:
[0, 3, 1, 4, 2]


represents:
0 -> 3 -> 1 -> 4 -> 2 -> 0

Therefore, a chromosome must be a permutation of all cities.
A valid chromosome:
[0, 3, 1, 4, 2]


An invalid chromosome:
[0, 3, 1, 3, 2]


because city 3 appears twice and city 4 is missing.
8. Project Structure
tsp-genetic-algorithm/
|
|-- data/
|-- experiments/
|-- results/
|-- src/
|-- README.md
|-- requirements.txt
`-- .gitignore

src/
Contains the source code of the algorithms.
data/
Contains input datasets for TSP experiments.
experiments/
Contains scripts used to run experiments.
results/
Contains experiment results, figures, and evaluation outputs.
9. Development Roadmap
- [ ] Chromosome encoding
- [ ] Population initialization
- [ ] Fitness function
- [ ] Selection
- [ ] Crossover
- [ ] Mutation
- [ ] Elitism
- [ ] Stopping condition
- [ ] Complete Genetic Algorithm
- [ ] Convergence visualization
- [ ] Parameter experiments
- [ ] Comparison with Brute Force
- [ ] Comparison with Greedy
- [ ] Final evaluation
10. Algorithms
This project will compare three approaches:
Algorithm	Optimal Guarantee	Speed	Suitable for Large TSP
Brute Force	Yes	Very slow	No
Greedy	No	Fast	Yes
Genetic Algorithm	No	Moderate	Yes


The objective is not only to obtain a solution, but also to study how
Genetic Algorithm searches the solution space and how its parameters
affect solution quality.