def longestSubstring(s, k):
    i = j = 0
    map = {}
    max_len = 0

    while j < len(s):
        if s[j] not in map:
            map[s[j]] = 1
        
        else:
            map[s[j]] += 1

        if len(map) < k:
            j += 1

        elif len(map) == k:
            max_len = max(max_len, j - i + 1)
            j += 1

        elif len(map) > k:
            while len(map) > k:
                map[s[i]] -= 1

                if map[s[i]] == 0:
                    del map[s[i]]

                i = i + 1
            j = j + 1

    return max_len

if __name__ == "__main__":
    s = 'aabacbebebe'
    k = 3

    print(longestSubstring(s, k))

            