def rearrange(arr):
    arr.sort()
    n = len(arr)
    i, j = 0, n - 1
    A = [0] * n
    k = 0

    while i <= j:
        if i == j:
            A[k] = arr[i]

        else:
            A[k] = arr[i]
            A[k + 1] = arr[j]

        i += 1
        j -= 1
        k += 2
    print(A)

if __name__ == "__main__":
    arr = [4, 2, 1, 3, 5]
    rearrange(arr)
    