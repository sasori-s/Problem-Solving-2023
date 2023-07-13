def countPalindrome(s, l, r):
    result = 0

    while l >= 0 and r < len(s) and s[l] == s[r]:
        result += 1
        print(s[l:r+1])
        l -= 1
        r += 1
    
    
    return result

def countSubstrings(s):
    result = 0 

    for i in range(len(s)):
        result += countPalindrome(s, i, i)
        result += countPalindrome(s, i, i+1)

    return result

if __name__ == "__main__":
    s = 'aaab'
    print(countSubstrings(s))