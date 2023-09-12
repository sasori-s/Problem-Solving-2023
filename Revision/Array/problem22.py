import sys

def maximumDifference(A):
    n = len(A)
    max_diff = -sys.maxsize 
    max_element = A[n - 1]

    if n == 0:
        return max_diff

    for i in reversed(range(n)):
        if A[i] > max_element:
            max_element = A[i]

        else:
            max_diff = max(max_diff, max_element - A[i])

    return max_diff

if __name__ == '__main__':
    A = [2, 7, 9, 5, 1, 3, 5]

    diff = maximumDifference(A)
    if diff != -sys.maxsize:
        print("The maximum difference is: ", diff)

