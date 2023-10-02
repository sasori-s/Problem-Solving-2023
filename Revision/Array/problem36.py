def findMaxProfit(A):
    profit = 0

    for i in range(1, len(A)):
        if A[i-1] < A[i]:
            profit += A[i] - A[i - 1]

    print(f'The max profit can be earned is {profit}')

if __name__ == '__main__':
    A = [1, 5, 2, 3, 7, 6, 4, 5]
    findMaxProfit(A)