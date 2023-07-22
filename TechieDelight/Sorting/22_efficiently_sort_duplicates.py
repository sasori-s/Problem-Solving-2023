RANGE =100
def customSort(A):
    freq = [0] * RANGE

    for i in A:
        freq[i] += 1 
        
    k = 0
    for i in range(RANGE):
        while freq[i] > 0:
            A[k] = i
            k += 1
            freq[i] = freq[i] - 1
            


if __name__ == "__main__":
    A = [4, 2, 40, 10, 10, 1, 4, 2, 1, 10, 40]
    customSort(A)
    print(A)