"""crossover_operators.py
Morgan Bauer and Ramsay Flower
19 April 2024

Different options for crossover operators using permutation representation.
Note: these operators will be applied elementwise to a vector of
permutations

"""

def cycle(parents: list):
    """Cycle crossover"""
    parent_index = 0
    used_numbers = set()
    for pos, start_entry in enumerate(parents[parent_index]):
        if start_entry not in used_numbers:
            cycle = set()
            cycle.append(start_entry)

            parent_index += 1
            parent_index % 2

            new_entry = 'l'
            while new_entry != start_entry:
                new_entry = parents[parent_index][pos]
                print("changes")