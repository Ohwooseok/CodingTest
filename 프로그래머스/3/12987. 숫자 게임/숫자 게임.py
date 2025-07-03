def solution(A, B):
    A.sort()
    B.sort()
    answer = 0
    
    idx_a = 0
    idx_b = 0
    
    while idx_a < len(A) and idx_b < len(B):
        if A[idx_a] < B[idx_b]:
            answer +=1
            idx_a += 1
            idx_b += 1
        else:
            idx_b += 1
            
    
    
    
    return answer