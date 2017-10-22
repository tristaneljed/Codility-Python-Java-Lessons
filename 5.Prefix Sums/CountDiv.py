def solution(A, B, K):
    if B < A or K <= 0:
        raise Exception("Invalid Input")
 
    min_value =  ((A + K -1) // K) * K
 
    if min_value > B:
      return 0
 
    return ((B - min_value) // K) + 1

# OR

def solution(A, B, K):
    diffs = B//K - A//K    
    if A % K == 0:   
        diffs += 1
    return diffs