import sys

def findSmallestSublistLen(A, k):
    length = sys.maxsize
    left = 0
    window_sum = 0

    for right in range(len(A)):
        window_sum += A[right]

        while window_sum > k and left <= right:
            length = min(length, right - left + 1)
            window_sum -= A[left]
            left += 1

    if length == sys.maxsize:
        return 0

    return length    
    

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 21
    
    length = findSmallestSublistLen(A, k)

    if length != sys.maxsize:
        print(f"The smallest sublist length is {length}")

    else:
        print("No sublist exits")