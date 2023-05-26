from ast import operator
from simpleai.search import CspProblem, backtrack, MOST_CONSTRAINED_VARIABLE, LEAST_CONSTRAINING_VALUE, min_conflicts

# from CSP.csp import const_different

variables = ('Baber', 'Daud', 'Faisal', 'Jameela', 'Kiran', 'Marium', 'Naila')

"""
Domain = ['SC', 'GTA', 'CoD', 'MK', 'TO', 'RL', 'DS']

1.	Daud ≠ Jameela 
2.	Kiran = {SC, GTA, CoD}
3.	Marium = {DS, CoD, TO}
4.	Naila < Marium
5.	Kiran < Daud
6.	Baber = {RL}
7.	Jameela > Naila
8.	Baber ≠ Naila 
9.	Naila ≠ {RL}
10.	Faisal ≠ {MK, TO, RL}
11.	Daud ≠ {TO}
12.	Daud < Faisal

"""

# domains = {
#     'Baber': ['RL'], 
#     'Daud': ['SC', 'GTA', 'CoD', 'MK', 'RL', 'DS'],
#     'Faisal': ['SC', 'GTA', 'CoD', 'DS'],
#     'Jameela': ['SC', 'GTA', 'CoD', 'MK', 'TO', 'RL', 'DS'],
#     'Kiran': ['SC', 'GTA', 'CoD'],
#     'Marium': ['CoD', 'TO', 'DS'],
#     'Naila': ['SC', 'GTA', 'CoD', 'MK', 'TO', 'DS']
# }
domainList = ('SC', 'GTA', 'CoD', 'MK', 'TO', 'RL', 'DS')

domains = {
    'Baber': ['SC', 'GTA', 'CoD', 'MK', 'TO', 'RL', 'DS'],
    'Daud': ['SC', 'GTA', 'CoD', 'MK', 'TO', 'RL', 'DS'],
    'Faisal': ['SC', 'GTA', 'CoD', 'MK', 'TO', 'RL', 'DS'],
    'Jameela': ['SC', 'GTA', 'CoD', 'MK', 'TO', 'RL', 'DS'],
    'Kiran': ['SC', 'GTA', 'CoD', 'MK', 'TO', 'RL', 'DS'],
    'Marium': ['SC', 'GTA', 'CoD', 'MK', 'TO', 'RL', 'DS'],
    'Naila': ['SC', 'GTA', 'CoD', 'MK', 'TO', 'RL', 'DS']
}

# *****************************************************************

def const_different(variables, values):
    return values[0] != values[1]

def const_less_than_other(variables, values):
    return domainList.index(values[0]) < domainList.index(values[1])

def const_greater_than_other(variables, values):
    return domainList.index(values[0]) > domainList.index(values[1])

constraints = [
    (('Daud', 'Jameela'), const_different),
    (('Naila', 'Marium'), const_less_than_other),
    (('Kiran', 'Daud'), const_less_than_other),
    (('Jameela', 'Naila'), const_greater_than_other),
    (('Baber', 'Naila'), const_different),
    (('Daud', 'Faisal'), const_less_than_other),
]

def printHeader(msg):
    print('\n' + '-' * 70)
    print(msg, end='')
    print('\n' + '-' * 70)

def part_a(domains):
    i = 1
    for key, value in domains.items():
        print(f'{i}) {key}: {set(value)}')
        i += 1

def part_b(domains):
    dic = {}
    for key, value in domains.items():                
        dic[str(len(value))] = key
    minIndex = min(dic.keys())
    
    return dic[minIndex]
    

printHeader('Part a) => Apply the unary constraints on each variable: ')
part_a(domains)

printHeader('Part b) => If the MRV is applied, the variable assigned first would be: ')
print(f'-> "{part_b(domains)}" would be assigned first as it has\nleast value in its domain after applying unary constraints')

my_problem = CspProblem(variables, domains, constraints)
res = backtrack(my_problem, variable_heuristic=MOST_CONSTRAINED_VARIABLE,       value_heuristic=LEAST_CONSTRAINING_VALUE)


min_res = min_conflicts(my_problem, None, 0)
print(res)
print(min_res)