def isAnagram(X, Y):
    if len(X) != len(Y):
        return False

    frequency = {}

    for i in range(len(X)):
        frequency[X[i]] = frequency.get(X[i], 0) + 1

    for i in range(len(Y)):
        if not Y[i] in frequency:
            return False

        frequency[Y[i]] = frequency[Y[i]] - 1

        if frequency[Y[i]] == 0:
            del frequency[Y[i]]

    return not frequency


if __name__ == "__main__":
    X = 'tommarvoloriddle'
    Y = 'iamlordvoldemort'

    if isAnagram(X, Y):
        print("Anagram")
    else:
        print("Not anagram")