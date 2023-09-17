import sys

def findSublist(A):
    max_so_far = -sys.maxsize

    for i in range(len(A)):
        if max_so_far < A[i]:
            max_so_far = A[i]

        if max_so_far > A[i]:
            rightIndex = i

    min_so_far = sys.maxsize

    for i in reversed(range(len(A))):
        if min_so_far > A[i]:
            min_so_far = A[i]

        if min_so_far < A[i]:
            leftindex = i

    if leftindex == -1:
        print("Array is already sorted")
        return

    print(f"Sort list from index {leftindex} to {rightIndex}")
        


if __name__ == '__main__':
    A = [1, 3, 2, 7, 5, 6, 4, 8]
    findSublist(A)

    