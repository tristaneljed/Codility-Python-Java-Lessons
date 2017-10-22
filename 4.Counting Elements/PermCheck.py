def solution(A):
    A.sort()
    l = len(A)
    if A[0] != 1:
        return 0
    else:
        for i, e in enumerate(A):
            if l != i + 1 and A[i] != A[i+1] - 1:
                return 0
    return 1