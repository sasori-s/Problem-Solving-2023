from collections import deque

def reverseText(s):
    if not s:
        return None

    low = high = 0
    stack  = deque()

    for i, e in enumerate(s):
        if e == ' ':
            stack.append(s[low:high+1])
            high = low = i + 1

        else:
            high = i

    sb = ""

    stack.append(s[low:])

    while stack:
        sb += stack.pop() + " "
    
    return sb[:-1]


if __name__ == '__main__':
    s = 'Preparation Interview Technical'
    print(reverseText(s))