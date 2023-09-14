def longestPalindromeSubseq(text1: str, text2: str) -> int:
        n = len(text2)
        m = len(text1)

        # dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
        dp1 = [0 for i in range(m + 1)]
        dp2 = [0 for i in range(m + 1)]
        # print(dp)

        return LCS(text1, text2, m, n, dp1, dp2)
    
def LCS( text1, text2,m, n, dp1, dp2):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text1[j - 1] == text2[i - 1]:
                dp2[j] = 1 + dp1[j - 1]
            else:
                dp2[j] = max(dp2[j - 1], dp1[j])

        dp1 = dp2.copy()


    return dp2[j]
        

if __name__ == '__main__':
    text1 = 'abc'
    text2 = 'abc'
    print(longestPalindromeSubseq(text1, text2))
