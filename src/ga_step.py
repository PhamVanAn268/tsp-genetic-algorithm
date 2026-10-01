from population import create_population
from selection import tournament_selection
from crossover import order_crossover
from mutation import swap_mutation


if __name__ == "__main__":
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    population = create_population(
        population_size=5,
        num_cities=4
    )

    print("Population:")
    for i, chromosome in enumerate(population):
        print(f"{i + 1}: {chromosome}")

    parent1 = tournament_selection(
        population,
        distance_matrix,
        tournament_size=3
    )

    parent2 = tournament_selection(
        population,
        distance_matrix,
        tournament_size=3
    )

    print("\nParent 1:", parent1)
    print("Parent 2:", parent2)

    child = order_crossover(parent1, parent2)

    print("Child after crossover:", child)

    mutated_child = swap_mutation(child)

    print("Child after mutation :", mutated_child)