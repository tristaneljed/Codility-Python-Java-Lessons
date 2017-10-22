def solution(X, A):
    covered = 0
    covered_a = [-1]*X
    for index,element in enumerate(A):
        if covered_a[element-1] == -1:
            covered_a[element-1] = element
            covered += 1
            if covered == X:
                return index
    return -1