"""mutation_operators.py
Morgan Bauer and Ramsay Flower
19 April 2024

Different options for mutation operators using permutation representation.
Note: these operators will be applied elementwise to a vector of
permutations

"""
import random

def randIndex(lyst:list):
    return random.randrange(0,len(lyst))
  

def insert(lyst:list):
    if not type(lyst) is list:
        raise Exception("Error: input for insert was not a list")
    k = lyst[randIndex(lyst)] #which element will be moved
    i = randIndex(lyst) #where will it be moved to
    lyst.remove(k)
    lyst.insert(i,k)
    return lyst #likely unecessary; should do it in place


def inverse(lyst:list):
    if not type(lyst) is list:
        raise Exception("Error: input for inverse was not a list")
    #define bounds for the subset
    i1,i2 = randIndex(lyst), randIndex(lyst)#index 1 and 2
    pass
    #ill do this later
#takes in a lyst, swaps two elements at random, modifies it in place(?) as well as returns it


def swap(lyst:list):
    if not type(lyst) is list:
        raise Exception("Error: input for swap was not a list")
    i1,i2 = randIndex(lyst), randIndex(lyst)#index 1 and 2
    temp = lyst[i1]
    lyst[i1]=lyst[i2]
    lyst[i2] = temp
    return lyst #likely unecessary; should do it in place

MUTATION_LYST = [insert, inverse, swap]