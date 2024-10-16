"""mutation_operators.py
Morgan Bauer and Ramsay Flower
19 April 2024

Different options for mutation operators using permutation representation.
Note: these operators will be applied elementwise to a vector of
permutations

"""
import random
#TODO: Test in-place

def randIndex(lyst: list):
    """Select a random index from a list
    
    Input:
    lyst -- the list to select an index from
    
    """
    return random.randint(0,len(lyst)-1)
  

def insert(lyst: list):
    """Insertion mutation
    
    Input:
    lyst -- the individual to mutate
    
    """
    if not type(lyst) is list:
        raise Exception("Error: input for insert was not a list")
    k = lyst[randIndex(lyst)]  # which element will be moved
    i = randIndex(lyst)  # where will it be moved to
    lyst.remove(k)
    lyst.insert(i,k)
    return lyst  # likely unecessary; should do it in place


def inverse(lyst:list):
    """Inverse mutation
    
    Input:
    lyst -- the individual to mutate
    
    """
    if not type(lyst) is list:
        raise Exception("Error: input for inverse was not a list")
    # define bounds for the subset
    i1,i2 = randIndex(lyst), randIndex(lyst)  # index 1 and 2
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
    """Swap mutation
    
    Input:
    lyst -- the individual to mutate
    
    """
    if not type(lyst) is list:
        raise Exception("Error: input for swap was not a list")
    # grab two random indices
    i1,i2 = randIndex(lyst), randIndex(lyst)
    # swap  
    lyst[i1], lyst[i2] = lyst[i2], lyst[i1]
    return lyst  # likely unecessary; should do it in place

def scramble(lyst:list):  # like an egg before you get folded like an omlette
    """Scramble mutation
    
    Input:
    lyst -- the individual to mutate
    
    """
    if not type(lyst) is list:
        raise Exception("Error: input for swap was not a list")
    # this is a really complex program
    random.shuffle(lyst)
    return lyst

MUTATION_LYST = [insert, inverse, swap, scramble]
