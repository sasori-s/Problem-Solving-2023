from collections import deque

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)



def BFS(graph, source, n):
    discovered = [False] * (n + 1)
    discovered[source] = True

    queue = deque()
    queue.append((source, 0))

    while queue:
        vertex, min_dist = queue.popleft()

        if vertex == n:
            return min_dist

        for u in graph.adjList[vertex]:
            if not discovered[u]:
                discovered[u] = True

                queue.append((u, min_dist + 1))


def findMinumumMovees(snake, ladder):
    n = 10 * 10
    edges = []

    for i in range(n):
        j = 1

        while j <= 6 and i + j <= n:
            src = i
            _snake = snake.get(i + j) if snake.get(i + j) else 0
            _ladder = ladder.get(i+j) if ladder.get(i+j) else 0

            if _snake or _ladder:
                dest = _ladder + _snake
            else:
                dest = i + j

            edges.append((src, dest))

            j += 1
    
    graph = Graph(edges, n)

    return BFS(graph, 0, n)


if __name__ == '__main__':
    snake = {}
    ladder = {}

    ladder[1] = 38
    ladder[4] = 14
    ladder[9] = 31
    ladder[21] = 42
    ladder[28] = 84
    ladder[51] = 67
    ladder[72] = 91
    ladder[80] = 99

    snake[17] = 7
    snake[54] = 34
    snake[62] = 19
    snake[64] = 60
    snake[87] = 36
    snake[93] = 73
    snake[95] = 75
    snake[98] = 79

    print(findMinumumMovees(snake, ladder))