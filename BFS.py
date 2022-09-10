graph = { 'A': set(['B','C']),
        'B': set(['A', 'D', 'E']),
        'C': set(['A', 'F']),
        'D': set(['B']),
        'E': set(['B', 'F']),
        'F': set(['C', 'E'])
}

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        print("Explored List: " + str(visited) + "Frontier List: " + str(queue))
        vertex = queue.pop()
        print("Poped Vertex: " + vertex)
        if vertex not in visited:
           visited.add(vertex)
           queue.extend(graph[vertex] - visited)
           print("----------")
        print("==========")
    return visited

print(bfs(graph, 'C'))

def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append([next, path + [next]])

print("Paths: " + list(bfs_path(graph, 'A', 'E')))

def shortest_path(graph, start, goal):
    try:
        return next(bfs_path(graph, start, goal))
    except StopIteration:
         return None
print("Shortest Path: " + shortest_path(graph, 'A', 'F'))