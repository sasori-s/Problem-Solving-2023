def findLISLength(input):
    if len(input) == 0:
        return 0 
    
    LIS = [1] * len(input)

    for i in range(1, len(input)):
        for j in range(i):
            if input[i] > input[j] and LIS[i] < LIS[j] + 1:
                LIS[i] = LIS[j] + 1

    return max(LIS)

if __name__ == '__main__':
    input = [2, 6, 3, 4, 1, 2 ,9, 5, 8]
    print("The length of the LTS is ", findLISLength(input))