def isCircularMove(s):
    x = y = 0

    dir = "N"

    for c in s:
        if c == 'M':
            if dir == "N": y = y + 1
            elif dir == "E": x = x + 1
            elif dir == "S": y = y - 1
            elif dir == "W": x = x - 1

        elif c == "L":
            if dir == "N" : dir = "W"
            elif dir == "E" : dir = "N"
            elif dir == "S" : dir = "E"
            elif dir == "W" : dir = "S"

        elif c == "R":
            if dir == "N" : dir = "E"
            elif dir == "E" : dir = "S"
            elif dir == "S" : dir = "W"
            elif dir == "W" : dir = "N"

    return x == 0 and y == 0

if __name__ == "__main__":
    s = 'MMRMMRMMRMM'
    
    if isCircularMove(s):
        print("Circular move")
    else:
        print("Not circular move")