def customSort(A):
    freq = {}

    for i in A:
        freq[i] = freq.get(i, 0) + 1

    index = 0
    for key in sorted(freq.keys()):
        val = freq.get(key)

        while val > 0:
            A[index] = key
            index += 1
            val -= 1

if __name__ == '__main__':
    A = [4, 2, 40, 10, 10, 1, 4, 2, 1, 10, 40]
    customSort(A)
    print(A)