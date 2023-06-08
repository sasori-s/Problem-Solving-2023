# Sort binary array in linear time
# Google Translate Icon
# Given a binary array, sort it in linear time and constant space. The output should print all zeroes, followed by all ones.

# For example,

# Input:  { 1, 0, 1, 0, 1, 0, 0, 1 }
 
# Output: { 0, 0, 0, 0, 1, 1, 1, 1 }


def sort(A):
    zeros = A.count(0)
    k = 0
    while zeros:
        A[k] = 0
        zeros -= 1
        k += 1
    
    for i in range(k, len(A)):
        A[i] = 1
        


if __name__ == "__main__":
    A = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
    sort(A)
    print(A)