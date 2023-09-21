def isOpening(char):
    if char == '(' or char == '{' or char == '[':
        return True

def isMatching(char1, char2):
    if char1 == '(' and char2 == ')': return True
    if char1 == '{' and char2 == '}': return True
    if char1 == '[' and char2 == ']': return True


def checkParenthesis(parenthesis):
    stack = []

    for i in parenthesis:
        if isOpening(i):
            stack.append(i)

        else:
            element = stack[-1]

            if len(stack) == 0:
                return False

            elif not isMatching(element, i):
                return False

            else:
                stack.pop()

    return len(stack) == 0 



if __name__ == '__main__':
    parenthesis = '()([])'

    if checkParenthesis(parenthesis):
        print("Valid parenthesis")
    else:
        print("Not valid parenthesis")