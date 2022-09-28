graph = {'A': {'B', 'C'},
         'B': {'A', 'D', 'E'},
         'C': {'A', 'F'},
         'D': {'B'},
         'E': {'B', 'F'},
         'F': {'C', 'E'}
         }

def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.extend([next, path + [next]])


print("Paths: " + list(bfs_path(graph, 'A', 'E')))

# def bfs(graph, start):
#     visited, queue = [], [start]
#     while queue:
#         # print("Explored List: " + str(visited) + "Frontier List: " + str(queue)) print("Poped Vertex: " + vertex)
#         vertex = queue.pop()
#         if vertex not in visited:
#             visited.extend(vertex)
#             queue.extend(graph[vertex] - set(visited))
#             print("----------")
#     return visited


# print(bfs(graph, 'C'))
