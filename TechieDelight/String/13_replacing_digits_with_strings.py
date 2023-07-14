def findCombinations(lists, keys, combinations, index, d, result=""):
    if index == -1:
        combinations.add(result)
        return 
    
    digits = keys[index]

    if digits not in d:
        n = len(lists[digits])

        for i in range(n):
            d[digits] = lists[digits][i]

            findCombinations(lists, keys, combinations, index - 1, d, str(lists[digits][i]) + result)

            d.pop(digits)

        return

    findCombinations(lists, keys, combinations, index-1, d, f'{d[digits]}{result}')


def findAllCombinations(lists, keys):
    if not lists or not keys:
        return set()

    combinations = set()

    d = {}

    findCombinations(lists, keys, combinations, len(keys) - 1, d)
    return combinations

if __name__ == "__main__":
    lists = [
        ['A', 'B', 'C', 'D'],
        ['E', 'F', 'G', 'H', 'I', 'J', 'K'],
        ['L', 'M', 'N', 'O', 'P', 'Q'],
        ['R', 'S', 'T'],
        ['U', 'V', 'W', 'X', 'Y', 'Z']
    ]

    keys = [0, 2, 0]
    print(findAllCombinations(lists, keys))