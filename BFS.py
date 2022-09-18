graph = {'A': {'B', 'C'},
         'B': {'A', 'D', 'E'},
         'C': {'A', 'F'},
         'D': {'B'},
         'E': {'B', 'F'},
         'F': {'C', 'E'}
         }


def bfs(graph, start):
    visited, queue = [], [start]
    while queue:
        # print("Explored List: " + str(visited) + "Frontier List: " + str(queue)) print("Poped Vertex: " + vertex)
        vertex = queue.pop()
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph[vertex] - set(visited))
            print("----------")
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
