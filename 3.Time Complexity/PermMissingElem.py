# 100/100
def solution(A):
    length = len(A)
    if length == 0:
    	return 1
    A.sort()
    for i in range(0, length -1):
    	if A[i] != i + 1:
    		return i + 1
    return length + 1
	
