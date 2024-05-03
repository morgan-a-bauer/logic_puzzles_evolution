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
    #TODO