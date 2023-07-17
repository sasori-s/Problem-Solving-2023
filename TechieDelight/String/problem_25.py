def generatepw(current_spot, total_spot, fmap, oddChar, answer_so_far):
    if current_spot > total_spot:
        rev = ""
        for i in answer_so_far:
            rev = i + rev
        
        res = answer_so_far
        if oddChar:
            res += oddChar
        
        res += rev

        print(res)
        return

    for key, value in fmap.items():
        if value > 0:
            fmap[key] = value - 1
            generatepw(current_spot + 1, total_spot, fmap, oddChar, answer_so_far+key)
            fmap[key] = value

if __name__ == "__main__":
    s = "aabbaabb"

    fmap = {}

    for i in range(len(s)):
        if s[i] in fmap:
            fmap[s[i]] += 1

        else:
            fmap[s[i]] = 1

    odd = None
    odds = 0
    length = 0

    for key, value in fmap.items():
        if fmap[key] % 2 == 1:
            odd = key
            odds += 1

        fmap[key] = value/2
        length += value/2

    if odds > 1:
        print("It does not exist")

    else:    
        generatepw(1, length, fmap, odd, '')

        