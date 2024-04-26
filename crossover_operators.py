"""crossover_operators.py
Morgan Bauer and Ramsay Flower
19 April 2024

Different options for crossover operators using permutation representation.
Note: these operators will be applied elementwise to a vector of
permutations

"""
from random import randint

def cycle(p1: list, p2: list):
    """An implementation of cycle crossover for evolutionary algorithms using
    permutation representation. Finds all cycles in the permutation and swaps
    the elements of approximately half of those cycles. Returns two lists,
    representing the two child permutations.

    Input:
    p1 -- a permutation from the genotype of the first parent
    p2 -- a permutation from the genotype of the second parent

    """
    # Which elements are already identified as elements of cycles
    used_nums = set()

    # Which elements are in cycles that will be switched
    to_switch = set()

    # Count the number of cycles
    cycle_num = 0

    # Until all cycles have been identified
    while len(used_nums) != len(p1):
        i = 0

        # If the element in p1 at index i is already in an identified cycle
        while p1[i] in used_nums:
            i += 1

        # Identify first two elements of the cycle
        start_num = p1[i]
        next_num = p2[i]

        # Initialize current cycle
        cycle = {start_num, next_num}
        used_nums.add(start_num)
        used_nums.add(next_num)

        # Continue until the starting element is reached again
        while next_num != start_num:

            # Find the next element in the cycle
            i = p1.index(next_num)
            next_num = p2[i]

            # Update sets
            cycle.add(next_num)
            used_nums.add(next_num)

        # Even numbered cycles will be switched
        if cycle_num % 2 == 0:
            to_switch |= cycle

        # Increment cycle number
        cycle_num += 1

    # Initialize child permutations
    c1_part = [0 for i in p1]
    c2_part = [0 for i in p1]

    # Populate chuld permutations
    for i in range(len(p1)):

        # Switch applicable elements
        if p1[i] in to_switch:
            c1_part[i], c2_part[i] = p2[i], p1[i]

        else:
            c1_part[i], c2_part[i] = p1[i], p2[i]

    return c1_part, c2_part


def pmx(p1: list, p2: list):
    point_1, point_2 = randint(len(p1)), randint(len(p1))

# Contains all crossover operators
CROSSOVER_LYST = [cycle]