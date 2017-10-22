def solution(N):
    A = (bin(N))[2:]
    length = len(A)
    i = 0
    List = []
    count = 0
    temp = 0
    while(i < length):
        if(A[i] == '1' and temp == 0):
            temp = 1
        if(temp == 1):
            if(A[i] == '0'):
                count += 1
            else:
                List.append(count)
                count = 0
        i += 1
    return max(List)