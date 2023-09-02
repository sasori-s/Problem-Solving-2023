def editDistance(x, y):
    m = len(x) + 1
    n = len(y) + 1

    dp = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        dp[i][0] = i

    for j in range(n):
        dp[0][j] = j

    for i in range(1, m):
        for j in range(1, n):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            else:
                dp[i][j] = 1 +  min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])

    return dp[m - 1][n - 1]
    

if __name__ == '__main__':
    x = 'AVCAB'
    y = 'EACB'

    operations = editDistance(x, y)
    print(operations)