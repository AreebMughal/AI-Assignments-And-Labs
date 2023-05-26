# from unittest import result
from simpleai.search import CspProblem, backtrack

# from simpleai import __init__

variables = ('L1', 'L2', 'L3', 'L4', 'L5')
"""
   1. L1 != L2
   2. L2 != L3
   3. L2 != L4
   4. L3 != L4
   5. L3 != L5
   6. L4 != L5
"""
domains = {
    'L1': ['Kareem'],
    'L2': ['Kareem', 'Jawad'],
    'L3': ['Kareem', 'Jawad', 'Ahmed'],
    'L4': ['Kareem', 'Jawad', 'Ahmed'],
    'L5': ['Kareem', 'Jawad']
}


def const_different(variables, values):
    return len(values) == len(set(values))


constraints = [
    (('L1', 'L2'), const_different),
    (('L2', 'L3'), const_different),
    (('L2', 'L4'), const_different),
    (('L3', 'L4'), const_different),
    (('L3', 'L5'), const_different),
    (('L4', 'L5'), const_different),
]

my_problem = CspProblem(variables, domains, constraints)

result = backtrack(my_problem)

print(result)
