from collections import deque

class Graph:
    indegree = None

    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        self.indegree = [0] * n

        for (src, dest) in edges:
            self.adjList[src].append(dest)

            self.indegree[dest] = self.indegree[dest] + 1

def topologicalSort(graph, n):
    sorted_elements = []
    indegree = graph.indegree

    queue = deque([i for i in range(n) if indegree[i] == 0])

    while queue:
        current = queue.pop()
        sorted_elements.append(current)

        for u in graph.adjList[current]:
            indegree[u] -= 1

            if indegree[u] == 0:
                queue.append(u)

    for i in range(n):
        if indegree[i]:
            return None

    return sorted_elements

if __name__ == '__main__':
    edges = [
        (0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)
    ]

    n = 8

    graph = Graph(edges, n) 

    topological = topologicalSort(graph, n)
    if topological:
        print(topological)
    else:
        print("The graph has at least one cycle. Topological sorting is not possible")