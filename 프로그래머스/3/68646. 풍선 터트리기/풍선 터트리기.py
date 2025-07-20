def solution(a):
    n = len(a)
    
    left_min = [0] * n
    min_val = a[0]
    for i in range(n):
        if a[i] < min_val:
            min_val = a[i]
        
        left_min[i] = min_val
    
    right_min = [0] * n
    min_val = a[-1]
    for i in range(n-1,-1,-1):
        if a[i] < min_val:
            min_val = a[i]
        right_min[i] = min_val
        
    answer = 0
    
    for i in range(n):
        # 풍선 i가 왼쪽 또는 오른쪽 구간의 최소값이면 살아남을 수 있음
        if a[i] <= left_min[i] or a[i] <= right_min[i]:
            answer += 1
    

    
    return answer