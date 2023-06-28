def findCombinations(A, out, k, i, n):
    if len(out) == k:
        print(out)
        return

    for j in range(i, n):
        out.append(A[j])

        findCombinations(A, out, k, j, n)
        out.pop()

if __name__ == "__main__":
    A = [1, 2, 3]
    k = 2

    out = []
    findCombinations(A, out, k, 0, len(A))
