def findAnagrams(word):
    if not words:
        return anagrams

    anagrams = []

    nums = ["".join(sorted(word)) for word in words]

    d = {}

    for i, e in enumerate(nums):
        d.setdefault(e,[]).append(i)

    for index in d.values():
        collection = tuple(words[i] for i in index)
        if len(collection) > 1:
            anagrams.append(collection)

    return anagrams

if __name__ == "__main__":
    words = ['CARS', 'REPAID', 'DUES', 'NOSE', 'SIGNED', 'LANE', 'PAIRED', 'ARCS',
             'GRAB', 'USED', 'ONES', 'BRAG', 'SUED', 'LEAN', 'SCAR', 'DESIGN']

    anagrams = findAnagrams(words)
    for anagram in anagrams:
        print(anagram)