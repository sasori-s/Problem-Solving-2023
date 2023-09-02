import sys

def minCoins(n, coins):
    if n == 0 :
        return 0 

    answer = sys.maxsize

    for i in coins:
        if n - i >= 0:
            subAns = minCoins(n - i, coins)
            
            if subAns != sys.maxsize and subAns + 1 < answer:
                answer = subAns + 1

    return answer

if __name__ == '__main__':
    n = 18
    coins = [7, 5, 1]

    ans = minCoins(n, coins)
    print(ans)