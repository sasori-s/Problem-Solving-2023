def findMaximumProduct(A):
    n = len(A)

    if n < 2:
        return
    
    A.sort()

    if (A[0] * A[1]) > (A[n - 1] * A[n - 2]):
        print("The pair is ", (A[0],  A[1]))

    else:
        print("Pair is", (A[n - 1], A[n - 2])) 


if __name__ == '__main__':
 
    A = [-10, -3, 5, 6, -20]
    findMaximumProduct(A)
