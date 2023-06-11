from random import randrange

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def shuffle(A):
    for i in reversed(range(1, len(A))):
        j = randrange(i + 1)
        swap(A, i, j)

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6]
    shuffle(A)
    print(A)