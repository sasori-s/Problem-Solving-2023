from collections import deque
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)

def BFS(adj, V, v, answer, inDegree):
    queue = deque()

    for i in range(V):
        if inDegree[i] == 0:
            queue.append(i)

    while queue:
        current = queue.popleft()

        answer.append(current)

        for u in adj[current]:
            inDegree[u] -= 1
            if inDegree[u] == 0:
                queue.append(u)

    return answer

def topologicalSort(adj, V):
    inDegree = [0] * V

    # for key in adj.keys():
    #     inDegree[key] += 1

    for i in adj:
        for j in i:
            inDegree[j] += 1

    # print(inDegree)
    answer = [] 
    visited = [False] * V

    return BFS(adj, V, 0,answer, inDegree)

if __name__ == '__main__':
    edges = [
        (0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)
    ]

    n = 8
    graph = Graph(edges, n)
    print(topologicalSort(graph.adjList, n))