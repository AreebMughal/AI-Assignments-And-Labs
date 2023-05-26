
from simpleai.search import CspProblem, backtrack, MOST_CONSTRAINED_VARIABLE, LEAST_CONSTRAINING_VALUE, min_conflicts


variables = ('Mark', 'Julia', 'Steve', 'Amanda', 'Brian', 'Joanne', 'Derek', 'Allan', 'Michelle', 'Kelly')

domains = {
    'Mark': ['Red', 'Green', 'Blue', 'Grey'],
    'Julia': ['Red', 'Green', 'Blue', 'Grey'],
    'Steve': ['Red', 'Green', 'Blue', 'Grey'],
    'Amanda': ['Red', 'Green', 'Blue', 'Grey'],
    'Brian': ['Red', 'Green', 'Blue', 'Grey'],
    'Joanne': ['Red', 'Green', 'Blue', 'Grey'],
    'Derek': ['Red', 'Green', 'Blue', 'Grey'],
    'Allan': ['Red', 'Green', 'Blue', 'Grey'],
    'Michelle': ['Red', 'Green', 'Blue', 'Grey'],
    'Kelly': ['Red', 'Green', 'Blue', 'Grey']
}


def const_diff(variables, values):
    return values[0] != values[1]

constraints = [
    (('Mark', 'Julia'), const_diff),
    (('Mark', 'Steve'), const_diff),
    (('Julia', 'Steve'), const_diff),
    (('Julia', 'Amanda'), const_diff),
    (('Julia', 'Derek'), const_diff),
    (('Julia', 'Brian'), const_diff),
    (('Steve', 'Amanda'), const_diff),
    (('Steve', 'Allan'), const_diff),
    (('Steve', 'Michelle'), const_diff),
    (('Amanda', 'Michelle'), const_diff),
    (('Amanda', 'Joanne'), const_diff),
    (('Amanda', 'Derek'), const_diff),
    (('Brian', 'Derek'), const_diff),
    (('Brian', 'Kelly'), const_diff),
    (('Joanne', 'Michelle'), const_diff),
    (('Joanne', 'Amanda'), const_diff),
    (('Joanne', 'Derek'), const_diff),
    (('Joanne', 'Kelly'), const_diff),
    (('Derek', 'Kelly'), const_diff),
]

problem = CspProblem(variables=variables, domains=domains, constraints=constraints)

result = backtrack(problem=problem, variable_heuristic=MOST_CONSTRAINED_VARIABLE, value_heuristic=LEAST_CONSTRAINING_VALUE)

print('Backtrack Result')
print(result)
for variable, value in result.items():
    print(f'{variable} => {value}')

result1 =  min_conflicts(problem)

print()
print('Iterative Improvement')
print(result1)
for variable, value in result1.items():
    print(f'{variable} => {value}')

