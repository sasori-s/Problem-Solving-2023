def heapify(arr, n, i):
    largest = i
    leftChild = i * 2 + 1
    rightchild = i * 2 + 2

    if leftChild < n and arr[leftChild] > arr[largest]:
        largest = leftChild

    if rightchild < n and arr[rightchild] > arr[largest]: 
        largest = rightchild

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def deleteRoot(arr):
    global n
    
    lastElement = arr[n-1]
    arr[0] = lastElement

    n = n - 1 
    heapify(arr, n, 0)

def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()

if __name__ == "__main__":
    arr = [10, 5, 3, 2, 4]
    n = len(arr)

    deleteRoot(arr)
    printArray(arr, n)