import sys

def findSublist(A, k):
    if not len(A) or k >= len(A):
        return
    
    window_sum = 0
    min_window = sys.maxsize

    last = 0

    for i in range(len(A)):
        window_sum += A[i]

        if i + 1 >= k:
            if min_window > window_sum:
                min_window = window_sum
                last = i
            
            window_sum -= A[i - k + 1]

    print(f"Minimum sum of the sublist is {(last - k + 1, last)}")


if __name__ == "__main__":
    A = [10, 4, 2, 5, 6, 3, 8, 1]
    k = 3

    findSublist(A, k)