
import simpleai as sa
from simpleai.search import SearchProblem, astar
print(SearchProblem.actions)


# graph = {
# 'A' : ['B','C'],
# 'B' : ['D', 'E'],
# 'C' : ['F'],
# 'D' : [],
# 'E' : ['F'],
# 'F' : []
# }
# BFS algorithm in Python


graph = {
    'A' : ['D'],
    'B' : ['C', 'D', 'F', 'I'],
    'C' : ['I', 'J'],
    'D' : ['E', 'K'],
    'E' : ['F', 'K'],
    'F' : ['G', 'I', 'K', 'L', 'Q', 'R', 'T', 'U'],
    'G' : ['H', 'I', 'L'],
    'H' : ['I', 'L', 'N'],
    'I' : ['J', 'O'],
    'J' : ['O', 'P'],
    'K' : ['Q'],
    'L' : ['M', 'N', 'U'],
    'M' : ['N', 'U', 'W'],
    'N' : ['O', 'P', 'W'],
    'O' : ['P'],
    'P' : ['W', 'X', 'Y', 'Z'],
    'Q' : ['R'],
    'R' : ['T', 'U'],
    'S' : ['T'],
    'T' : ['U'],
    'U' : ['W'],
    'V' : ['W', 'X'],
    'W' : ['X'],
    'X' : [],
    'Y' : ['Z'],
    'Z' : [],
}

import collections

# BFS algorithm
def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


# if __name__ == '__main__':

print("Following is Breadth First Traversal: ")
bfs(graph, 'A')