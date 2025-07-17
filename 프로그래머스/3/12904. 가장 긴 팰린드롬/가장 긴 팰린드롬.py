def solution(s):
    n = len(s)
    max_len = 1
    
    for center in range(n):
        left, right = center, center
        while left >= 0 and right < len(s) and s[left] == s[right]:
            max_len = max(max_len, right - left + 1)
            left -= 1
            right += 1
        
        left, right = center, center+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            max_len = max(max_len, right - left + 1)
            left -= 1
            right += 1
    return max_len