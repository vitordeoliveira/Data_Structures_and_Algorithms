# Kosaraju's algorithm to find strongly connected components in Python

from collections import defaultdict


class Graph:

    def __init__(self, vertex=1) -> None:
        self.V = vertex
        self.graph = defaultdict(list)

    def add_edge(self, s, d):
        if(not s in self.graph):
            self.V = self.V + 1
        self.graph[s].append(d)

    def dfs_1(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs_1(i, visited_vertex, stack)
        stack = stack.append(d)

    def dfs_2(self, d, visited_vertex):
        visited_vertex[d] = True
        print(d, end='')
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs_2(i, visited_vertex)

    def reverse(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def print_scc(self):
        stack = []
        visited_vertex = [False] * (self.V)

        for i in range(self.V):
            if not visited_vertex[i]:
                self.dfs_1(i, visited_vertex, stack)

        gr = self.reverse()

        visited_vertex = [False] * (self.V)

        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs_2(i, visited_vertex)
                print("")


g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 0)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
g.add_edge(6, 7)

# print(g.V)

print("Strongly Connected Components:")
g.print_scc()
