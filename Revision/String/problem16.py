import collections

def getMinumumOperations(first, second):
    i = len(first) - 1
    j = i
    count = 0

    while i >= 0:
        while i >= 0 and first[i] != second[j]:
            count += 1
            i -= 1

        j -= 1
        i -= 1

    return count


def isTransformable(first, second):
    if len(first) != len(second):
        return False

    return collections.Counter(first) == collections.Counter(second)


if __name__ == '__main__':
    first = 'ADCB'
    second = 'ABCD'

    if isTransformable(list(first), list(second)):
        print(f"The {first} string to {second} can be comverted with {getMinumumOperations(first, second)} opearations ")