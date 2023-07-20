def heapify(arr, size, i):
    parent = int(((i-1)/2))

    if arr[parent] > 0:
        if arr[i] > arr[parent]:
            arr[i], arr[parent] = arr[parent], arr[i]

            heapify(arr, size, parent)

def insertNode(arr, key):
    global size
    size += 1
    
    arr.append(key)

    heapify(arr, size, size - 1)

def printArray(arr, size):
    for i in range(size):
        print(arr[i], end=" ")

if __name__ == '__main__':
    arr = [10, 5, 3, 2, 4, 1, 7]
    size = 7
    key = 15
    insertNode(arr, key)
    printArray(arr, size)