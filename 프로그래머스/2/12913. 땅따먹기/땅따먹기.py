def solution(land):
    answer = 0

    prev = land[0][:]
    
    for r in range(1, len(land)):
        cur = [0] * 4
        for c in range(4):
            cur[c] = land[r][c] + max(prev[k] for k in range(4) if k != c)
        
        prev = cur
            

    return max(prev)