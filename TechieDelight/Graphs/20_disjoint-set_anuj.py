# class DisjointUnionSet:
#     def __init__(self, n) :
#         rank = [None] * n
#         parent = [None] * n

#         self.n = n

#         for i in range(n):
#             parent[i] = i

# def find(x):
#     if parent[x] != x

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]

def union(parent, rank, a, b):
    xRoot = find(parent, a)
    yRoot = find(parent, b)

    if xRoot == yRoot:
        return 

    if rank[xRoot] < rank[yRoot]:
        parent[xRoot] = yRoot

    elif range[yRoot] < range[xRoot]:
        parent[yRoot] = xRoot

    else:
        parent[xRoot] = yRoot
        range[yRoot] += 1

if __name__ == '__main__':
    n = 10
    rank = [0] * n
    parent = [None] * n

    for i in range(n):
        parent[i] = i