def findInterleavings(X, Y, interleavings, curr=''):
    if not X and not Y:
        interleavings.add(curr)
        return

    if X:
        findInterleavings(X[1:], Y, interleavings, curr + X[0])

    if Y:
        findInterleavings(X, Y[1:], interleavings, curr + Y[0])

    
    return interleavings

def findAllInterleavings(X, Y):
    interleavings = set()

    if not X and not Y:
        return interleavings

    findInterleavings(X, Y, interleavings)
    return interleavings

if __name__ == "__main__":
    X = 'ABC'
    Y = 'ACB'

    interleavings = findAllInterleavings(X, Y)
    print(interleavings)