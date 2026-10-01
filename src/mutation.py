import random


def swap_mutation(chromosome, mutation_rate=0.1):
    """
    Perform swap mutation with a given probability.
    """

    mutated = chromosome.copy()

    if random.random() < mutation_rate:
        i, j = random.sample(
            range(len(mutated)),
            2
        )

        mutated[i], mutated[j] = mutated[j], mutated[i]

    return mutated

if __name__ == "__main__":
    chromosome = [0, 1, 2, 3, 4]

    mutated = swap_mutation(chromosome)

    print("Original:", chromosome)
    print("Mutated :", mutated)