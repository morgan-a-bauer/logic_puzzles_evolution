"""mutation_operators.py
Morgan Bauer and Ramsay Flower
19 April 2024

Different options for mutation operators using permutation representation.
Note: these operators will be applied elementwise to a vector of
permutations

"""
import random
def insert(lyst):
    k = lyst[random.randint(0,len(lyst))] #which element will be moved
    i = random.randint(0,len(lyst)) #where will it be moved to
    lyst.remove(k)
    lyst.insert(i,k)
    return lyst
def inverse(lyst):
    #define bounds for the subset
    i1 = random.randint(0,len(lyst)) #index 1
    i2 = random.randint(0,len(lyst)) #index 2