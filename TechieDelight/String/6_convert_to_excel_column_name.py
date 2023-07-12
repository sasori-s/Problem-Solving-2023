from random import randint

def getColumnName(n):
    result = " "

    while n > 0:
        index = (n - 1) % 26
        result += chr(index + ord('A'))
        n = (n - 1) // 26

    return result[::-1]

if __name__ == "__main__":
    for i in range(1, 11):
        r = randint(1, 1000)
        print(r, '-', getColumnName(r))