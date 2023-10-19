def isSafe(graph, N, m, color, col, node):
    for k in range(N):
        if k != node and graph[k][node] == 1 and color[k] == col:
            return False

    return True


def solvable(graph, N, m, color, node):
    if node == m:
        return True
    
    for i in range(1, N + 1):
        if isSafe(graph, N, m, color, i, node):
            color[node] = i
            if solvable(graph, N, m, color, node + 1):
                return True
            color[node] = 0

    return False


def graphColoring(graph, N, m):
    color = [0] * N
    
    if solvable(graph, N, m, color, 0):
        return True
    
    return False


if __name__ == '__main__':
    graph = [[0 for i in range(50)] for j in range(50)]

    m = 3
    N = 4

    graph[0][1] = 1
    graph[1][0] = 1
    graph[1][2] = 1
    graph[2][1] = 1
    graph[2][3] = 1
    graph[3][2] = 1
    graph[3][0] = 1
    graph[0][3] = 1
    graph[0][2] = 1
    graph[2][0] = 1

    print(1 if graphColoring(graph, N, m) else 0)