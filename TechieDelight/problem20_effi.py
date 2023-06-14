def findBitonicSublist(A):
    n = len(A)
    
    if n == 0:
        return
    
    max_len = 1
    end_index = 0
    i = 0

    while i + 1 < n:
        length = 1

        while i + 1 < n and A[i] < A[i + 1]:
            i = i + 1
            length += 1

        while i + 1 < n and A[i] > A[i + 1]:
            i = i + 1
            length += 1

        while i + 1 < n and A[i] == A[i + 1]:
            i = i + 1
            
        
        if length > max_len:
            max_len = length
            end_index = i

    
    print(f"The longest bitonic subarry is {max_len}")
    print("The longest subarry is ", A[end_index - max_len + 1 : end_index + 1])
        
        
if __name__ == "__main__":
    A = [3, 5, 8, 4, 5, 9, 10, 8, 5, 3, 4]
    findBitonicSublist(A)