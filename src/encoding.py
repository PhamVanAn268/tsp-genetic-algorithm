import random


def create_chromosome(num_cities):
    """
    Create one valid TSP chromosome.

    Example:
    num_cities = 5

    Possible output:
    [2, 0, 4, 1, 3]
    """

    chromosome = list(range(num_cities))
    random.shuffle(chromosome)

    return chromosome


def is_valid_chromosome(chromosome, num_cities):
    """
    Check whether a chromosome is a valid TSP permutation.
    """

    expected = list(range(num_cities))

    return sorted(chromosome) == expected

if __name__ == "__main__":
    chromosome = create_chromosome(5)

    print("Chromosome:", chromosome)
    print("Valid:", is_valid_chromosome(chromosome, 5))
    