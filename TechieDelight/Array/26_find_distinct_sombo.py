def findCombinations(A, k, subarrays, out=(), i=0):
    if len(A) == 0 or k > len(A):
        return

    if k == 0:
        subarrays.add(out)
        return
    
    for j in range(i, len(A)):
        findCombinations(A, k - 1, subarrays, out + (A[j], ), j + 1)

if __name__ == "__main__":
    A = [1, 2, 3]
    k = 2
    subarrays = set()

    findCombinations(A, k, subarrays)
    print(subarrays)
