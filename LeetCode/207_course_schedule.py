def DFS(graph, n, departure, discovered, node, time):
    discovered[node] = True

    for u in range(n):
        if graph[node][u] == 1 and not discovered[u]:
            time = DFS(graph, n, departure, discovered, u, time)

    departure[node] = time
    time += 1

    return time

    


def isDaG(graph, n):
    departure = [-1] * n 

    discovered = [False] * n
    
    time = 0

    for i in range(n):
        if not discovered[i]:
            time = DFS(graph, n, departure, discovered, i, time)

    for u in range(n):
        for v in range(n):
            if graph[u][v] == 1 and departure[u] <= departure[v]:
                return False
            
    return True


if __name__ == '__main__':
    prerequisites = [[1,0]]
    n = 2

    graph = [[0 for _ in range(n)] for _ in range(n)]

    for u in prerequisites:
            graph[u[0]][u[1]] = 1

    print(isDaG(graph, n))