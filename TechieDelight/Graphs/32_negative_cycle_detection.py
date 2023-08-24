import sys
INF = sys.maxsize

def floydMarshal(adjMatrix):
    if not adjMatrix:
        return

    n = len(adjMatrix)

    cost = [[adjMatrix[u][v] for u in range(n)] for v in range(n)]

    for k in range(n):
        for v in range(n):
            for u in range(n):
                if cost[v][k] != INF and cost[k][u] != INF \
                    and cost[v][k] + cost[k][u] < cost[v][u]:
                    cost[v][u] = cost[v][k] + cost[k][u]

            if cost[v][v] < 0:
                print("Negative weight cycle exists")
                return

    print("Negative-weight cycle doest doesn\'t exist")

if __name__ == '__main__':
    adjMatrix = [
        [0, INF, -2, INF],
        [4, 0, -3, INF],
        [INF, INF, 0, 2],
        [INF, -1, INF, 0]
    ]

    floydMarshal(adjMatrix)