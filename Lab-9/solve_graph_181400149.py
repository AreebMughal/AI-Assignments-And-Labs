
def bfs(graph, node):
    visited = [] 
    queue = [] 
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print (s, end = " ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)
                                    

def dfs(graph, node, visited=None):
    if (visited is None):
        visited = set() 
    if node not in visited:
        print(node, end=' ')
    visited.add(node)
    for neighbour in graph[node]:
        dfs(graph, neighbour, visited)


def main():
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

    print('\n' + '-'*50)
    print("Following is Breadth First Search Traversal: ")
    bfs(graph, 'A')
    print('\n' + '-'*50)



    print('\n' + '-'*50)
    print("Following is Depth First Search Traversal: ")
    dfs(graph, 'A')
    print('\n' + '-'*50)

    print('\n===> Note: As there is no goal specify, so both searches traverse all elements, \nthat\'s why both visited nodes and path return would be same. \n')

main()
