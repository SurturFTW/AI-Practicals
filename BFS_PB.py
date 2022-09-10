graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        #print("explored list : " + str(visited) + " frontier list : " + str(queue))
        vertex = queue.pop(0)
        #print("Poped vertex :"+vertex)
        if vertex not in visited:
            visited.add(vertex)
            #print(graph[vertex])
            queue.extend(graph[vertex] - visited)
        # print("-------")
    # print("========")
    return visited

print(bfs(graph, 'C')) # {'B', 'C', 'A', 'F', 'D', 'E'}

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        # print(queue)
        (vertex, path) = queue.pop(0)
        # print("Path " + str((vertex, path)))
        # print("Now =" + str(graph[vertex]))
        # print(str())
        # print(str(graph[vertex] - set(path)))
        for next in (graph[vertex] - set(path)):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

print(list(bfs_paths(graph, 'A', 'F'))) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

print(shortest_path(graph, 'A', 'F')) # ['A', 'C', 'F']


