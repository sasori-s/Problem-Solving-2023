import collections

def getMinimumOperations(first, second):
    i = j = len(first) - 1

    count = 0

    while i >= 0:
        while i >= 0 and first[i] != second[j]:
            i = i - 1
            count += 1

        i = i - 1
        j = j -1
    return count


def isTransformable(first, second):
    if len(first) != len(second):
        return False

    return collections.Counter(first) == collections.Counter(second)

if __name__ == "__main__":
    first = 'ADCB'
    second = 'ABCD'

    if isTransformable(first, second):
        print(f"The minimum number of steps required to convert string {first} to string {second} is {getMinimumOperations(first, second)}")