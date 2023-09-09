def expands(s, left, right, k):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        if right - left + 1 == k:
            return True

        left -= 1
        right += 1

    return False


def longestPalindrome(s, k):
    for i in range(len(s) - 1):
        if expands(s, i, i, k) or expands(s, i, i+1, k):
            return True

    return False


def isRotatedPalindrome(s):
    n = len(s)
    return longestPalindrome(s+s, n)


if __name__ == '__main__':
    s = 'ABCCBA'
    s = s[2:] + s[:2]

    if isRotatedPalindrome(s):
        print('The string is rotated palindrome')
    else:
        print("The string is not rotated palindrome")