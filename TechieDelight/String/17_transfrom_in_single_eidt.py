def checkEditDistance(first, second):
    i = j = 0
    m = len(first)
    n = len(second)

    if abs(m-n) > 1:
        return False

    edits = 0

    while i < m and j < n:
        if first[i] != second[j]:
            if m > n:
                i = i + 1

            elif m < n:
                j = j + 1

            else:
                i += 1
                j += 1

            edits += 1

        else:
            j += 1
            i += 1

        
    if i < m:
        edits = edits + 1

    if j < n:
        edits = edits + 1

    return edits == 1


if __name__ == "__main__":
    print(checkEditDistance("xyz", "xz"))       # True
    print(checkEditDistance("xyz", "xyyz"))     # True
    print(checkEditDistance("xyz", "xyx"))      # True
    print(checkEditDistance("xyz", "xxx"))