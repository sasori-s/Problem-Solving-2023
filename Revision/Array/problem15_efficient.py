def findEquilibriumIndex(A):
    total = sum(A)

    right = 0

    indices = []

    for i in reversed(range(len(A))):
        if right == total - A[i] - right:
            indices.append(i)

        right += A[i]

    print(f"Equilibrium indices are {indices}")

if __name__ == '__main__':
    A = [0, -3, 5, -4, -2, 3, 1, 0]

    findEquilibriumIndex(A)