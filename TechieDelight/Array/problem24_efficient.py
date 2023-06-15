import sys
def kadane(A):
    if len(A) <= 1:
        return A
    
    start = end = 0
    max_so_far = -sys.maxsize
    max_ending_here = 0

    beg = 0

    for i in range(len(A)):
        max_ending_here = max_ending_here + A[i]

        if max_ending_here < A[i]:
            max_ending_here = A[i]
            beg = i

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = beg
            end = i

    print(f"The continious subarray with maximum sum is {A[start : end + 1]}")

if __name__ == '__main__':
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    kadane(A)
