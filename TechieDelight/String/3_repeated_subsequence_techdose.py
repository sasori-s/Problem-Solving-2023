def dp(m, n, A, B):
    array_2d = [[0 for i in range(n + 1)]for j in range(m + 1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            array_2d[i][j] = -1

    return lcs(array_2d, m, n, A, B)

def lcs(array_2d, m, n, A, B):
    if m == 0 or n == 0:
        return 0
    
    if array_2d[m][n] != -1:
        return array_2d[m][n]

    if str1[m-1] == str2[n-1] and m != n:
        array_2d[m][n] = 1 + lcs(array_2d, m-1, n-1, A, B)
        return array_2d[m][n] 
    
    else:
        array_2d[m][n] = max(lcs(array_2d, m, n-1, A, B), lcs(array_2d, m-1, n, A, B))
        return array_2d[m][n]

if __name__ == "__main__":
    str1 = "ABCAB"
    str2 = "ABCAB"

    lcs_length = dp(len(str1), len(str2), str1, str2)

    if lcs_length > 1:
        print("There exists a repeated subsequence")
    else:
        print("There does not exist a repeated subsequence")