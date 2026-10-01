import random


def order_crossover(parent1, parent2):
    """
    Create one child using Order Crossover (OX).
    """

    size = len(parent1)

    start, end = sorted(
        random.sample(range(size), 2)
    )

    child = [None] * size

    child[start:end + 1] = parent1[start:end + 1]

    remaining_cities = [
        city for city in parent2
        if city not in child
    ]

    remaining_index = 0

    for i in range(size):
        if child[i] is None:
            child[i] = remaining_cities[remaining_index]
            remaining_index += 1

    return child

if __name__ == "__main__":
    parent1 = [0, 1, 2, 3, 4, 5]
    parent2 = [3, 5, 4, 1, 0, 2]

    child = order_crossover(parent1, parent2)

    print("Parent 1:", parent1)
    print("Parent 2:", parent2)
    print("Child   :", child)