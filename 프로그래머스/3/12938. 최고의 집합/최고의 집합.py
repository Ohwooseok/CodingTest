def solution(n, s):
   
    if s < n :
        return [-1]
    
    base = s // n
    remainder = s % n
    
    answer = [base] * (n - remainder) + [base+1] * remainder

        
    
    return answer