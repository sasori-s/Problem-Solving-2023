def findLogestBitonic(A):
    I = [1] * len(A)
    D = [1] * len(A)

    for i in range(1, len(A)):
        if A[i - 1] < A[i]:
            I[i] = I[i-1] + 1

    for i in reversed(range(len(A) - 1)):
        if A[i] > A[i + 1]:
            D[i] = D[i + 1] + 1

    lbs_len = 0
    start = end = 0

    for i in range(len(A)):
        if lbs_len < I[i] + D[i] -1:
            lbs_len = I[i] + D[i] - 1
            start = i - I[i] + 1
            end = i + D[i] - 1

    print('The length of the longest bitonic subarray is: ', lbs_len)
    print("The longest bitonic subarray is: ", A[start:end+1])


if __name__ == '__main__':
    A = [3, 5, 8, 4, 5, 9, 10, 8, 5, 3, 4]

    findLogestBitonic(A)