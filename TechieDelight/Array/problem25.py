def kadane(A):
    max_so_far = max_ending_here = 0

    for i in range(len(A)):
        max_ending_here = A[i] + max_ending_here
        max_ending_here = max(max_ending_here, 0)
        max_so_far = max(max_ending_here, max_so_far)

    # print(max_so_far)
    return max_so_far

def runCircularKadane(A):
    if len(A) == 0:
        return 0
    
    maximum = max(A)

    if maximum < 0:
        return maximum
    
    for i in range(len(A)):
        A[i] = -A[i]

    neg_max_sum = kadane(A)
    print(f"Negative array sum {neg_max_sum}")

    for i in range(len(A)):
        A[i] = -A[i]

    print(f"Total array sum {sum(A)}")

    return max(kadane(A), sum(A) + neg_max_sum)




if __name__ == "__main__":
    A = [2, 1, -5, 4, -3, 1, -3, 4, -1]
    print("The sum of the sublist with largest sum is ", runCircularKadane(A))