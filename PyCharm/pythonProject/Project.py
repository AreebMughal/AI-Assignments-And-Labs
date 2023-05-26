
from simpleai.search import CspProblem, backtrack, MOST_CONSTRAINED_VARIABLE, LEAST_CONSTRAINING_VALUE, min_conflicts

"""
Domain = ['SC', 'GTA', 'CoD', 'MK', 'TO', 'RL', 'DS']
Constraints: 
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
variables = ('Baber', 'Daud', 'Faisal', 'Jameela', 'Kiran', 'Marium', 'Naila')

gameList = ('SC', 'GTA', 'CoD', 'MK', 'TO', 'RL', 'DS')

domains = {
    'Baber': ['SC', 'GTA', 'CoD', 'MK', 'TO', 'RL', 'DS'],
    'Daud': ['SC', 'GTA', 'CoD', 'MK', 'TO', 'RL', 'DS'],
    'Faisal': ['SC', 'GTA', 'CoD', 'MK', 'TO', 'RL', 'DS'],
    'Jameela': ['SC', 'GTA', 'CoD', 'MK', 'TO', 'RL', 'DS'],
    'Kiran': ['SC', 'GTA', 'CoD', 'MK', 'TO', 'RL', 'DS'],
    'Marium': ['SC', 'GTA', 'CoD', 'MK', 'TO', 'RL', 'DS'],
    'Naila': ['SC', 'GTA', 'CoD', 'MK', 'TO', 'RL', 'DS']
}

# *********************** Section-1 ******************************
def apply_unary_const(variables, domains, unary_constraints):
    for tuple in unary_constraints:
        varibale_name = tuple[0]
        domain_list = tuple[1]
        constraint_type = tuple[2]
        if varibale_name in variables:
            if constraint_type == '=':
                domains[varibale_name] = domain_list
            elif constraint_type == '!=':
                domain = list(domains[varibale_name])
                for element in domain_list:
                    domain.remove(element)
                domains[varibale_name] = domain
    return domains

unary_constraints = [
    ('Baber', ['RL'], '='),
    ('Daud', ['TO'], '!='),
    ('Faisal', ['MK', 'TO', 'RL'], '!='),
    ('Kiran', ['SC', 'GTA', 'CoD'], '='),
    ('Marium', ['DS', 'CoD', 'TO'], '='),
    ('Naila', ['RL'], '!=')
]

# *****************************************************************

def const_different(variables, values):
    return values[0] != values[1]

def const_less_than_other(variables, values):
    return gameList.index(values[0]) < gameList.index(values[1])

def const_greater_than_other(variables, values):
    return gameList.index(values[0]) > gameList.index(values[1])

binary_constraints = [
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

def print_solution(result):
    i = 1
    for variable, value in result.items():
        print(f'{i}) {variable} = {value}')
        i += 1

printHeader('Part a) => After applying unary constraints on each variable: ')
domains = apply_unary_const(variables, domains, unary_constraints)
part_a(domains)

printHeader('Part b) => If the MRV is applied, the variable assigned first would be: ')
print(f'-> "{part_b(domains)}" would be assigned first as it has\nleast value in its domain after applying unary constraints')

print('\nSecond way for finding first variable using MRV is: ')
my_problem = CspProblem(variables, domains, binary_constraints)
mrv_result = backtrack(my_problem, variable_heuristic=MOST_CONSTRAINED_VARIABLE)    
mrv_variables = list(mrv_result.keys())
print(f'-> "{mrv_variables[0]}" will be selected as first variable if we apply built-in MRV Heuristic')

printHeader('Part c) => Solution by using the Forward Checking with the \nLCV and MRV heuristics:')
result = backtrack(my_problem, variable_heuristic=MOST_CONSTRAINED_VARIABLE,       value_heuristic=LEAST_CONSTRAINING_VALUE)    
print_solution(result)

print('\nOrdering of Assigned Variables if we use LCV Heuristic:')
lcv_result = backtrack(my_problem, value_heuristic=LEAST_CONSTRAINING_VALUE) 
i = 1
for variable in lcv_result.keys():
    print(f'{i}) {variable}')
    i += 1

printHeader('Part d) => Iterative Improvement with Min-Conflicts Heuristic: ')
iterative_improvement_res = min_conflicts(my_problem, initial_assignment=None, iterations_limit=0)
print_solution(iterative_improvement_res)