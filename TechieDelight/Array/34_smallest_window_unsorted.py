import sys

def findSublist(A):
    leftIndex = rightIndex = -1
    max_so_far = -sys.maxsize

    for i in range(len(A)):
        if max_so_far < A[i]:
            max_so_far = A[i]

        if A[i] < max_so_far:
            rightIndex = i

    min_so_far = sys.maxsize

    for i in reversed(range(len(A))):
        if min_so_far > A[i]:
            min_so_far = A[i]

        if A[i] > min_so_far:
            leftIndex = i

    if leftIndex == -1:
        print("Array is already sorted")
        return
    
    print(f"Sort the list from {leftIndex} to {rightIndex}")


if __name__ == "__main__":
    A = [1, 3, 2, 7, 5, 6, 4, 8]
    findSublist(A)