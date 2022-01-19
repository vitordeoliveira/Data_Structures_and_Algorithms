# Adjacency Matrix representation in Python for a undirected graph
import time


class Graph(object):

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def add_edge(self, x, y):
        self.adjMatrix[x][y] = 1
        self.adjMatrix[y][x] = 1

    # Remove edges
    def remove_edge(self, x, y):
        self.adjMatrix[x][y] = 0
        self.adjMatrix[y][x] = 0

    # Print the matrix
    def print_matrix(self):
        for x in range(self.size):
            print("------"*self.size)
            print("|  ", end="")
            for y in range(self.size):
                print(self.adjMatrix[x][y], end="  |  ", flush=True)
                time.sleep(0.05)
            print()
        print("------"*self.size)


def main():
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(1, 2)

    g.print_matrix()


if __name__ == '__main__':
    main()
