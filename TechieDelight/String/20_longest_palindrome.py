def longestPalindrome(s):
    total = [0] * (len(s) + 1)

    for i in range(1, len(s) + 1):
        total[i] = total[i-1] + int(s[i-1])

    max = 0

    for i in range(len(s) - 1):
        for j in range(1 + len(s) - 2):
            length = j - i + 1

            mid = i + length // 2

            if total[mid] - total[i] == total[j+1] - total[mid] and max < length:
                max = length

    return max

if __name__ == "__main__":
    s = '13267224'
    print('The length of the longest palindromic sum substring is',
            longestPalindrome(s))