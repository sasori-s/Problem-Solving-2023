from collections import deque
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)

def BFS(g, source, n):
    q = deque()
    discovered = [False] * (n + 1)

    discovered[source] = True

    q.append((source, 0))

    while q:
        vertex, min_dist = q.popleft()

        if vertex == n:
            return min_dist

        for u in g.adjList[vertex]:
            if not discovered[u]:
                discovered[u] = True

                q.append((u, min_dist + 1))

def findMinimumMoves(ladder, snake):
    n = 100

    edges = []
    for i in range(n):
        j = 1

        while j <= 6 and i + j <= n:
            src = i

            _ladder = ladder.get(i + j) if (ladder.get(i+j)) else 0
            _snake = snake.get(i + j) if (snake.get(i+j)) else 0

            if _ladder or _snake:
                dest = _ladder + _snake
            else:
                dest = i + j
            
            edges.append((src, dest))

            j += 1

    g = Graph(edges, n)
    return BFS(g, 0, n)

if __name__ == '__main__':
    ladder = {}
    snake = {}

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
 
    print(findMinimumMoves(ladder, snake))