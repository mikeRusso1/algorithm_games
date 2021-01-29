from collections import deque
import collections 

class Queue:

    def __init__(self):
        self.elements = collections.deque()

    def empty(self) -> bool:
        return not self.elements

    def put(self):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': [],
    'F': [], 
    'G': [],
    'H': [],
    'I': []
}

visited = set() # List to keep track of visited nodes.
queue = Queue()     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop() 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
# bfs(visited, graph, 'A')


open_ = deque()
closed_ = []
goal_state = 'E'
def search(graph, node, open_, closed_, bound):
    print("-------------")
    if node == goal_state:
        return node 

    elif node not in closed_ and bound > 0:
        closed_.append(node)
        for neighbour in graph[node]:
            open_.append(neighbour)
        print(node, open_)
    if open_:
        s = open_.pop()
        search(graph, s, open_, closed_, bound - 1)
    else:
        return 'fail'


def ids(node):
    i = 0
    while i >= 0:
        result = search(graph, node, open_, closed_, i)
        if result == 'fail':
            i += 1
        else:
            return result


# search(graph, 'A', open_, closed_)
ids('A')

# Location = TypeVar('Lacation')







