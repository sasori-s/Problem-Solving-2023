def findLogestSubstring(s):
    res = ''
    resLen = 0

    for i in range(len(s)):
        left, right = i, i

        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > resLen:
                resLen = right - left + 1
                res = s[left : right + 1]

            left -= 1
            right += 1

        left, right = i, i + 1

        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > resLen:
                resLen = right - left + 1
                res = s[left : right + 1]

            left -= 1
            right += 1

    return res




if __name__ == '__main__':
    s = 'ABDCBCDBDCBBC'

    print(f"The longest palindromic substring of {s} is {findLogestSubstring(s)}")