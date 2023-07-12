from collections import deque

def printAllCombinations(pattern):
    if not pattern:
        return

    stack = deque()
    stack.append(pattern)

    while stack:
        curr = stack.pop()
        index = curr.find('?')

        if index != -1:
            for ch in '01':
                curr = curr[:index] + ch + curr[index + 1:]
                stack.append(curr)

        else:
            print(curr)

if __name__ == "__main__":
    pattern = '1?11?00?1?'
    printAllCombinations(pattern)

    