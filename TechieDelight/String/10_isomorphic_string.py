def isomorphic(X, Y):
    if len(X) != len(Y):
        return False

    d = {}
    s = set()

    for i in range(len(X)):
        x = X[i]
        y = Y[i]

        if x in d:
            if d[x] != y:
                return False

        else:
            if y in s:
                return False
            
            d[x] = y
            s.add(y)

    return True

if __name__ == "__main__":
    X = 'ACAB'
    Y = 'XCXY'

    if isomorphic(X, Y):
        print(f"{X} and {Y} are isomorphic")
    else:
        print(f"{X} and {Y} are not isomorphic")