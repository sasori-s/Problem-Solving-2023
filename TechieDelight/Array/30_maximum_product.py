def findMaximumProduct(A):
    if not len(A):
        return
    
    max_ending = min_ending = A[0]
    max_so_far = A[0]

    for i in range(1, len(A)):
        temp = max_ending

        max_ending = max(A[i], max(A[i] * max_ending, A[i] * min_ending))
        min_ending = min(A[i], min(A[i] * temp, A[i] * min_ending))

        max_so_far = max(max_so_far, max_ending)

    return max_so_far

if __name__ == "__main__":
    A = [-6, 4, -5, 8, -10, 0, 8]
    print("The maximum product of a sublist is ", findMaximumProduct(A))