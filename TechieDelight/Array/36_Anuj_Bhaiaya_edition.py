def findMaxProfit(A):
    min_so_far = 0
    max_so_far = 0
    profit = 0

    for i in range(len(A)):
        min_so_far = min(min_so_far, A[i])
        profit = A[i] - min_so_far
        max_so_far = max(profit, max_so_far)

    return max_so_far


if __name__ == "__main__":
    A = [3,1, 4, 8, 7, 2,5]
    print("The maximum profit is, ", findMaxProfit(A))