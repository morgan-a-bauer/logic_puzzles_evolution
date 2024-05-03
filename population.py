"""population.py
Morgan Bauer and Ramsay Flower
11 April 2024

A class representing a population for an evolutionary approach to solving
logic grid puzzles. Each individual is a vector of permutations. The population
contains information such as the categories of objects

"""

class Population:
    def __init__(self, pop_size: int, pc: float, pm: float, indiv_dims: tuple,
                 fitness_func: function, categories: list, rules: list):
        self.__pop_size = pop_size
        self.__pc = pc
        self.__pm = pm
        self.__indiv_dims = indiv_dims
        self.__categories = categories
        self.__num_categories = len(categories)
        self.__items_per_category = len(categories[0])
        self.__fitness_func = fitness_func
        self.__rules = rules
        self.__pop = []


        @property
        def pop_size(self):
            return self.__pop_size


        @property
        def pc(self):
            return self.__pc


        @property
        def pm(self):
            return self.__pm


        @property
        def indiv_dims(self):
            return self.__indiv_dims


        @property
        def categories(self):
            return self.__categories


        @property
        def num_categories(self):
            return self.__num_categories


        @property
        def items_per_category(self):
            return self.__items_per_category


        @property
        def fitness_func(self):
            return self.__fitness_func


        @property
        def rules(self):
            return self.__rules


        @property
        def pop(self):
            return self.__pop


        def initialize(self):
            