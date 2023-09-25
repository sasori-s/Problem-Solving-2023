import sys

def getPath(vertex, parent):
    if vertex < 0:
        return []

    return getPath(parent[vertex], parent) + [vertex]


def bellmanFord(edges, _source, n):
    parent = [-1] * n
    distance = [sys.maxsize] * n

    distance[_source] = 0

    for i in range(n - 1):
        for (source, dest, weight) in edges:
            if distance[source] != sys.maxsize and distance[dest] > distance[source] + weight:
                distance[dest] = distance[source] + weight

                parent[dest] = source

    for (source, dest, weight) in edges:
            if distance[source] != sys.maxsize and distance[dest] > distance[source] + weight:
                print("Negative weight cycle has been found")
                return

    # print(source, distance)
    # print(parent)

    for i in range(n):
        if i != source and distance[i] != sys.maxsize:
            print(f"The shortest path from {i} to {_source} with weight {distance[i]} is {getPath(i, parent)} ")
            

if __name__  == '__main__':
    edges = [
        (0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2),
        (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)
    ]

    n = 5

    for source in range(n):
        bellmanFord(edges, source,  n)