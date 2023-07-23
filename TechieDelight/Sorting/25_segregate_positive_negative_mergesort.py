def merge(A, aux, low, mid, high):
    k = low

    for i in range(low, mid + 1):
        if A[i] < 0:
            aux[k] = A[i]
    
            k += 1
    for j in range(mid + 1, high + 1):
        if A[j] < 0:
            aux[k] = A[j]
            k += 1

    for i in range(low, mid + 1):
        if A[i] >= 0:
            aux[k] = A[i]
    
            k += 1
    
    for j in range(mid + 1, high + 1):
        if A[j] >= 0:
            aux[k] = A[j]
            k += 1

    for i in range(low, high + 1):
        A[i] = aux[i]

    

def partition(A, aux, low, high):
    if low >= high:
        return

    mid = low +((high - low) >> 1)

    partition(A, aux, low, mid)
    partition(A, aux, mid + 1, high)

    merge(A, aux, low, mid, high)

if __name__ == '__main__':
    A = [9, -3, 5, -2, -8, -6, 1, 3]
    aux = A.copy()

    partition(A, aux, 0, len(A) - 1)
    print(A)