

import collections


def bfs(graph, root):
    queue = collections.deque([root])
    visited = set(), 

    visited.add(root)

    while queue:
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        for i in graph[vertex]:
            if i not in visited:
                visited.add(i)
                queue.append(i)

if __name__ == '__main__':
    graph = {0: set([1, 2, 3]),
         1: set([2]),
         2: set([4]),
         3: set([]),
         4: set([]),
         }
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)
