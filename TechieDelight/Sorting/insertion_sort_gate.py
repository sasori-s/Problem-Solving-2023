def insertionSort(arr):
    for j in range(2, len(arr)):
        key = arr[j]

        i = j - 1

        while i > 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        
        arr[i+1] = key
    
    return arr

if __name__ == "__main__":
    arr = [40, 20, 60, 10, 50, 30]
    print(insertionSort(arr))