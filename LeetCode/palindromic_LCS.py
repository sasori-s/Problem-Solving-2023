def longestPalindromeSubseq(s: str) -> int:
        reverse = s[::-1]
        n = len(s)

        # dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
        dp1 = [0 for i in range(n + 1)]
        dp2 = [0 for i in range(n + 1)]
        # print(dp)

        return LCS(s, reverse, n, dp1, dp2)
    
def LCS( original, reverse, n, dp1, dp2):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if original[i - 1] == reverse[j - 1]:
                dp2[j] = 1 + dp1[j - 1]
            else:
                dp2[j] = max(dp2[j - 1], dp1[j])

        dp1 = dp2.copy()


    return dp2[j]
        

if __name__ == '__main__':
    s = 'bbbab'
    print(longestPalindromeSubseq(s))
