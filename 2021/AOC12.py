"""BIG IDEA: 
create a graph using a dictionary
keys will be nodes in the graph, values will be sets of neighbouring nodes
e.g. graph[a] = set(neighbours of a)

paths will be a list of nodes which are connected
e.g. [start, a, A, end] 

therefore a list of paths is a list of lists 

next_paths is a function which takes a path and returns a list of paths 
by taking the current path and concatenating it with each neighbour of the current node 

step takes a list of paths 
generates the new paths for each path 
and then returns a list of paths"""


with open('AOC12.txt') as f:
    edges = {tuple(x.split('-')) for x in f.read().splitlines()}
    vertices = {x for edge in edges for x in edge}
    # graph = {v: [w for x,w in edges if (x,w) == (v,w) or (x,w) == (w, v)] for v in vertices}

graph = {v: set() for v in vertices}
for v,w in edges:
    if w != 'start': graph[v].add(w)
    if v != 'start': graph[w].add(v)

def next_paths(graph, cur_path):
    # returns all reachable paths from current path
    paths = [] 
    cur_node = cur_path[-1] # node we are at is the node at end of current path
    neighbours = graph[cur_node]
    for neighbour in neighbours:
        if not neighbour.islower():
            # small caves should only be visited once 
            paths.append(cur_path + [neighbour])
        elif neighbour not in cur_path:
            paths.append(cur_path + [neighbour])
    return paths

def step(graph, cur_paths):
    # cur_paths is a list of lists (because its elements are paths which are lists)
    new_paths = [] 
    for path in cur_paths:
        if 'end' not in path:
            new_paths += next_paths(graph, path)
        else:
            new_paths.append(path) # if we have reached the end in a path, dont find any new paths from it
    return new_paths

def find_all_paths(graph):
    incomplete_paths = [['start']] # paths which havent met an end 
    complete_paths = [] 
    while len(incomplete_paths) > 0:
        new_incomplete_paths = [] 
        for path in incomplete_paths:
            for p in next_paths(graph, path):
                if p[-1] == 'end':
                    complete_paths.append(p)
                else:
                    new_incomplete_paths.append(p)
        incomplete_paths = new_incomplete_paths
    return complete_paths

# task 1 
print(len(find_all_paths(graph)))

# task 2, need to slightly alter next_paths to allow once double visit to a small cave

def all_small_visited_once(cur_path):
    for node in cur_path:
        if node.islower() and cur_path.count(node) > 1:
            return False
    return True

def next_paths2(graph, cur_path):
    # returns all reachable paths from current path
    paths = [] 
    cur_node = cur_path[-1] # node we are at is the node at end of current path
    neighbours = graph[cur_node]
    small_visited_once = all_small_visited_once(cur_path)
    for neighbour in neighbours:
        if not neighbour.islower():
            paths.append(cur_path + [neighbour])
        elif small_visited_once:
            paths.append(cur_path + [neighbour])
        elif neighbour not in cur_path:
            paths.append(cur_path + [neighbour])
    return paths

def step2(graph, cur_paths):
    # cur_paths is a list of lists (because its elements are paths which are lists)
    new_paths = [] 
    for path in cur_paths:
        if 'end' not in path:
            new_paths += next_paths2(graph, path)
        else:
            new_paths.append(path)
    return new_paths

def find_all_paths2(graph):
    incomplete_paths = [['start']] # paths which havent met an end 
    complete_paths = [] 
    while len(incomplete_paths) > 0:
        new_incomplete_paths = [] 
        for path in incomplete_paths:
            for p in next_paths2(graph, path):
                if p[-1] == 'end':
                    complete_paths.append(p)
                else:
                    new_incomplete_paths.append(p)
        incomplete_paths = new_incomplete_paths
    return complete_paths

print(len(find_all_paths2(graph)))