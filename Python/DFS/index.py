
from collections import defaultdict


def dfs_full_connections(d, visited_stack, graph):
    visited_stack[d] = True
    print(f"vertex {d}: {graph[d]}")
    for i in graph[d]:
        if not visited_stack[i]:
            dfs_full_connections(i, visited_stack, graph)

def dfs(d, visited_stack, graph):
    visited_stack[d] = True
    print(f"=> {d}  ", end="")
    for i in graph[d]:
        if not visited_stack[i]:
            dfs(i, visited_stack, graph)


graph = defaultdict(list)

graph[0].append(1)
graph[0].append(2)
graph[0].append(3)
graph[0].append(4)
graph[1].append(3)
graph[3].append(0)
graph[4].append(3)


dfs(1, [False]*5, graph)
print()
dfs_full_connections(1, [False]*5, graph)
# print(graph)
