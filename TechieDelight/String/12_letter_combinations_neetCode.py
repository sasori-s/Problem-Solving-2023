def letterCombinations(digits):
    res = []
    digitToChar = {
        '2' : 'abc',
        '3' : 'def',
        '4' : 'ghi',
        '5' : 'jkl',
        '6' : 'mno',
        '6' : 'mno',
        '7' : 'qprs',
        '8' : 'tuv',
        '9' : 'wxyz',
    }

    def bracktrack(i, currStr):
        if len(currStr) == len(digits):
            res.append(currStr)
            return
        
        for c in digitToChar[digits[i]]:
            bracktrack(i + 1, currStr + c)

    if digits:
        bracktrack(0, "")

    return res

if __name__ == "__main__":
    digits = '234'
    print(letterCombinations(digits))