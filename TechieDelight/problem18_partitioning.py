def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(A):
    j = 0
    for i in range(len(A)):
        if A[i]:
            swap(A, i, j)
            j += 1




if __name__ =="__main__":
    A = [6, 0, 8, 2, 3, 0, 4, 0, 1]
    partition(A)
    print(A)