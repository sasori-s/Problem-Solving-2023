def isFound(s, word, worddict, start):
    if start == len(s):
        return True
    
    for word in worddict:
        if s[start : start + len(word)] == word:
           print(s[start : start + len(word)])
           return isFound(s, word, worddict, start + len(word))
        
    return False


if __name__ == '__main__':
    worddict = ["cats","dog","sand","and","cat"]
    s = 'catsandog'

    print(isFound(s, "",  worddict, 0))

