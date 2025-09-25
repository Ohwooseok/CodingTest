def solution(sequence, k):
    
    l = len(sequence)
    left = 0
    curr = 0
    best = (0, l-1)
    
    for right in range(l):
        curr += sequence[right]
        
        while curr > k and right > left:
            curr -= sequence[left]
            left += 1
        
        
        if curr == k:
            if best[1] - best[0] > right - left:
                best = (left, right)
            
    
    return [best[0], best[1]]