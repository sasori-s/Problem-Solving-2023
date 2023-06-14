def findEquilibriumindex(A):
    left = [0] * len(A)

    for i in range(1, len(A)):
        left[i] = left[i - 1] + A[i - 1]
    # print(left)

    right = 0
    indeces = []

    for i in reversed(range(len(A))):
        if left[i] == right:
            indeces.append(i)

        right += A[i]

    print("The Equiribirum point is ", indeces)

if __name__ == "__main__":
    A = [0, -3, 5, -4, -2, 3, 1, 0]
    findEquilibriumindex(A)