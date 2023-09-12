def findCombinations(A, subarrays, k, out=(),i=0):
    if len(A) == 0 or k > len(A):
        return

    if k == 0:
        subarrays.add(out)
        return

    for j in range(i, len(A)):
        findCombinations(A, subarrays, k - 1, out + (A[j], ), j + 1)

if __name__ == '__main__':
    A = [1, 2, 3]
    subarrays = set()
    k = 2
    findCombinations(A, subarrays, k)
    print(subarrays)