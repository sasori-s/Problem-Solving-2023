def findPalindromes(word, n, dp, left, right):
    if left > right:
        return 0
    
    if left == right:
        return 1
    
    if dp[left][right] != -1:
        return dp[left][right]
    
    if word[left] == word[right]:
        dp[left][right] =  1 + findPalindromes(word, n, dp, left + 1, right) + findPalindromes(word, n, dp, left, right - 1)

        return dp[left][right]
    else:
        dp[left][right] =  findPalindromes(word, n, dp, left + 1, right) + findPalindromes(word, n, dp, left, right - 1) - findPalindromes(word, n, dp, left + 1, right - 1)

        return dp[left][right]
    
    

if __name__ == '__main__':
    word = 'bccb'
    n = len(word)

    dp = [[-1 for _ in range(n)]for _ in range(n)]
    left = 0
    right = n - 1

    count = findPalindromes(word, n, dp, left, right)
    print(count)
