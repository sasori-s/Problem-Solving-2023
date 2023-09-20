def expand(s, max, left, right):
    leftSum = rightSum = 0  
    
    while left >= 0 and right < len(s):
        leftSum += int(s[left])
        rightSum += int(s[right])

        if leftSum == rightSum and right - left + 1 > max:
            max = right - left + 1

        (left, right) = (left -1, right + 1)

    return max

def findLongestSum(s):
    if not s:
        return None

    max = 0 

    for i in range(len(s) - 1):
        max = expand(s, max, i, i + 1)

    return max


if __name__ == '__main__':
    s = '546374'
    print(f"The longest length of the palindromic sum substring is: {findLongestSum(s)}")