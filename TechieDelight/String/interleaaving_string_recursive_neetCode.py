def dfs(dp, s1, s2, s3, i, j):
    if len(s1) == i and len(s2) == j:
        return True

    if (i, j) in dp:
        return dp[(i, j)]

    if i < len(s1) and s1[i] == s3[i+j] and dfs(dp, s1, s2, s3, i+1, j):
        return True
    
    if j < len(s2) and s2[j] == s3[i + j] and dfs(dp, s1, s2, s3, i, j+1):
        return True

    dp[(i, j)] = False
    return False
    

if __name__ == "__main__":
    str1 = 'aabcc'
    str2 = 'dbbca'
    str3 = 'aadbbcbcac'
    dp = {}

    print(dfs(dp, str1, str2, str3, 0, 0))