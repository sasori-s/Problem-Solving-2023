def isInterLeaving(s1, s2, s3, i, j):
    if len(s1) + len(s2) != len(s3):
        return False

    dp = [[False] * (len(s2) + 1) for i in range(len(s1)+1)]
    dp[len(s1)][len(s2)] = True

    for i in range(len(s1), -1, -1):
        for j in range(len(s2), -1, -1):
            if i < len(s1) and s1[i] == s3[i + j] and dp[i+1][j]:
                dp[i][j] = True
            
            if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                dp[i][j] = True

    return dp[0][0]

if __name__ == "__main__":
    str1 = 'aabcc'
    str2 = 'dbbca'
    str3 = 'aadbbcbcac'
    dp = {}

    print(isInterLeaving(str1, str2, str3, 0, 0))