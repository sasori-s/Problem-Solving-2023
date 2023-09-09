def find(x, y, interleavigns, curr=""):
    if not x and not y:
        interleavigns.add(curr)
        return

    if x:
        find(x[1:], y, interleavigns, curr + x[0])
    
    if y:
        find(x, y[1:], interleavigns, curr + y[0])

    return interleavigns



def findInterleavings(x, y):
    interleavings = set()
    
    if not x and not y:
        return interleavings

    find(x, y, interleavings)
    return interleavings

if __name__ == '__main__':
    x = 'ABC'
    y = 'ACB'

    interleavings = findInterleavings(x, y)
    print(interleavings)