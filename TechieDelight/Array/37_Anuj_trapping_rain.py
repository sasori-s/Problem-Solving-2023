def trappingWater(A):
    n = len(A)
    left = [0] * n
    right = [0] * n

    left[0] = A[0]

    for i in range(1, n):
        left[i] = max(left[i - 1], A[i])

    right[n - 1] = A[n - 1]

    for j in reversed(range(n - 1)):
        right[j] = max(right[j + 1], A[j])

    ans = 0

    for i in range(n):
        ans += min(left[i], right[i]) - A[i]

    return ans



if __name__ == "__main__":
    A = [3, 1, 2, 4, 0, 1, 3, 2]
    print("Total water blocks can be trapped is, ", trappingWater(A))