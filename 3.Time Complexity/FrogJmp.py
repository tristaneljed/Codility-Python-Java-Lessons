def solution(X, Y, D):
    
    distance = Y - X
    if distance == 0:
        return 0
    jumps = distance / D
    rest = distance % D
    if rest == 0:
        return jumps
    else:
        return jumps + 1