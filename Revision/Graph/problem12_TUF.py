from collections import deque

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)


def topologicalSort(graph, n):
    indegree = [0] * n
    queue = deque()

    for i in range(n):
        for vertex in graph.adjList[i]:
            indegree[vertex] += 1


    print(indegree)

    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
    
    print(queue)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for u in graph.adjList[vertex]:
            indegree[u] -= 1
            if indegree[u] == 0:
                queue.append(u)
    


    


if __name__ == '__main__':
    edges = (0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)
    n = 8

    graph = Graph(edges, n)

    topologicalSort(graph, n)