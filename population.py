"""population.py
Morgan Bauer and Ramsay Flower
11 April 2024

A class representing a population for an evolutionary approach to solving
logic grid puzzles. Each individual is a vector of permutations. The population
contains information such as the categories of objects

"""

class Population:
    def __init__(self, S1: list, S2: list, S3: list, S4: list, rules: list):
        self.__S1 = S1
        self.__S2 = S2
        self.__S3 = S3
        self.__S4 = S4
        self.__rules = rules
        self.__pop = []