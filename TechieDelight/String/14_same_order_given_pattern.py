def patternMatch(words, pattern):
    if not words or not pattern:
        return 
    
    for word in words:
        dict1 = {}
        dict2 = {}

        if len(pattern) == len(word):
            i = 0

            while i < len(pattern):
                w = word[i]
                p = pattern[i]

                if w not in dict1:
                    dict1[w] = p
                else:
                    if dict1[w] != p:
                        break


                if p not in dict2:
                    dict2[p] = w
                else:
                    if dict2[p] != w:   
                        break

                i = i + 1

            if i == len(pattern):
                print(word, end=' ')
                

if __name__ == "__main__":
    words = ['leet', 'abcd', 'loot', 'geek', 'cool', 'for', 'peer', 'dear', 'seed','meet', 'noon', 'otto', 'mess', 'loss']

    pattern = 'moon'

    patternMatch(words, pattern)