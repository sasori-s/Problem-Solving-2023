def isPalindrome(str):
    (low, high) = (0, len(str) - 1)

    while low < high:
        if str[low] != str[high]:
            return False

        high -= 1
        low += 1

    return True

def hasrepeatedSubsequence(str):
    if not str:
        return False

    frequency = {}
    
    for char in str:
        frequency[char] = frequency.get(char, 0) + 1
        if frequency.get(char) >= 3:
            return True


    repeated = [char for char in str if frequency.get(char) >= 2 ]

    return not isPalindrome(repeated)



if __name__ == "__main__":
    str = 'XYBYAXB'

    if hasrepeatedSubsequence(str):
        print("Repeated subseqeuence is present")
    else:
        print("Repeated subseqeuence is not present")