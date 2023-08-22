class DisjointSets:
    parent = {}

    def makeSet(self, n):
        for i in range(n):
            self.parent[i] = i

    def find(self, k):
        if self.parent[k] == k:
            return k

        return self.find(self.parent[k])

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)

        self.parent[x] = y

def runKruskal(edges, n):
    MST = []

    ds = DisjointSets()
    ds.makeSet(n)

    index = 0

    edges.sort(key=lambda x: x[2])

    while len(MST) != n -1:
        (src, dest, weight) = edges[index]
        index += 1
        x = ds.find(src)
        y = ds.find(dest)

        if x != y:
            MST.append((src, dest, weight))
            ds.union(x, y)

    return MST

if __name__ == '__main__':
    edges = [
        (0, 1, 7), (1, 2, 8), (0, 3, 5), (1, 3, 9), (1, 4, 7), (2, 4, 5),
        (3, 4, 15), (3, 5, 6), (4, 5, 8), (4, 6, 9), (5, 6, 11)
    ]
    
    n = 7

    e = runKruskal(edges, n)
    print(e)