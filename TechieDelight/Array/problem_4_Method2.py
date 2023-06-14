def sort(A):
    size = len(A)
    count = 0

    for i in range(len(A)):
        if A[i] == 1:
            A[i] = 0
            count += 1
            last_zero = i
    print(last_zero)
    # print(A)
        
    for i in range(len(A) - count, len(A)):
        A[i] = 1


if __name__ == "__main__":
    A = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
    sort(A)
    print(A)