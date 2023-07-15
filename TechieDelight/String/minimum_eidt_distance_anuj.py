def editDistance(a, b):
    m = len(a)
    n = len(b)

    dp = [[1 for i in range(n+1)]for i in range(m+1)]

    for i in range(1, m+1): dp[i][0] = i
    for j in range(1, n+1): dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            
            else:
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

    return dp[i][j]

if __name__ == "__main__":
    a = 'ABCAB'
    b = 'EACB'
    print(editDistance(b, a))