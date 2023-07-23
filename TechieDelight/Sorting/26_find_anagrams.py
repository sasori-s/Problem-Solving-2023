def groupAnagrams(words):
    anagrams = []

    if not words:
        return anagrams

    nums = [''.join(sorted(word)) for word in words]

    d = {}

    for i, e in enumerate(nums):
        d.setdefault(e, []).append(i)

    for index in d.values():
        collections = tuple(words[i] for i in index)
        if len(collections) > 1:
            anagrams.append(collections)
        
    return anagrams



if __name__ == "__main__":
    words = ['CARS', 'REPAID', 'DUES', 'NOSE', 'SIGNED', 'LANE', 'PAIRED', 'ARCS',
             'GRAB', 'USED', 'ONES', 'BRAG', 'SUED', 'LEAN', 'SCAR', 'DESIGN']

    anagrams = groupAnagrams(words)
    
    for anagram in anagrams:
        print(anagram)