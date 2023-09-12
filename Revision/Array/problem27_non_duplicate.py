def findCombinations(A, k, i=0, out=[]):
    if len(out) == k:
        print(out)
        return

    j = i

    while j < len(A):
        out.append(A[j])
        findCombinations(A, k, j, out)

        out.pop()

        while j < len(A) - 1 and A[j] == A[j+1]:
            j += 1

        j += 1

if __name__ == '__main__':
    A = [1, 2, 1]
    k = 2

    A.sort()
    findCombinations(A, k)