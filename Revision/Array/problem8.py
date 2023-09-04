import sys

def findMaxProduct(A):
    max1 = A[0]
    max2 = -sys.maxsize

    min1 = A[0]
    min2 = sys.maxsize

    for i in range(1, len(A)):
        if A[i] > max1:
            max2 = max1
            max1 = A[i]

        elif A[i] > max2:
            max2 = A[i]

        if A[i] < min1:
            min2 = min1
            min1 = A[i]

        elif A[i] < min2:
            min2 = A[i]


    print(min1, min2, max1, max2)
        
    if -(min1 * min2) < max1 * max2:
        print(f"The largest prodduct is {min1 , min2}")
    else:
        print(f"The largest product is {max1 , max2}")

            

if __name__ == "__main__":
    A = [-10, -4, 5, 6, -2]
    findMaxProduct(A)