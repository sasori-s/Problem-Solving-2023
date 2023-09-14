def findSubSequence(arr, n, total, result, i):
    if i == len(arr):
        if total == sum(result):
            print(result)
            return True
        
        return False
    
    result.append(arr[i])
    if findSubSequence(arr, n, total, result, i + 1):
        return True

    result.pop()
    if findSubSequence(arr, n, total, result, i + 1):
        return True
    
    return False



if __name__ == '__main__':
    arr = [1, 2, 1]
    n = 3
    total = 2
    result = []

    findSubSequence(arr, n, total, result, 0)