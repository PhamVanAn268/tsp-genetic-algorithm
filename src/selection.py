import random

from fitness import calculate_fitness

def tournament_selection(
    population,
    distance_matrix,
    tournament_size=3
):
    """
    Select one parent using tournament selection.
    """

    candidates = random.sample(
        population,
        tournament_size
    )

    best_candidate = candidates[0]
    best_fitness = calculate_fitness(
        best_candidate,
        distance_matrix
    )

    for candidate in candidates[1:]:
        fitness = calculate_fitness(
            candidate,
            distance_matrix
        )

        if fitness > best_fitness:
            best_candidate = candidate
            best_fitness = fitness

    return best_candidate

if __name__ == "__main__":
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    population = [
        [0, 1, 2, 3],
        [0, 1, 3, 2],
        [0, 2, 1, 3],
        [0, 2, 3, 1],
        [0, 3, 1, 2]
    ]

    parent = tournament_selection(
        population,
        distance_matrix,
        tournament_size=3
    )

    print("Selected parent:", parent)
    print(
        "Fitness:",
        calculate_fitness(parent, distance_matrix)
    )