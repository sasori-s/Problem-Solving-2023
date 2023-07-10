def lcs(m, n, A, B):
    if m == 0 or n == 0:
        return 0
    
    if str1[m-1] == str2[n-1]:
        return 1 + lcs(m-1, n-1, A, B)
    
    else:
        return max(lcs(m-1, n, A, B), lcs(m, n-1, A, B))

if __name__ == "__main__":
    str1 = "ABCAB"
    str2 = "AECB"

    print(lcs(len(str1), len(str2), str1, str2))