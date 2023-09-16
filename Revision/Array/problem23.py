import sys

def kdadaneNeg(A):
    max_sp_far = -sys.maxsize
    max_ending_here = 0

    for i in range(len(A)):
        max_ending_here = max_ending_here + A[i]

        max_ending_here = max(max_ending_here, A[i])

        max_sp_far = max(max_sp_far, max_ending_here)

    return max_sp_far

if __name__ == '__main__':
    A = [-8, -3, -6, -2, -5, -4]
    print("The sum of contiguous sublist with the largest sum is: ", kdadaneNeg(A))