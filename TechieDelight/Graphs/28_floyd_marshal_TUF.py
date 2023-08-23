import sys

def shortestDistance(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == -1:
                matrix[i][j] = sys.maxsize
            
            if i == j:
                matrix[i][j] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == sys.maxsize:
                matrix[i][j] = - 1

                