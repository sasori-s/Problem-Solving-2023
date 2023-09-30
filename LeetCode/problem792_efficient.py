from collections import defaultdict

def numMatchingSubseq(S, words):
    waiting = defaultdict(list)
    for w in words:
        waiting[w[0]].append(iter(w[1:]))

    print(waiting)

    for c in S:
        # print(len(waiting))
        for it in waiting.pop(c, ()):
            print(len(waiting))
            waiting[next(it, None)].append(it)
    
    # print(len(waiting))
    return len(waiting[None])

if __name__ == '__main__':
    s = "qlhxagxdqh"
    words = ["qlhxagxdq","qlhxagxdq","lhyiftwtut","yfzwraahab"]
    test = 'yfzwraahab'
    # print(isSubsequence(test, s))
    print(numMatchingSubseq(s, words))