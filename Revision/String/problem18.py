from collections import deque

def findMaxLen(parenthesis):
    stack = deque()

    if not parenthesis:
        return False

    stack.append(-1)

    length = 0

    for i, e in enumerate(parenthesis):
        if e == '(':
            stack.append(i)

        else:
            stack.pop()

            if not stack:
                stack.append(i)
                continue

        current_length = i - stack[-1]

        if current_length > length:
            length = current_length

    return length


if  __name__ == "__main__":
    print(findMaxLen('((()()'))         # prints 4
    print(findMaxLen('(((()'))          # prints 2
    print(findMaxLen('(((('))           # prints 0
    print(findMaxLen('()()'))           # prints 4
    print(findMaxLen('(()())(()'))      # prints 6
 