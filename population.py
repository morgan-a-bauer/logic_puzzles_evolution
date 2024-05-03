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
                 mutation_ind: int, num_rounds = 1):
        self.__pop_size = pop_size
        self.__pc = pc
        self.__pm = pm
        self.__puzzle = puzzle
        self.__num_categories = indiv_dims[0]
        self.__items_per_category = indiv_dims[1]
        self.__fitness_func = get_fitness
        self.__rules = rules
        self.__crossover_ind = crossover_ind  # Which crossover operator is used
        self.__mutation_ind = mutation_ind  # Which mutation operator is used
        self.__num_rounds = num_rounds  # For tournament selection
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
    def num_rounds(self):
        return self.__num_rounds


    @property
    def pop_lyst(self):
        return self.__pop_lyst


    @pop_lyst.setter
    def pop_lyst(self, new_lyst):
        self.__pop_lyst = new_lyst


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
        contestants = [[choice(self.__pop_lyst) for i in range(2)] for i in\
                       range(self.__num_rounds * 2)]
        for round in range(self.__num_rounds):
            for bracket_num, bracket in enumerate(contestants):
                contestants[bracket_num] = max(bracket)
            if round != self.__num_rounds - 1:
                contestants = [[contestants[2 * i], contestants[2 * i + 1]] for i in range((len(contestants) // 2))]
        return max(contestants)


    def new_generation(self):
        next_gen = Population(self.__pop_size, self.__pc, self.__pm,
                              (self.__num_categories, self.__items_per_category),
                              self.__puzzle, self.__rules, self.__crossover_ind,
                              self.__mutation_ind, self.__num_rounds)
        child_lyst = []
        while len(child_lyst) != len(self.__pop_lyst):
            parent1 = self.select_parent()
            parent2 = self.select_parent()


    def __str__(self):
        print_str = ''
        for indiv in self.__pop_lyst:
            print_str += str(indiv) + "\n"

        return print_str


if __name__ == "__main__":
    #Clue 1
    def rule1(indiv):
        return indiv.genotype[3][1] != indiv.genotype[1][0]

    def rule2(indiv):
        return indiv.genotype[3][1] != indiv.genotype[2][2]

    def rule3(indiv):
        return indiv.genotype[1][0] != indiv.genotype[2][2]


    def rule4(indiv): #wasnt tested for string elements ie '1st'. actually, do we need to do that? the individuals are just 2d lists of numbers right
        p = int(indiv.pop.puzzle[2][indiv.genotype[2].index(indiv.genotype[3][1])][0])
        q = int(indiv.pop.puzzle[2][indiv.genotype[2].index(indiv.genotype[1][0])][0])
        return abs(p-q) == 3

    #Clue 2
    def rule5(indiv):
        return indiv.genotype[2][3] == indiv.genotype[1][3]

    #Clue 3
    def rule6(indiv):
        return indiv.genotype[3][3] != indiv.genotype[1][2]

    def rule7(indiv):
        return indiv.genotype[3][3] != indiv.genotype[2][2]

    def rule8(indiv):
        return indiv.genotype[1][2] != indiv.genotype[2][2]

    def rule9(indiv):
        p = int(indiv.pop.puzzle[2][indiv.genotype[2].index(indiv.genotype[3][3])][0])
        q = int(indiv.pop.puzzle[2][indiv.genotype[2].index(indiv.genotype[1][2])][0])
        return abs(p-q) == 3

    #Clue 4
    def rule10(indiv):
        return indiv.genotype[0][2] != indiv.genotype[1][4]

    def rule11(indiv):
        p = int(indiv.pop.puzzle[2][indiv.genotype[2].index(indiv.genotype[0][2])][0]) + 1
        q = int(indiv.pop.puzzle[2][indiv.genotype[2].index(indiv.genotype[1][4])][0])
        return p==q

    def rule12(indiv):
        return indiv.genotype[0][2] != indiv.genotype[2][4]

    def rule13(indiv):
        return indiv.genotype[1][4] != indiv.genotype[2][0]

    #Clue 5
    def rule14(indiv):
        p = int(indiv.pop.puzzle[2][indiv.genotype[2].index(indiv.genotype[3][3])][0]) - 1
        q = int(indiv.pop.puzzle[2][indiv.genotype[2].index(indiv.genotype[3][2])][0])
        return p==q

    def rule15(indiv):
        return indiv.genotype[3][3] != indiv.genotype[2][0]

    def rule16(indiv):
        return indiv.genotype[3][2] != indiv.genotype[2][4]

    #Clue 6
    def rule17(indiv):
        return indiv.genotype[3][4] != indiv.genotype[0][0]

    def rule18(indiv):
        p = int(indiv.pop.puzzle[2][indiv.genotype[2].index(indiv.genotype[3][4])][0])
        q = int(indiv.pop.puzzle[2][indiv.genotype[2].index(indiv.genotype[0][0])][0])
        return abs(p-q) == 2

    def rule19(indiv):
        return indiv.genotype[0][4] == indiv.genotype[2][3]

    def rule20(indiv):
        return indiv.genotype[3][4] == indiv.genotype[2][4]

    def rule21(indiv):
        return indiv.genotype[0][4] != indiv.genotype[3][4]

    rules = [rule1, rule2, rule3,
             rule4, rule5, rule6,
             rule7, rule8, rule9,
             rule10, rule11, rule12,
             rule13, rule14, rule15,
             rule16, rule17, rule18,
             rule19, rule20, rule21]

    new_pop = Population(100, 0.3, 0.01, (4, 5), [
                         ["Venezuela", "Spain", "Panama", "Colombia", "Nicaragua"],
                         ["Medicine", "Physics", "Literature", "Sociology", "Technology"],
                         ["1st", "2nd", "3rd", "4th", "5th"],
                         ["Carlos", "Ana", "Victor", "Ricardo", "Juan"]], rules,
                         0, 2, 4)

    new_pop.initialize_pop()
    print(new_pop)

    print("\nSelection\n")
    p1 = new_pop.select_parent()
    print(p1.fitness)
