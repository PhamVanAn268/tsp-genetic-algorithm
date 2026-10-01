from selection import tournament_selection
from crossover import order_crossover
from mutation import swap_mutation
from fitness import calculate_fitness


def create_next_generation(
    population,
    distance_matrix,
    tournament_size=3,
    mutation_rate=0.1,
    elite_size=1
):
    """
    Create the next generation of the population.

    Steps:
    1. Keep the best individuals using elitism.
    2. Select parents using tournament selection.
    3. Create child using crossover.
    4. Apply mutation with a given probability.
    5. Repeat until the new population is full.
    """

    new_population = []

    population_size = len(population)

    # --------------------------------------------------
    # 1. ELITISM
    # --------------------------------------------------

    sorted_population = sorted(
        population,
        key=lambda chromosome: calculate_fitness(
            chromosome,
            distance_matrix
        ),
        reverse=True
    )

    elites = sorted_population[:elite_size]

    new_population.extend(elites)

    # --------------------------------------------------
    # 2. CREATE THE REST OF THE NEW POPULATION
    # --------------------------------------------------

    while len(new_population) < population_size:

        # Select parent 1
        parent1 = tournament_selection(
            population,
            distance_matrix,
            tournament_size
        )

        # Select parent 2
        parent2 = tournament_selection(
            population,
            distance_matrix,
            tournament_size
        )

        # Crossover
        child = order_crossover(
            parent1,
            parent2
        )

        # Mutation
        child = swap_mutation(
            child,
            mutation_rate
        )

        # Add child to new population
        new_population.append(child)

    return new_population


if __name__ == "__main__":
    from population import create_population
    from fitness import calculate_total_distance

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

    print("Old population:")

    for i, individual in enumerate(population):
        distance = calculate_total_distance(
            individual,
            distance_matrix
        )

        fitness = calculate_fitness(
            individual,
            distance_matrix
        )

        print(
            f"Individual {i + 1}: "
            f"{individual} | "
            f"Distance: {distance} | "
            f"Fitness: {fitness}"
        )

    new_population = create_next_generation(
        population,
        distance_matrix,
        tournament_size=3,
        mutation_rate=0.1,
        elite_size=1
    )

    print("\nNew population:")

    for i, individual in enumerate(new_population):
        distance = calculate_total_distance(
            individual,
            distance_matrix
        )

        fitness = calculate_fitness(
            individual,
            distance_matrix
        )

        print(
            f"Individual {i + 1}: "
            f"{individual} | "
            f"Distance: {distance} | "
            f"Fitness: {fitness}"
        )