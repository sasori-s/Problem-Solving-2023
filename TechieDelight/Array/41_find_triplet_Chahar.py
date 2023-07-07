def findTriplet(A):
    A.sort()
    n = len(A)

    for i in range(n):
        left = i + 1
        right = n - 1   

        while left < right:
            sum = A[left] + A[right] + A[i]

            if sum == 0:
                return True

            elif sum < 0:
                left += 1

            else:
                right += 1

    return False

if __name__ == "__main__":
    A = [-1, 2, -3, 4, 0, 1]
    print(findTriplet(A))