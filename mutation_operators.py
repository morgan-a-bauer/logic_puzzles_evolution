"""mutation_operators.py
Morgan Bauer and Ramsay Flower
19 April 2024

Different options for mutation operators using permutation representation.
Note: these operators will be applied elementwise to a vector of
permutations

"""
import random

def randIndex(lyst:list):
    return random.randint(0,len(lyst)-1)
  

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
    if i1>i2:
        i1,i2 = i2,i1
    elif i1==i2:
        return lyst
    reverseSect = lyst[i1:i2+1]
    reverseSect.reverse()
    lyst2=[]
    for item in lyst[:i1]:
        lyst2.append(item)
    for item in reverseSect:
        lyst2.append(item)
    for item in lyst[i2+1:]:
        lyst2.append(item)
    return lyst2

def swap(lyst:list):
    if not type(lyst) is list:
        raise Exception("Error: input for swap was not a list")
    i1,i2 = randIndex(lyst), randIndex(lyst)#index 1 and 2
    temp = lyst[i1]
    lyst[i1]=lyst[i2]
    lyst[i2] = temp
    return lyst #likely unecessary; should do it in place

MUTATION_LYST = [insert, inverse, swap]