def findCombinations(lists, keys, combinations, d, index, result=""):
    if index == -1:
        combinations.add(result)
        return

    digit = keys[index]

    if digit not in d:
        n = len(lists[digit])

        for i in range(n):
            d[digit] = lists[digit][i]

            findCombinations(lists, keys, combinations, d, index - 1, str(lists[digit][i]) + result)

            d.pop(digit)
        return

    else:
        findCombinations(lists, keys, combinations, d, index - 1, f'{d[digit]}{result}')


def findAllCombinations(lists, keys):
    if not lists and not keys:
        return set()

    d = {}

    combinations = set()

    findCombinations(lists, keys, combinations, d, len(keys) - 1)
    return combinations


if __name__ == '__main__':
    lists = [
        ['A', 'B', 'C', 'D'],
        ['E', 'F', 'G', 'H', 'I', 'J', 'K'],
        ['L', 'M', 'N', 'O', 'P', 'Q'],
        ['R', 'S', 'T'],
        ['U', 'V', 'W', 'X', 'Y', 'Z']
    ]

    keys = [0, 2, 0]
    
    print(findAllCombinations(lists, keys))