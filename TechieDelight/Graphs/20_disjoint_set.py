class DisjointSet:
    parent = {}

    def makeSet(self, universe):
        for i in universe:
            self.parent[i] = i

    def find(self, k):
        if self.parent[k] == k:
            return k
        
        return self.find(self.parent[k])

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)

        if x == y:
            return 

        else:
            self.parent[x] = y

def printSets(universe, ds):
    print([ds.find(i) for i in universe])

if __name__ == '__main__':
    universe = [1, 2, 3, 4, 5]

    ds = DisjointSet()
    ds.makeSet(universe)
    printSets(universe, ds)

    ds.union(4, 3) # 4 and 3 are in the same set
    printSets(universe, ds)