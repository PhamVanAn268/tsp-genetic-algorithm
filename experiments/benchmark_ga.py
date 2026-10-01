import csv
import io
import os
import statistics
import sys
import time
from contextlib import redirect_stdout

import tsplib95


# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

SRC_DIR = os.path.join(PROJECT_ROOT, "src")

sys.path.append(SRC_DIR)

from genetic_algorithm import genetic_algorithm


# ============================================================
# BENCHMARK CONFIGURATION
# ============================================================

TSP_FILE = os.path.join(
    PROJECT_ROOT,
    "data",
    "tsplib",
    "eil51.tsp"
)

RESULT_FILE = os.path.join(
    PROJECT_ROOT,
    "results",
    "benchmark_eil51.csv"
)

# Known optimum of TSPLIB eil51
OPTIMAL_DISTANCE = 426

# Test first with 5 runs.
# Change to 30 later for the final benchmark.
NUM_RUNS = 5


# GA parameters
POPULATION_SIZE = 100
GENERATIONS = 1000
TOURNAMENT_SIZE = 3
MUTATION_RATE = 0.1
ELITE_SIZE = 2
PATIENCE = 100


# ============================================================
# LOAD TSPLIB INSTANCE
# ============================================================

print("Loading TSPLIB instance...")

problem = tsplib95.load(TSP_FILE)

nodes = list(problem.get_nodes())

print("Problem:", problem.name)
print("Number of cities:", problem.dimension)
print("Edge weight type:", problem.edge_weight_type)


# ============================================================
# BUILD DISTANCE MATRIX
# ============================================================

distance_matrix = []

for node_i in nodes:

    row = []

    for node_j in nodes:

        distance = problem.get_weight(
            node_i,
            node_j
        )

        row.append(distance)

    distance_matrix.append(row)


print("Distance matrix created successfully.")


# ============================================================
# RUN BENCHMARK
# ============================================================

distances = []
runtimes = []
gaps = []
results = []


for run in range(1, NUM_RUNS + 1):

    print("\n==============================")
    print(f"Run {run}/{NUM_RUNS}")
    print("==============================")

    start_time = time.perf_counter()

    # Suppress generation-by-generation output
    with redirect_stdout(io.StringIO()):

        best_chromosome, best_distance, history = genetic_algorithm(
            distance_matrix,
            population_size=POPULATION_SIZE,
            generations=GENERATIONS,
            tournament_size=TOURNAMENT_SIZE,
            mutation_rate=MUTATION_RATE,
            elite_size=ELITE_SIZE,
            patience=PATIENCE
        )

    end_time = time.perf_counter()

    runtime = end_time - start_time

    optimality_gap = (
        (best_distance - OPTIMAL_DISTANCE)
        / OPTIMAL_DISTANCE
        * 100
    )

    distances.append(best_distance)
    runtimes.append(runtime)
    gaps.append(optimality_gap)

    results.append({
        "run": run,
        "best_distance": best_distance,
        "optimal_distance": OPTIMAL_DISTANCE,
        "gap_percent": optimality_gap,
        "runtime_seconds": runtime,
        "generations_executed": len(history),
        "best_chromosome": str(best_chromosome)
    })

    print("Best distance:", best_distance)
    print("Known optimum:", OPTIMAL_DISTANCE)
    print(f"Gap: {optimality_gap:.2f}%")
    print(f"Runtime: {runtime:.4f} seconds")
    print("Generations executed:", len(history))


# ============================================================
# STATISTICS
# ============================================================

best_distance = min(distances)
average_distance = statistics.mean(distances)
worst_distance = max(distances)

best_gap = min(gaps)
average_gap = statistics.mean(gaps)
worst_gap = max(gaps)

average_runtime = statistics.mean(runtimes)

if len(distances) > 1:
    distance_std = statistics.stdev(distances)
else:
    distance_std = 0.0


# ============================================================
# DISPLAY FINAL RESULTS
# ============================================================

print("\n")
print("==========================================")
print("TSPLIB eil51 - GENETIC ALGORITHM BENCHMARK")
print("==========================================")

print("Problem:", problem.name)
print("Cities:", problem.dimension)
print("Runs:", NUM_RUNS)
print("Known optimum:", OPTIMAL_DISTANCE)

print("\nDISTANCE")
print("Best:", best_distance)
print(f"Average: {average_distance:.2f}")
print("Worst:", worst_distance)
print(f"Standard deviation: {distance_std:.2f}")

print("\nOPTIMALITY GAP")
print(f"Best gap: {best_gap:.2f}%")
print(f"Average gap: {average_gap:.2f}%")
print(f"Worst gap: {worst_gap:.2f}%")

print("\nRUNTIME")
print(f"Average: {average_runtime:.4f} seconds")
print(f"Fastest: {min(runtimes):.4f} seconds")
print(f"Slowest: {max(runtimes):.4f} seconds")


# ============================================================
# SAVE CSV
# ============================================================

os.makedirs(
    os.path.dirname(RESULT_FILE),
    exist_ok=True
)

with open(
    RESULT_FILE,
    "w",
    newline="",
    encoding="utf-8"
) as file:

    fieldnames = [
        "run",
        "best_distance",
        "optimal_distance",
        "gap_percent",
        "runtime_seconds",
        "generations_executed",
        "best_chromosome"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(results)


print("\nBenchmark results saved to:")
print(RESULT_FILE)