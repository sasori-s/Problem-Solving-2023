def LCS(A, B):
    if A == "" or B == "":
        return 0

    if A[0] == B[0]:
        return LCS(A[1:], B[1:])
    else:
        return max(1 + LCS(A[1:], B), 1 + LCS(A, B[1:]))

if __name__ == '__main__':
    A = 'abcde'
    B = 'ace'

    print(LCS(A, B))