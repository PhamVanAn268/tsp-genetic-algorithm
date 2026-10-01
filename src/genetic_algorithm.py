import matplotlib.pyplot as plt

from population import create_population
from generation import create_next_generation
from fitness import calculate_total_distance


def genetic_algorithm(
    distance_matrix,
    population_size=20,
    generations=100,
    tournament_size=3,
    mutation_rate=0.1,
    elite_size=1,
    patience=20
):
    """
    Run Genetic Algorithm for TSP.

    Returns:
        best_chromosome
        best_distance
        history
    """

    num_cities = len(distance_matrix)

    # Create initial population
    population = create_population(
        population_size,
        num_cities
    )

    # Best solution found so far
    best_chromosome = None
    best_distance = float("inf")

    # Count generations without improvement
    no_improvement = 0

    # Store best distance of each generation
    history = []

    for generation in range(generations):

        improved = False

        # Evaluate all chromosomes in current population
        for chromosome in population:

            distance = calculate_total_distance(
                chromosome,
                distance_matrix
            )

            # Update best solution
            if distance < best_distance:
                best_distance = distance
                best_chromosome = chromosome.copy()

                improved = True

        # Save best distance of this generation
        history.append(best_distance)

        # Update early stopping counter
        if improved:
            no_improvement = 0
        else:
            no_improvement += 1

        print(
            f"Generation {generation}: "
            f"Best distance = {best_distance} | "
            f"No improvement = {no_improvement}"
        )

        # Early stopping
        if no_improvement >= patience:
            print("\nStopping early: no improvement.")
            break

        # Create next generation
        population = create_next_generation(
            population,
            distance_matrix,
            tournament_size=tournament_size,
            mutation_rate=mutation_rate,
            elite_size=elite_size
        )

    return best_chromosome, best_distance, history


if __name__ == "__main__":

    distance_matrix = [
        [0, 12, 10, 19, 8, 14, 16, 11, 17, 13],
        [12, 0, 3, 7, 15, 9, 18, 14, 6, 10],
        [10, 3, 0, 6, 20, 8, 17, 13, 5, 9],
        [19, 7, 6, 0, 11, 12, 9, 10, 8, 7],
        [8, 15, 20, 11, 0, 5, 7, 9, 14, 6],
        [14, 9, 8, 12, 5, 0, 4, 6, 10, 3],
        [16, 18, 17, 9, 7, 4, 0, 5, 13, 8],
        [11, 14, 13, 10, 9, 6, 5, 0, 12, 7],
        [17, 6, 5, 8, 14, 10, 13, 12, 0, 9],
        [13, 10, 9, 7, 6, 3, 8, 7, 9, 0]
    ]

    best_chromosome, best_distance, history = genetic_algorithm(
        distance_matrix,
        population_size=50,
        generations=200,
        tournament_size=3,
        mutation_rate=0.1,
        elite_size=2,
        patience=40
    )

    print("\nBest solution:")
    print("Chromosome:", best_chromosome)
    print("Distance:", best_distance)

    print("\nHistory:")
    print(history)

    plt.plot(history)

    plt.xlabel("Generation")
    plt.ylabel("Best Distance")
    plt.title("Genetic Algorithm Convergence - 10 Cities")

    plt.grid()

    plt.show()