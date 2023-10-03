from collections import defaultdict

def findAnagrams(words):
    res = defaultdict(list)

    for word in words:
        count = [0] * 26

        for char in word:
            count[ord(char) - ord("A")] += 1

        res[tuple(count)].append(word)

    return res.values()


if __name__ == '__main__':
    words = ['CARS', 'REPAID', 'DUES', 'NOSE', 'SIGNED', 'LANE', 'PAIRED', 'ARCS',
             'GRAB', 'USED', 'ONES', 'BRAG', 'SUED', 'LEAN', 'SCAR', 'DESIGN']

    anagrams = findAnagrams(words)
    print(anagrams)