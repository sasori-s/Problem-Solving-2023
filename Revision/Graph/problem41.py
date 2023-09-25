class Graph:
    def __init__(self, edges, n) :
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


def colorGraph(graph, n):
    result = {}

    for v in range(n):
        assigned = [result.get(i) for i in graph.adjList[v] if i in result ]

        color = 1
        for c in assigned:
            if c != color:
                break

            color = color + 1

        result[v] = color

    for u in range(n):
        print(f"color assigned to the vertex {u} is {colors[result[u]]}")


if __name__ == '__main__':
    colors = [
        '', 'BLUE', 'GREEN', 'RED', 'YELLOW', 'ORANGE', 'PINK',
            'BLACK', 'BROWN', 'WHITE', 'PURPLE', 'VOILET'
    ]

    edges = [
        (0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)
    ]

    n = 6

    graph = Graph(edges, n)
    colorGraph(graph, n)