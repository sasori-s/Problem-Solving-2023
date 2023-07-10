def LCS(arr, A, B):
    for i in range(len(A)):
        for j in range(len(B)):
            if i == 0 or j == 0:
                arr[i][j] = 0
            
            if A[i] == B[j]:
                arr[i][j] = 1 + arr[i-1][j-1]

            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])

    print(arr[i][j])


def make2dArray(m, n):
    arr = [[0] * n] * m
    # print(arr)
    return arr

if __name__ == "__main__":
    str1 = "stone"
    str2 = "longest"

    arr = make2dArray(len(str1), len(str2))
    LCS(arr, str1, str2)
