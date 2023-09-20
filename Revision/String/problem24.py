def findLogestSubstring(s, k):
    freq = [0] * 128
    begin = end = 0
    low = high = 0

    window = set()

    while high < len(s):
        window.add(s[high])
        freq[ord(s[high])] = freq[ord(s[high])] + 1

        while len(window) > k:
            freq[ord(s[low])] = freq[ord(s[low])] - 1
            

            if freq[ord(s[low])] == 0:
                window.remove(s[low])

            low += 1

        if end - begin < high - low:
            end = high
            begin = low

        high += 1

    return s[begin: end + 1]




if __name__ == '__main__':
    s = 'abcbdbdbbdcdabd'
    k = 2

    print(findLogestSubstring(s, k))