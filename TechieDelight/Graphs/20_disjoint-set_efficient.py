class DisjointSet:
    parent = {}
    rank = {}

    def makeSet(self, universe):
        for i in universe:
            self.parent[i] = i
            self.rank[i] = 0

    def Find(self, k):
        if self.parent[k] != k:
            self.parent[k] = self.Find(self.parent[k])

        return self.parent[k]

    def Union(self, a, b):
        x = self.Find(a)
        y = self.Find(b)

        if x == y:
            return 

        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        elif self.rank[y] < self.rank[x]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            self.rank[y] += 1

def printSets(universe, ds):
    print([ds.Find(i) for i in universe])

if __name__ == '__main__':
    universe = [1, 2, 3, 4, 5]

    ds = DisjointSet()

    ds = DisjointSet()
 
    # create a singleton set for each element of the universe
    ds.makeSet(universe)
    printSets(universe, ds)
 
    ds.Union(4, 3)        # 4 and 3 are in the same set
    printSets(universe, ds)
 
    ds.Union(2, 1)        # 1 and 2 are in the same set
    printSets(universe, ds)
 
    ds.Union(1, 3)        # 1, 2, 3, 4 are in the same set
    printSets(universe, ds)
 