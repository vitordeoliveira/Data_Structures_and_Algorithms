# Kosaraju's algorithm to find strongly connected components in Python

from collections import defaultdict


class Graph:

    def __init__(self, vertex) -> None:
        self.V = vertex
        self.graph = defaultdict(list)

    def add_edge(self, s, d):
        self.graph[s].append(d)


g = Graph(5)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 2)


print(g.graph)
