from collections import deque

def reverseText(s):
    if not s:
        return s

    stack = deque()

    low = high = 0

    for i, e in enumerate(s):
        if e == " ":
            stack.append(s[low: high + 1])
            low = high = i + 1

        else:
            high = i

    stack.append(s[low : ])

    sb = ""
    while stack:
        sb += stack.pop() + ' '

    return sb[:-1]

if __name__ == "__main__":
    s = 'Preparation Interview Technical'
    print(reverseText(s))
