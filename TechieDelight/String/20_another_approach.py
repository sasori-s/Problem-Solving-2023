def expand(s, low, high, max):
    leftSum = rightSum = 0

    while low >= 0 and high < len(s): 
        leftSum += int(s[low])
        rightSum += int(s[high])

        if leftSum == rightSum and (high - low - 1) > max:
            max = high - low + 1

        (low, high) = (low - 1, high + 1)

    return max

def longestPalindrome(s):
    if not s:
        return 0
    
    max = 0

    for i in range(len(s)):
        max = expand(s, i, i+1, max)

    return max


if __name__ == "__main__":
    s = '546374'
    print('The length of the longest palindromic sum substring is',
            longestPalindrome(s))
    