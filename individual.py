"""individual.py
Morgan Bauer and Ramsay Flower
11 April 2024

A class representing an individual for an evolutionary approach to solving
logic grid puzzles. Each individual is a vector of permutations.

"""
from crossover_operators import CROSSOVER_LYST
from random import randrange
from util import random_perm

class Individual:
    def __init__(self, perms: list, c_ind: int, m_ind: int):
        self.__genotype = perms
        self.__fitness = 0.0
        self.__crossover_index = c_ind
        self.__mutation_index = m_ind


    @property
    def genotype(self) -> list:
        return self.__genotype


    @property
    def fitness(self) -> float:
        return self.__fitness


    def __mul__(self, other):
        """Overloads the multiplication operator for recombination."""

        # Determine which crossover operator is being used
        operator = CROSSOVER_LYST[self.__crossover_index]

        # Initialize child genotypes
        c1 = []
        c2 = []

        # Populate child genotypes
        for p1_perm, p2_perm in zip(self.__genotype, other.genotype):
            c1_perm, c2_perm = operator(p1_perm, p2_perm)
            c1.append(c1_perm)
            c2.append(c2_perm)

        # Instantiate and return new Individual objects representing the children
        return Individual(c1, self.__crossover_index, self.__mutation_index),\
               Individual(c2, self.__crossover_index, self.__mutation_index)

    def __str__(self) -> str:
        return "   ".join(["".join(map(str, perm)) for perm in self.__genotype])

if __name__ == "__main__":
    print("Cycle Crossover:\n")
    p1 = random_perm(5)
    p2 = random_perm(5)
    p3 = random_perm(5)

    i1 = Individual([p1, p2, p3, [1, 2, 3, 4, 5]], 0, 0)
    print(i1)

    p4 = random_perm(5)
    p5 = random_perm(5)
    p6 = random_perm(5)

    i2 = Individual([p4, p5, p6, [1, 2, 3, 4, 5]], 0, 0)
    print(i2)
    print()

    c1, c2 = i1 * i2
    print(c1)
    print(c2)

    print("\nPMX Crossover:\n")
    i3 = Individual([p1, p2, p3, [1, 2, 3, 4, 5]], 1, 0)
    print(i3)

    i4 = Individual([p4, p5, p6, [1, 2, 3, 4, 5]], 0, 0)
    print(i4)
    print()

    c3, c4 = i3 * i4
    print(c3)
    print(c4)