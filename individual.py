"""individual.py
Morgan Bauer and Ramsay Flower
11 April 2024

A class representing an individual for an evolutionary approach to solving
logic grid puzzles. Each individual is a vector of permutations.

"""
from random import randrange
from util import random_perm

class Individual:
    def __init__(self, p1: list, p2: list, p3: list):
        self.__genotype = [p1, p2, p3, [1, 2, 3, 4, 5]]
        self.__fitness = 0.0


    @property
    def genotype(self) -> list:
        return self.__genotype


    @property
    def fitness(self) -> float:
        return self.__fitness


    def __mul__(self, other):
        #TODO
        pass

    def __str__(self) -> str:
        print(self.__genotype)
        return "   ".join(["".join(map(str, perm)) for perm in self.__genotype])

if __name__ == "__main__":
    p1 = random_perm(5)
    p2 = random_perm(5)
    p3 = random_perm(5)

    i1 = Individual(p1, p2, p3)
    print(i1)