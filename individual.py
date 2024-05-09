"""individual.py
Morgan Bauer and Ramsay Flower
11 April 2024

A class representing an individual for an evolutionary approach to solving
logic grid puzzles. Each individual is a vector of permutations.

"""
from copy import deepcopy
from crossover_operators import CROSSOVER_LYST
from mutation_operators import MUTATION_LYST
from random import randrange, random
from util import random_perm

class Individual:
    def __init__(self, perms: list):
        self.__genotype = perms
        self.__fitness = 0.0
        self.__pop = None


    @property
    def genotype(self) -> list:
        return self.__genotype


    @property
    def fitness(self) -> float:
        return self.__fitness


    @fitness.setter
    def fitness(self, new_fit):
        self.__fitness = new_fit


    @property
    def pop(self):
        return self.__pop


    @pop.setter
    def pop(self, new_pop):
        self.__pop = new_pop


    def evaluate_fitness(self):
        self.__fitness = self.__pop.fitness_func(self)


    def __invert__(self):
        """Overloads the ~ operator for mutation."""
        operator = MUTATION_LYST[self.__pop.mutation_ind]

        # Each permutation (except the last) is mutated independently
        for loc, perm in enumerate(self.__genotype):
            if loc != len(self.__genotype) - 1:
                r = random()
                if r < self.__pop.pm:
                    self.__genotype[loc] = operator(perm)


    def __mul__(self, other):
        """Overloads the multiplication operator for recombination."""

        # Only crosses over a certain percentage of the time
        r = random()
        if r < self.__pop.pc:
            # Determine which crossover operator is being used
            operator = CROSSOVER_LYST[self.__pop.crossover_ind]

            # Initialize child genotypes
            c1 = []
            c2 = []

            # Populate child genotypes
            for p1_perm, p2_perm in zip(self.__genotype, other.genotype):
                c1_perm, c2_perm = operator(p1_perm, p2_perm)
                c1.append(c1_perm)
                c2.append(c2_perm)

            # Instantiate new Individual objects representing the children
            c1, c2 = Individual(c1), Individual(c2)

        else:
            c1 = deepcopy(self)
            c2 = deepcopy(other)

        # Set child populations
        c1.pop = self.__pop
        c2.pop = self.__pop


        # Perform mutation on children
        ~c1
        ~c2

        return c1, c2


    def __lt__(self, other):
        return True if self.__fitness < other.fitness else False


    def __gt__(self, other):
        return True if self.__fitness > other.fitness else False


    def __str__(self) -> str:
        genotype_str = "   ".join(["".join(map(str, perm)) for perm in self.__genotype])
        return f"{genotype_str}           {self.__fitness:.4f}"


if __name__ == "__main__":
    print("Cycle Crossover:\n")
    p1 = random_perm(5)
    p2 = random_perm(5)
    p3 = random_perm(5)

    i1 = Individual([p1, p2, p3, [1, 2, 3, 4, 5]])
    print(i1)

    p4 = random_perm(5)
    p5 = random_perm(5)
    p6 = random_perm(5)

    i2 = Individual([p4, p5, p6, [1, 2, 3, 4, 5]])
    print(i2)
    print()

    print("\nLess Than\n")
    print(i1 > i2)
    print("min:", min([i1, i2]))
    print("max:", max([i1, i2]))

    print("\nCycle Crossover\n")
    c1, c2 = i1 * i2
    print(c1)
    print(c2)

    print("\nPMX Crossover:\n")
    i3 = Individual([p1, p2, p3, [1, 2, 3, 4, 5]])
    print(i3)

    i4 = Individual([p4, p5, p6, [1, 2, 3, 4, 5]])
    print(i4)
    print()

    c3, c4 = i3 * i4
    print(c3)
    print(c4)

    print("\nmutation\n")

    ~c3
    ~c4

    print(c3)
    print(c4)