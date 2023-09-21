def generatepw(current, target, fmap, oddc, answer_so_far):
    if current > target:
        rev = ''
        for ch in answer_so_far:
            rev = ch + rev

        res = answer_so_far

        if oddc:
            res += oddc
        res += rev

        print(res)
        return

    for char in fmap.keys():
        # print(fmap)
        freq = fmap[char]

        if fmap[char] > 0:
            fmap[char] = freq - 1
            generatepw(current + 1, target, fmap, oddc, answer_so_far + char)
            fmap[char] = freq
    

def hashify(s):
    fmap = {}
    for i, e in enumerate(s):
        if e in fmap:
            fmap[e] += 1
        else:
            fmap[e] = 1

    # print(fmap)

    odd = ''
    odds = 0
    length = 0

    for char in fmap.keys():
        freq = fmap.get(char)

        if freq % 2:
            odds += 1
            odd = char

        fmap[char] = freq // 2
        length += freq // 2

    if odds > 1:
        print("Operation is not possible")
        return

    print(fmap)
    # print(length)
    # print(odd)

    generatepw(1, length, fmap, odd, "")    


if __name__ == '__main__':
    s = 'malayalam'
    hashify(s)