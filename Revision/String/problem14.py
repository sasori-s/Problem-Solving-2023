def patternMatch(words, pattern):
    if not words or not pattern:
        return 

    for word in words:
        d1 = {}
        d2 = {}

        flag = True
        for i in range(len(word)):
            w = word[i]
            p = pattern[i]

            if w not in d1:
                d1[w] = p
            else:
                if d1[w] != p:
                    flag = False
                    break

            if p not in d2:
                d2[p] = w
            else:
                if d2[p] != w:
                    flag = False
                    break
                              
        if flag:
            print(word, end=" ")
        
        # if i == len(pattern) - 1:
        #     print(word, end=" ")
                


if __name__ == '__main__':
    words = ['leet', 'abcd', 'loot', 'geek', 'cool', 'for', 'peer', 'dear', 'seed',
            'meet', 'noon', 'otto', 'mess', 'loss']

    pattern = 'moon'

    patternMatch(words, pattern)