def kodane(A):
    max_so_far = 0
    max_ending_here = 0

    for index, i in enumerate(A):
        max_ending_here = i + max_ending_here
        max_ending_here = max(max_ending_here, 0)
        if max_ending_here == 0:
            start_index = index + 1

        max_so_far = max(max_so_far, max_ending_here)
        if max_so_far == max_ending_here:
            ending_index = index

    print(start_index, ending_index)

    return max_so_far

if __name__ == "__main__":
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("The maximum sum of the subarray is ", kodane(A))

