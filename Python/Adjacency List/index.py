# Adjascency List representation in Python


class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None

class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * num

    # Add edges
    def add_edge(self, beginning_with, to):
        node = AdjNode(to)
        node.next = self.graph[beginning_with]
        self.graph[beginning_with] = node

        # Make the graph undirected
        node_b = AdjNode(beginning_with)
        node_b.next = self.graph[to]
        self.graph[to] = node_b

    # Print the graph
    def print_agraph(self):
        for i in range(self.V):
            print(f"Vertex {i}:", end="")
            tmp = self.graph[i]
            while tmp is not None:
                print(f" -> {tmp.vertex}", end="")
                tmp = tmp.next
            print()


if __name__ == "__main__":
    pass
    # Create graph and edges
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)

    graph.print_agraph()
