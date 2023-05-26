from abc import ABC, abstractmethod
from collections import deque
import sys
import numpy as np
import time

class Board:
    parent = None
    state = None
    operator = None
    depth = 0
    zero = None
    cost = 0

    def __init__(self, state, parent=None, operator=None, depth=0):
        self.parent = parent
        self.state = np.array(state)
        self.operator = operator
        self.depth = depth
        self.zero = self.find_0()
        self.cost = self.depth + self.manhattan()

    def __lt__(self, other):
        if self.cost != other.cost:
            return self.cost < other.cost
        else:
            op_pr = {'Up': 0, 'Down': 1, 'Left': 2, 'Right': 3}
            return op_pr[self.operator] < op_pr[other.operator]

    def __str__(self):
        return str(self.state[:3]) + '\n' \
               + str(self.state[3:6]) + '\n' \
               + str(self.state[6:]) + ' ' + str(self.depth) + str(self.operator) + '\n'

    def goal_test(self):
        if np.array_equal(self.state, np.arange(9)):
            return True
        else:
            return False

    def find_0(self):
        for i in range(9):
            if self.state[i] == 0:
                return i

    def manhattan(self):
        state = self.index(self.state)
        goal = self.index(np.arange(9))
        return sum((abs(state // 3 - goal // 3) + abs(state % 3 - goal % 3))[1:])

    @staticmethod
    def index(state):
        index = np.array(range(9))
        for x, y in enumerate(state):
            index[y] = x
        return index

    def swap(self, i, j):
        new_state = np.array(self.state)
        new_state[i], new_state[j] = new_state[j], new_state[i]
        return new_state

    def up(self):
        if self.zero > 2:
            return Board(self.swap(self.zero, self.zero - 3), self, 'Up', self.depth + 1)
        else:
            return None

    def down(self):
        if self.zero < 6:
            return Board(self.swap(self.zero, self.zero + 3), self, 'Down', self.depth + 1)
        else:
            return None

    def left(self):
        if self.zero % 3 != 0:
            return Board(self.swap(self.zero, self.zero - 1), self, 'Left', self.depth + 1)
        else:
            return None

    def right(self):
        if (self.zero + 1) % 3 != 0:
            return Board(self.swap(self.zero, self.zero + 1), self, 'Right', self.depth + 1)
        else:
            return None

    def neighbors(self):
        neighbors = [self.up(), self.down(), self.left(), self.right()]
        return list(filter(None, neighbors))

    __repr__ = __str__


class Solver(ABC):
    solution = None
    frontier = None
    nodes_expanded = 0
    max_depth = 0
    explored_nodes = set()
    initial_state = None

    def __init__(self, initial_state):
        self.initial_state = initial_state

    def ancestral_chain(self):
        current = self.solution
        # print('Current => ', current)
        chain = [current]
        while current.parent is not None:
            chain.append(current.parent)
            current = current.parent
        # print('Chain = ', chain)
        return chain

    @property
    def path(self):
        path = [node.operator for node in self.ancestral_chain()[-2::-1]]
        return path

    @abstractmethod
    def solve(self):
        pass

    def set_solution(self, board):
        self.solution = board
        self.nodes_expanded = len(self.explored_nodes) - len(self.frontier) - 1
        # return self.solution


class DFS(Solver):
    def __init__(self, initial_state):
        super(DFS, self).__init__(initial_state)
        self.frontier = []

    def solve(self):
        self.frontier.append(self.initial_state)
        while self.frontier:
            board = self.frontier.pop()
            self.explored_nodes.add(tuple(board.state))
            if board.goal_test():
                self.set_solution(board)
                break
            for neighbor in board.neighbors()[::-1]:
                if tuple(neighbor.state) not in self.explored_nodes:
                    self.frontier.append(neighbor)
                    self.explored_nodes.add(tuple(neighbor.state))
                    self.max_depth = max(self.max_depth, neighbor.depth)
        return


class BFS(Solver):
    def __init__(self, initial_state):
        super(BFS, self).__init__(initial_state)
        self.frontier = deque()

    def solve(self):
        self.frontier.append(self.initial_state)
        while self.frontier:
            board = self.frontier.popleft()
            self.explored_nodes.add(tuple(board.state))
            if board.goal_test():
                self.set_solution(board)
                break
            for neighbor in board.neighbors():
                if tuple(neighbor.state) not in self.explored_nodes:
                    self.frontier.append(neighbor)
                    self.explored_nodes.add(tuple(neighbor.state))
                    self.max_depth = max(self.max_depth, neighbor.depth)
        return


start_time = 0
def main():
    # print(sys.argv)
    p = Board(np.array(eval(sys.argv[2])))
    alg = sys.argv[1]
    if alg == 'bfs':
        s = BFS(p)
    elif alg == 'dfs':
        s = DFS(p)
    else:
        print("Invalid input, continuing through DFS")
        s = DFS(p)
    s.solve()
    end_time = time.time() - start_time
    file = open('searchResults.txt', 'w')

    file.write('path_to_goal: ' + str(s.path) + '\n')
    file.write('cost_of_path: ' + str(len(s.path)) + '\n')
    file.write('nodes_expanded: ' + str(s.nodes_expanded) + '\n')
    file.write('search_depth: ' + str(s.solution.depth) + '\n')
    file.write('max_search_depth: ' + str(s.max_depth) + '\n')
    file.write('running_time: ' + str(end_time))

    file.close()


if __name__ == "__main__":
    start_time = time.time()
    main()
