def findZeroIndex(A):
    max_index = -1
    max_count = 0

    prev_zero_index = -1
    count = 0

    for i in range(len(A)):
        if A[i] == 1:
            count += 1

        else:
            count = i - prev_zero_index
            prev_zero_index = i

        if count > max_count:
            max_count = count
            max_index = prev_zero_index

    return max_index
        

if __name__ == '__main__':
    A = [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]

    index = findZeroIndex(A)

    if index != -1:
        print("Index to be replaced is: ", index)
    else:
        print("invalid input")