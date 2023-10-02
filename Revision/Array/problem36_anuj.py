import sys

def findMaxProfit(A):
    min_so_far = sys.maxsize
    max_profit = -sys.maxsize

    for i in range(len(A)):
        min_so_far = min(min_so_far, A[i]) 
        max_profit = max(max_profit, A[i] - min_so_far)

    print(f"Max profit is {max_profit}")


if __name__ == '__main__':
    A = [1, 5, 2, 3, 7, 6, 4, 5]

    findMaxProfit(A)