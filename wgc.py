
#This is the wolf, goat and cabbage problem
#The farmer has to take the wolf, goat and cabbage across the river
#The farmer can only take one item at a time
#The wolf cannot be left alone with the goat
#The goat cannot be left alone with the cabbage

#algoirthms used: BFS, IDS

# State represented as a tuple: (farmer, wolf, goat, cabbage)
# 0 = start bank, 1 = target bank

import collections

init_state = (0,0,0,0)
GOAL = (1,1,1,1)

def valid_moves(state):
    states = []
    farmer, wolf, goat, cabbage = state
    if farmer == 0:
        if farmer == wolf:
            states.append((abs(1-farmer),abs(1-wolf),goat,cabbage))
        if farmer == goat:
            states.append((abs(1-farmer),wolf,abs(goat-1),cabbage))
        if farmer == cabbage:
            states.append((abs(1-farmer),wolf,goat,abs(1-cabbage)))
        states.append((abs(1-farmer),wolf,goat,cabbage))
    if farmer == 1:
        if farmer == wolf:
            states.append((abs(1-farmer),abs(1-wolf),goat,cabbage))
        if farmer == goat:
            states.append((abs(1-farmer),wolf,abs(1-goat),cabbage))
        if farmer == cabbage:
            states.append((abs(1-farmer),wolf,goat,abs(1-cabbage)))
        states.append((abs(1-farmer),wolf,goat,cabbage))
    for move in states:
          if move[1] == move[2] and move[0] != move[1]:
                states.remove(move)
          if move[2] == move[3] and move[0] != move[2]:
                states.remove(move)
    return states

def goal(state):
       if state == (1,1,1,1):
              return True
       return False

def bfs(start_node):
    queue = collections.deque()
    queue_size = len(queue)
    t_nodes = 1
    e_nodes = 0
    visited = set()
    visited.add(start_node)
    queue.append((start_node, [start_node]))
    while queue:
        t_nodes += 1
        current_node, path  = queue.popleft()
        e_nodes += 1
        if current_node == GOAL:
            return path, queue_size, t_nodes, e_nodes
        for next_node in valid_moves(current_node):
            if next_node not in visited:
                visited.add(next_node)
                queue.append((next_node, path + [next_node]))
        if len(queue) > queue_size:
            queue_size = len(queue)
    return None

def dls(current_node,GOAL,depth):
    # visited = set()
    # visited.add(current_node)
    if current_node == GOAL:
        return [current_node]
    if depth == 0:
         return None
    for next_node in valid_moves(current_node):
        path = dls(next_node,GOAL,depth-1)
        if path:
            return [current_node] + path
    return None

def ids(start_node):
    depth = 0
    while True:
        depth += 1
        path = dls(start_node, GOAL, depth)
        if path:
            return path