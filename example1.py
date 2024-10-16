# Adjust rules for yourself by modifying logical operators and indices

# Clue 1
def rule1(indiv):
    return indiv.genotype[3][1] != indiv.genotype[1][0]

def rule2(indiv):
    return indiv.genotype[3][1] != indiv.genotype[2][2]

def rule3(indiv):
    return indiv.genotype[1][0] != indiv.genotype[2][2]


def rule4(indiv): # wasnt tested for string elements ie '1st'. actually, do we need to do that? the individuals are just 2d lists of numbers right
    p = int(indiv.pop.puzzle[2][indiv.genotype[2].index(indiv.genotype[3][1])][0])
    q = int(indiv.pop.puzzle[2][indiv.genotype[2].index(indiv.genotype[1][0])][0])
    return abs(p-q) == 3

# Clue 2
def rule5(indiv):
    return indiv.genotype[2][3] == indiv.genotype[1][3]

# Clue 3
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

# Clue 4
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

# Clue 5
def rule14(indiv):
    p = int(indiv.pop.puzzle[2][indiv.genotype[2].index(indiv.genotype[3][3])][0]) - 1
    q = int(indiv.pop.puzzle[2][indiv.genotype[2].index(indiv.genotype[3][2])][0])
    return p==q

def rule15(indiv):
    return indiv.genotype[3][3] != indiv.genotype[2][0]

def rule16(indiv):
    return indiv.genotype[3][2] != indiv.genotype[2][4]

# Clue 6
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

# A collection of all rules to be satisfied
rules = [rule1, rule2, rule3,
            rule4, rule5, rule6,
            rule7, rule8, rule9,
            rule10, rule11, rule12,
            rule13, rule14, rule15,
            rule16, rule17, rule18,
            rule19, rule20, rule21]

# A collection of lists. Each sublist represents a category, where its elements are the items of that category
puzzle = [
            ["Venezuela", "Spain", "Panama", "Colombia", "Nicaragua"],
            ["Medicine", "Physics", "Literature", "Sociology", "Technology"],
            ["1st", "2nd", "3rd", "4th", "5th"],
            ["Carlos", "Ana", "Victor", "Ricardo", "Juan"]]
