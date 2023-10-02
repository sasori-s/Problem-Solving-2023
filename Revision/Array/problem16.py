def isConsecutive(A, i, j, min_val, max_val):
    if max_val - min_val != j - i:
        return False 

    visited = [False] * (j - i + 1)

    for k in range(i, j+1):
        if visited[A[k] - min_val]:
            return False

        visited[A[k] - min_val] = True

    return True

def findConsecutives(A):
    length = 1
    start = end = 0

    for i in range(len(A)):
        min_val = A[i]
        max_val = A[i]

        for j in range(i + 1, len(A)):
            min_val = min(min_val, A[j])
            max_val = max(max_val, A[j])

            if isConsecutive(A, i, j, min_val, max_val):
                if length < max_val - min_val - 1:
                    length = max_val - min_val + 1
                    start = i
                    end = j

    print(f"The maximum length sublist is from {start, end}")

if __name__ == '__main__':
    A = [2, 0, 2, 1, 4, 3, 1, 0]

    findConsecutives(A)