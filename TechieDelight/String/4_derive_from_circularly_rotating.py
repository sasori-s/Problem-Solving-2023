def check(X, Y):
    if len(X) != len(Y):
        return False

    for i in range(len(X)):
        X = X[1:] + X[0]

        if X == Y:
            return True

if __name__ == "__main__":
    X = 'ABCD'
    Y = 'DABC'

    if check(X, Y):
        print("The given string can be derived from each other")
    else:
        print("The given string can not be derived from each other")