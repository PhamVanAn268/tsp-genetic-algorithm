from encoding import create_chromosome, is_valid_chromosome

def create_population(population_size, num_cities):
    """
    Create an initial population for TSP.

    Each individual is a valid chromosome.
    """

    population = []

    for _ in range(population_size):
        chromosome = create_chromosome(num_cities)
        population.append(chromosome)

    return population


def is_valid_population(population, num_cities):
    """
    Check whether every chromosome in the population is valid.
    """

    for chromosome in population:
        if not is_valid_chromosome(chromosome, num_cities):
            return False

    return True


if __name__ == "__main__":
    population = create_population(
        population_size=5,
        num_cities=5
    )

    for i, chromosome in enumerate(population):
        print(f"Individual {i + 1}: {chromosome}")

    print("Population valid:", is_valid_population(population, 5))