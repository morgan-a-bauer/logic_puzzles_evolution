"""solver.py
Morgan Bauer and Ramsay Flower

An evolutionary solver for logic grid puzzles. (For now) The solver is initiated
from the command line. Input in the following order:
1. The maximum number of generations to run (an integer)
2. The size of the population (an integer)
3. The probability of crossover occuring (a floating-point number between 0.0 and 1.0)
4. The probability of mutation occuring (a floating-point number between 0.0 and 1.0)
6. The number of categories in the puzzle (an integer)
7. The number of items per category in the puzzle (an integer)
8. The index of which crossover method to use (in crossover_operators.py)
9. The index of which mutation method to use (in mutation_operators.py)
10. The number of rounds that occur in tournament selection (an integer)

Example: python3 solver.py 500 100 0.30 0.01 4 5 0 2 4
"""
from example1 import puzzle, rules
from population import Population
from stats import stats, report
import sys

def main():
    # Get input from command line
    max_gen = int(sys.argv[1])
    pop_size = int(sys.argv[2])
    pc = float(sys.argv[3])
    pm = float(sys.argv[4])
    num_categories = int(sys.argv[5])
    items_per_category = int(sys.argv[6])
    crossover_ind = int(sys.argv[7])
    mutation_ind = int(sys.argv[8])
    num_rounds = int(sys.argv[9])
    indiv_dims = (num_categories, items_per_category)

    gen_num = 0

    while gen_num < max_gen:
        gen_num += 1

        # Initialize first generation
        if gen_num == 1:
            generation = Population(pop_size, pc, pm, indiv_dims, puzzle, rules,
                                    crossover_ind, mutation_ind, num_rounds)
            generation.initialize_pop()

        gen_stats = stats(generation)
        top = report(generation, gen_num)
        if top.fitness == 1.0:
            break
        generation = generation.new_generation()

if __name__ == "__main__":
    main()