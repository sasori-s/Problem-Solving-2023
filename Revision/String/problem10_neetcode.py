def isIsomorphic(x, y):
    if len(x) != len(y):
        return False

    mapXY = {}
    mapYX = {}

    for i in range(len(x)):
        charx = x[i]
        chary = y[i]

        if (charx in mapXY and mapXY[charx] != chary) or (chary in mapYX and mapYX[chary] != charx):
            return False

        mapXY[charx] = chary
        mapYX[chary] = charx

    return True


if __name__ == '__main__':
    x = 'ACAB'
    y = 'XCXY'

    if isIsomorphic(x, y):
        print(f'{x} and {y} are isomorphic')
    else:
        print(f'{x} and {y} are not isomorphic')