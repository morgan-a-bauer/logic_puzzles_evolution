"""population.py
Morgan Bauer and Ramsay Flower
11 April 2024

A class representing a population for an evolutionary approach to solving
logic grid puzzles. Each individual is a vector of permutations. The population
contains information such as the categories of objects

"""
from individual import Individual
from random import choice
from util import get_fitness, random_perm

class Population:
    def __init__(self, pop_size: int, pc: float, pm: float, indiv_dims: tuple,
                 puzzle: list, rules: list, crossover_ind: int,
                 mutation_ind: int):
        self.__pop_size = pop_size
        self.__pc = pc
        self.__pm = pm
        self.__puzzle = puzzle
        self.__num_categories = indiv_dims[0]
        self.__items_per_category = indiv_dims[1]
        self.__fitness_func = get_fitness
        self.__rules = rules
        self.__crossover_ind = crossover_ind
        self.__mutation_ind = mutation_ind
        self.__pop_lyst = []


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
    def puzzle(self):
        return self.__puzzle


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
    def crossover_ind(self):
        return self.__crossover_ind


    @property
    def mutation_ind(self):
        return self.__mutation_ind


    @property
    def pop_lyst(self):
        return self.__pop_lyst


    def initialize_pop(self):
        for i in range(self.__pop_size):
            new_genotype = [random_perm(self.__items_per_category) for\
                            i in range(self.__num_categories - 1)] +\
                            [[i for i in range(1, self.__items_per_category + 1)]]
            new_indiv = Individual(new_genotype)
            new_indiv.pop = self
            new_indiv.evaluate_fitness()
            self.__pop_lyst.append(new_indiv)


    def select_parent(self):
        contestants = [choice(self.__pop_lyst) for i in range(2)]
        return max(contestants)


    def new_generation(self):
        #TODO
        pass


    def __str__(self):
        print_str = ''
        for indiv in self.__pop_lyst:
            print_str += str(indiv) + "\n"

        return print_str


if __name__ == "__main__":
    new_pop = Population(100, 0.3, 0.01, (4, 5), [
                         ["Venezuela", "Spain", "Panama", "Colombia", "Nicaragua"],
                         ["Medicine", "Physics", "Literature", "Sociology", "Technology"],
                         ["1st", "2nd", "3rd", "4th", "5th"],
                         ["Carlos", "Ana", "Victor", "Ricardo", "Juan"]], [],
                         0, 2)

    new_pop.initialize_pop()
    print(new_pop)