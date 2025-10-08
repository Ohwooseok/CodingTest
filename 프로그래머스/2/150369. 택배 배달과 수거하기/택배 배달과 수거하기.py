def solution(cap, n, deliveries, pickups):
    answer = 0
    d_remain = 0
    p_remain = 0
    
    for i in range(n-1, -1, -1):
        
        d_remain += deliveries[i]
        p_remain += pickups[i]
        
        if d_remain > 0 or p_remain > 0:
            trips = max(
                (d_remain + cap - 1) // cap,
                (p_remain + cap - 1) // cap
            )
            answer += (i+1) * 2 * trips
            d_remain -= cap * trips
            p_remain -= cap * trips
    
    
    
    
    return answer