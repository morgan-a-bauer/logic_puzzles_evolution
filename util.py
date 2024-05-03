"""util.py
Morgan Bauer and Ramsay Flower
11 April 2024

Utility functions for an evolutionary approach to solving logic grid puzzles

"""
from random import shuffle


def random_perm(n: int) -> str:
    p = [i for i in range(1, n+ 1)]
    shuffle(p)
    return p


def get_fitness(individual):
    rules = individual.pop.rules
    fitness = 1.0
    for rule in rules:
        if not rule:
            fitness -= (1 / len(rules))

    return fitness


if __name__ == "__main__":
    def rule1(indiv):
        return indiv.genotype[3][1] != indiv.genotype[1][0]

    def rule2(indiv):
        return indiv.genotype[3][1] != indiv.genotype[2][2]

    rules = [rule1, rule2]