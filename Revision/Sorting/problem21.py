def customSort(first, second):
    freq = {}

    for i in first:
        freq[i] = freq.get(i, 0) + 1

    index = 0

    for i in second:
        n = freq.setdefault(i, 0)

        for _ in range(n):
            first[index] = i
            index += 1

        freq.pop(i)

    for key in sorted(freq.keys()):
        count = freq.get(key)

        while count:
            first[index] = key
            index += 1
            count -= 1



if __name__ == '__main__':
    first = [5, 8, 9, 3, 5, 7, 1, 3, 4, 9, 3, 5, 1, 8, 4]
    second = [3, 5, 7, 2]

    customSort(first, second)
    print("After sorting the list is: ", first)