def expand(s, low, high, k):
    while low >= 0 and high <= len(s) and s[low] == s[high]:
        if high - low + 1 == k:
            return True

        low -= 1
        high += 1

    return False

def longestPalindromeSubstrings(s, k):
    for i in range(len(s) - 1):
        if expand(s, i, i, k) or expand(s, i, i+1, k):
            return True
        
    return False


def isRotatedPalindrome(s):
    n = len(s)
    return longestPalindromeSubstrings(s+s, n)

if __name__ == "__main__":
    s = "ABCCBA"
    s = s[:2] + s[2:]

    if isRotatedPalindrome(s):
        print("The string is rotated palindrome")
    else:
        print("The string is not rotated palindrome")