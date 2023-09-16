def numMatchingSubseq( s, words):
    number = 0
    freq = {}

    for word in words:
        freq[word] = freq.setdefault(word, 0) + 1

    print(freq)

    for key in freq.keys():
        if not isSubsequence(key, s):
            freq[key] = 0 

    print(freq)

    for value in freq.values():
        number += value

    return number

def isSubsequence(s, t):
    m = len(t)
    n = len(s)

    if m < n:
        return False
    
    i = 0
    j = 0
    count = 0

    while i < m and j < n:
        if s[j] == t[i]:
            i += 1
            j += 1
            count += 1
            
        else:
            i += 1

    # print(count)
    if count >= n:
        return True
    
    return False



if __name__ == '__main__':
    s = "qlhxagxdqh"
    words = ["qlhxagxdq","qlhxagxdq","lhyiftwtut","yfzwraahab"]
    test = 'yfzwraahab'
    # print(isSubsequence(test, s))
    print(numMatchingSubseq(s, words))