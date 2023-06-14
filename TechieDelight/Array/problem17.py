def findMajorityElement(A):
    n = len(A)
    for i in range(n // 2):
        count = 1
        for j in range(i + 1, n):
            if A[i] == A[j]:
                count += 1
            
            if count > n//2:
                # return A[i]
                print("The majority element is, ", A[i])
            
    return -1

if __name__ == "__main__":
    A = [2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]
    findMajorityElement(A)
    