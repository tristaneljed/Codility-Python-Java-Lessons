def solution(A):
    sum = 0
    
    for num in A:
        sum = sum + num
    
    sum_left = 0
    sum_right = sum
    abs_diff = []
    
    for i in range(1, len(A)):
        sum_left = sum_left + A[i - 1]
        sum_right = sum_right - A[i - 1]
        diff = sum_left - sum_right
        if diff < 0:
            abs_diff.append(diff * -1)
        else:
            abs_diff.append(diff)
            
    return min(abs_diff)