from collections import deque

def isParenthesis(brackets):
    stack = deque()

    for bracket in brackets:
        if isOpening(bracket):
            stack.append(bracket)

        else:
            if len(stack) == 0:
                return False
            
            elif not isMatching(bracket, stack[-1]):
                return False

            else:
                stack.pop()

    return len(stack) == 0

def isOpening(bracket):
    if bracket == '('  or bracket == '{'  or bracket == '[':
        return True
    
def isMatching(bracket, stack_element):
    if (stack_element == '(' and bracket == ')') or\
    (stack_element == '{' and bracket == '}') or\
    (stack_element == '[' and bracket == ']'):
        return True
    

if __name__ == "__main__":
    brackets = '()([])'
    print(isParenthesis(brackets))