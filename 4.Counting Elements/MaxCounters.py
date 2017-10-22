def solution(N, A):
    
    counters = [0] * N
    maxNum = 0
    last_increase = 0
    
    for i in A:
        if i > N:
            last_increase = maxNum
        else:
            counters[i - 1] = max(counters[i - 1], last_increase)
            counters[i - 1] += 1
            maxNum = max(maxNum, counters[i - 1])
    for i in range(0, N):
        counters[i] = max(counters[i], last_increase)

    return counters