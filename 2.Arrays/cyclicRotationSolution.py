from collections import deque

def solution(A, K):
    d=deque(A)
    d.rotate(K)
    return list(d)
	
# OR

def solution2(A, K):
    return A[-K:]+A[:-K]