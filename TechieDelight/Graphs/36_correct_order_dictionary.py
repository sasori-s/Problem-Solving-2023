class Graph:
    def __init__(self, N):
        self.adjList = [[] for _ in range(N)]

def printGraph(graph, d):
    for i in range(N):
        if graph.adjList[i]:
            print(d[i], '->', [d[v] for v in graph.adjList[i]])

def DFS(graph, v, discovered, departure, time):
    discovered[v] = True
    time += 1

    for u in graph.adjList[v]:
        if not discovered[u]:
            time = DFS(graph, u, discovered, departure, time)

    departure[time] = v
    return time + 1

def doTopologicalSort(graph, d):
    departure = [-1] * (2 * N)

    discovered = [False] * N
    time = 0 

    for i in range(N):
        if not discovered[i] and len(graph.adjList[i]):
            time = DFS(graph, i,  discovered, departure, time)

    for i in reversed(range(2 * N)):
        if departure[i] != -1:
            print(d[departure[i]], end=" ")

def findAlphabetsOrder(dictionary):
    d = {}

    k = 0

    for word in dictionary:
        for s in word:
            d.setdefault(s, k)
            k += 1

    graph = Graph(N)

    for i in range(1, len(dictionary)):
        prev = dictionary[i - 1] 
        curr = dictionary[i]

        j = 0

        while j < len(curr) and j < len(prev):
            if prev[j] is not curr[j]:
                graph.adjList[d[prev[j]]].append(d[curr[j]])
                break

            j += 1

    reverse = dict((v, u) for u, v in d.items())

    printGraph(graph, reverse)
    doTopologicalSort(graph, reverse)

if __name__ == '__main__':
    N = 100

    dictionary = [
        ["¥", "€", "±"],
        ["€", "±", "€"],
        ["€", "±", "‰", "ð"],
        ["ð", "ß"],
        ["±", "±", "ð"],
        ["±", "ß", "ß"]
    ]

    findAlphabetsOrder(dictionary)
