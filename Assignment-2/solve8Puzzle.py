

goal_state = ((0, 1, 2), (3, 4, 5), (6, 7, 8))

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
    print()