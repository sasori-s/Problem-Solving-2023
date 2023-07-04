def findMaxSum(X, Y):
    m = len(X)
    n = len(Y)

    i = j = 0

    while i < m and j < n:

        while i < m-1 and X[i] == X[i + 1]:
            sum_x += X[i]
            i = i + 1

        
        while j < n - 1 and Y[j] == Y[i+1]:
            sum_y += Y[j]
            j = j + 1

        if Y[j] < X[i]:
            sum_y += Y[j]
            j = j + 1

        elif X[i] < Y[j]:
            sum_x += X[i]
            i = i + 1

        else:
            total += max(sum_x, sum_y) + X[i]
            i += 1
            j += 1

    while i < m:
        sum_x += X[i]
        i += 1

    while j < n:
        sum_y += Y[j]
        j += 1

    
    total += max(sum_x, sum_y)
    return total

if __name__ == "__main__":
    X = [3, 6, 7, 8, 10, 12, 15, 18, 100]
    Y = [1, 2, 3, 5, 7, 9, 10, 11, 15, 16, 18, 25, 50]
 
    print("The maximum sum is ", findMaxSum(X, Y))