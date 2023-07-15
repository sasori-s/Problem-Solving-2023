from collections import deque

def findMaxLen(s):
    if not s:
        return 0

    stack = deque()

    stack.append(-1)

    length = 0

    for i, e in enumerate(s):
        if e == '(':
            stack.append(i)

        else:
            stack.pop()

            if not stack:
                stack.append(i)
                continue

        curr_len = i - stack[-1]

        if length < curr_len:
            length = curr_len

    return length


if __name__ == "__main__":
    print(findMaxLen('((()()'))         # prints 4
    print(findMaxLen('(((()'))          # prints 2
    print(findMaxLen('(((('))           # prints 0
    print(findMaxLen('()()'))           # prints 4
    print(findMaxLen('(()())(()'))      # prints 6

        