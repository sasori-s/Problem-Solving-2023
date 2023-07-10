def expand(s, low, high):
    length = len(s)

    while low >= 0 and high < length and s[low] == s[high]:
        high += 1
        low -= 1

    return s[low + 1: high]

def find_longest_palindrome_substring(s):
    if not s:
        return ' '

    max_str = " "
    max_length = 0

    for i in range(len(s)):
        curr_str = expand(s, i, i)
        curr_length = len(curr_str)

        if curr_length > max_length:
            max_length = curr_length
            max_str = curr_str

        curr_str = expand(s, i, i+1)
        curr_length = len(curr_str)

        if curr_length > max_length:
            max_length = curr_length
            max_str = curr_str

    return max_str


if __name__ == "__main__":
    s = 'ABDCBCDBDCBBC'
    print(f"The longest palindromic substring of {s} is", find_longest_palindrome_substring(s))