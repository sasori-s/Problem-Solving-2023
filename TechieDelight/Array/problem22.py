import sys
def getMaxDif(A):
    diff = -sys.maxsize

    n = len(A)
    if n == 0:
        return diff
    
    max_so_far = A[n - 1]
    
    for i in reversed(range(n - 1)):
        if A[i] > max_so_far:
            max_so_far = A[i]

        else:
            diff = max(diff, max_so_far - A[i])
            if diff == max_so_far - A[i]:
                starting_element = A[i]

    print("The pair having maximum difference is ", (starting_element, max_so_far))
    
    return diff


if __name__ == "__main__":
    A = [ 2, 7, 9, 5, 1, 3, 5]
    diff = getMaxDif(A)
    
    if diff != -sys.maxsize:
        print("The maximum difference is ", diff)