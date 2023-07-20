def countSort(A, k):
    output = [0] * len(A)

    freq = [0] * (k + 1)

    for i in A:
        freq[i] += 1
    
    total = 0

    for i in range(k + 1):
        oldCount = freq[i]
        freq[i] = total
        total += oldCount

    for i in A:
        output[freq[i]] = i
        freq[i] += 1

    for i in range(len(A)):
        A[i] = output[i]



if __name__ == "__main__":
    A = [4, 2, 10, 10, 1, 4, 2, 1, 10]
    k = 10
    countSort(A, k)
    print(A)