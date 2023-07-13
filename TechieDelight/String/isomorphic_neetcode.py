def isomorphic(X, Y):
    mapXY, mapYX = {}, {}

    for i in range(len(X)):
        char_x, char_y = X[i], Y[i]

        if (char_x in mapXY and mapXY[char_x]!=char_y) or \
            (char_y in mapYX and mapYX[char_y] != char_x):
            return False
        
        mapXY[char_x] = char_y
        mapYX[char_y] = char_x

    return True


if __name__ == "__main__":
    X = 'ACAB'
    Y = 'XCXY'

    if isomorphic(X, Y):
        print(f"{X} and {Y} are isomorphic")
    else:
        print(f"{X} and {Y} are not isomorphic")