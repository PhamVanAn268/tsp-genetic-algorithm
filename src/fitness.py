from population import create_population



def calculate_total_distance(chromosome, distance_matrix):
    """
    Calculate the total distance of a TSP tour.
    """

    total_distance = 0

    for i in range(len(chromosome) - 1):
        current_city = chromosome[i]
        next_city = chromosome[i + 1]

        total_distance += distance_matrix[current_city][next_city]

    # Return from the last city to the starting city
    last_city = chromosome[-1]
    first_city = chromosome[0]

    total_distance += distance_matrix[last_city][first_city]

    return total_distance

def calculate_fitness(chromosome, distance_matrix):
    """
    Calculate fitness of a TSP chromosome.

    Smaller distance means larger fitness.
    """

    total_distance = calculate_total_distance(
        chromosome,
        distance_matrix
    )

    return 1 / total_distance

def evaluate_population(population, distance_matrix):
    """
    Calculate fitness for every chromosome in the population.
    """

    fitness_values = []

    for chromosome in population:
        fitness = calculate_fitness(
            chromosome,
            distance_matrix
        )

        fitness_values.append(fitness)

    return fitness_values


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

    fitness_values = evaluate_population(
        population,
        distance_matrix
    )

    for i, chromosome in enumerate(population):
        distance = calculate_total_distance(
            chromosome,
            distance_matrix
        )

        fitness = fitness_values[i]

        print(
            f"Individual {i + 1}: "
            f"{chromosome} | "
            f"Distance: {distance} | "
            f"Fitness: {fitness}"
        )